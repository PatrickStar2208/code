"""
Hospital Patient Management System - Main Application
Entry point for the hospital system. Manages all user interactions and coordinates:
- Patient Database (active registered patients)
- Medical History (all medical records as linked list)
- Menu UI (formatting and user input)
"""
import os
from MedicalHistoryManagement import MedicalHistoryManagement
from patient import Patient
from patient_database import PatientDatabase
from menu import (
    display_menu, print_success, print_error, print_section,
    safe_input, input_int, input_symptoms, Color
)


def main():
    """
    Main application loop - coordinates all system operations.
    Uses two main data structures:
    - history: Linked list for ALL medical records (from all patients)
    - database: Dictionary for ACTIVE registered patients
    """
    history = MedicalHistoryManagement()  # Linked list: stores ALL medical records
    database = PatientDatabase()  # Dictionary: stores ACTIVE patients only

    while True:  # Infinite loop until user exits
        display_menu()
        choice = input_int("Select option: ")

        # ========== CHOICE 0: EXIT ==========
        if choice == 0:
            print_section("Thank You & Goodbye!")
            print(f"  {Color.GREEN}Thanks for using Hospital Management System!{Color.END}\n")
            print(f"{Color.CYAN}{'='*60}{Color.END}\n")
            break  # Exit the infinite loop

        # ========== CHOICE 1: REGISTER NEW PATIENT ==========
        elif choice == 1:
            print_section("📝 REGISTER PATIENT")
            pid = safe_input("Patient ID: ")
            name = safe_input("Patient Name: ")
            if pid and name:
                patient = Patient(pid=pid, name=name)
                database.register_patient(patient)
                print_success("Patient registered successfully!")
            else:
                print_error("Please enter Patient ID and Name!")

        # ========== CHOICE 2: SEARCH FOR PATIENT ==========
        elif choice == 2:
            print_section("🔎 FIND PATIENT")
            pid = safe_input("Patient ID to search: ")
            if pid:
                found = database.search_patient(pid)
                if found:
                    print(found)
                else:
                    print_error("Patient not found.")
            else:
                print_error("Please enter a patient ID!")

        # ========== CHOICE 3: UPDATE PATIENT ==========
        elif choice == 3:
            print_section("✏️  UPDATE PATIENT")
            pid = safe_input("Patient ID to update: ")
            new_name = safe_input("New name (leave blank to skip): ") or None
            new_severity = input_int("New severity level 1-4 (leave blank to skip): ")
            database.update_patient(pid, new_name=new_name, new_severity=new_severity)
            print_success("Patient updated successfully!")

        # ========== CHOICE 4: DISCHARGE PATIENT ==========
        elif choice == 4:
            print_section("📤 DISCHARGE PATIENT")
            pid = safe_input("Patient ID to discharge: ")
            if pid:
                database.discharge_patient(pid)
                print_success("Patient discharged successfully!")
            else:
                print_error("Please enter a patient ID!")

        # ========== CHOICE 5: DISPLAY ALL PATIENTS ==========
        elif choice == 5:
            print_section("📊 DISPLAY ALL PATIENTS")
            database.display_all_patients()

        # ========== CHOICE 6: ADD MEDICAL HISTORY ==========
        elif choice == 6:
            print_section("➕ ADD MEDICAL HISTORY")
            pid = safe_input("Patient ID: ")
            if pid:
                found = database.search_patient(pid)
                if found:
                    symptom = input_symptoms()
                    severity = input_int("Severity Level (1-4): ")
                    if symptom and severity in [1, 2, 3, 4]:
                        history.addrecord(Patient(pid=pid, name=found.name, symptom=symptom, severity=severity))
                        print_success("Medical history added successfully!")
                    else:
                        print_error("Please enter symptoms and valid severity level!")
                else:
                    print_error("Patient ID not found in database!")
            else:
                print_error("Please enter a patient ID!")

        # ========== CHOICE 7: DELETE LAST MEDICAL RECORD ==========
        elif choice == 7:
            print_section("🗑️  DELETE LAST MEDICAL RECORD")
            history.deleteRecord()

        # ========== CHOICE 8: DISPLAY MEDICAL HISTORY ==========
        elif choice == 8:
            print_section("📖 DISPLAY MEDICAL HISTORY")
            history.display()

        # ========== CHOICE 9: FIND SPECIFIC PATIENT'S HISTORY ==========
        elif choice == 9:
            print_section("🔍 FIND PATIENT HISTORY")
            pid = safe_input("Patient ID to search: ")
            if pid:
                history.getHistory(pid)
            else:
                print_error("Please enter a patient ID!")

        # ========== CHOICE 10: UPDATE MEDICAL HISTORY ==========
        elif choice == 10:
            print_section("🛠️ UPDATE MEDICAL HISTORY")
            pid = safe_input("Patient ID to update history for: ")
            if pid:
                new_symptom = input_symptoms("New symptoms (comma-separated): ")
                if new_symptom:
                    updated = history.updateRecord(pid, new_symptom)
                    if updated:
                        print_success("Medical history updated successfully!")
                    else:
                        print_error("No medical history found for this patient.")
                else:
                    print_error("Please enter new symptoms!")
            else:
                print_error("Please enter a patient ID!")

        # ========== INVALID CHOICE ==========
        else:
            print_error("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
