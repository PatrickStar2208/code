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
from triage_patient import EmergencyQueue
from menu import (
    display_menu, print_success, print_error, print_section,
    safe_input, input_int, input_symptoms, input_age, input_phone, input_address, Color
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
    queue = EmergencyQueue()  # Priority queue for emergency triage

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
            age = input_age()
            phone = input_phone()
            address = input_address()
            symptom = input_symptoms()
            severity = input_int("Severity Level (1-4): ")

            if not pid or not name:
                print_error("Please enter Patient ID and Name!")
            elif age is None or phone is None or address is None:
                print_error("Please provide valid age, phone, and address!")
            elif severity not in [1, 2, 3, 4]:
                print_error("Please enter a valid severity level 1-4")
            else:
                patient = Patient(pid=pid, name=name, age=age, phone=phone, address=address, symptom=symptom, severity=severity)
                ok = database.register_patient(patient)
                if ok:
                    queue.add_patient(patient)
                    print_success("Patient registered and added to triage queue successfully!")
                else:
                    print_error("Registration failed: duplicate patient ID.")

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
            new_age = input_age("New age (leave blank to skip): ")
            new_phone = input_phone("New phone (leave blank to skip): ")
            new_address = input_address("New address (leave blank to skip): ")
            new_symptom = input_symptoms("New symptoms (leave blank to skip): ") or None
            new_severity = input_int("New severity level 1-4 (leave blank to skip): ")

            updated = database.update_patient(pid, new_name=new_name, new_age=new_age, new_phone=new_phone, new_address=new_address, new_symptom=new_symptom, new_severity=new_severity)
            if updated:
                # If severity changed, reflect in queue as well
                if new_severity is not None:
                    queue.update_patient_severity(pid, new_severity)
                print_success("Patient updated successfully!")
            else:
                print_error("Patient not found.")

        # ========== CHOICE 4: DISCHARGE PATIENT ==========
        elif choice == 4:
            print_section("📤 DISCHARGE PATIENT")
            pid = safe_input("Patient ID to discharge: ")
            if pid:
                removed = database.discharge_patient(pid)
                if removed:
                    # Also remove from triage queue if present
                    queue.remove_patient(pid)
                    print_success("Patient discharged successfully!")
                else:
                    print_error("Patient not found.")
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
            if not pid:
                print_error("Please enter a patient ID!")
                continue

            patient = database.search_patient(pid)
            if not patient:
                print_error("Patient not found. Please register the patient first.")
                continue

            if history.has_history(pid):
                print_error("Patient already has a medical history record. Please update the existing record instead.")
                continue

            symptom = input_symptoms("Symptoms (comma-separated): ")
            if not symptom:
                print_error("Please enter symptoms!")
                continue

            new_record = Patient(
                pid=pid,
                name=patient.name,
                age=patient.age,
                phone=patient.phone,
                address=patient.address,
                symptom=symptom,
                severity=patient.severity,
            )
            history.addrecord(new_record)
            print_success("Medical history record added successfully!")


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

        # ========== CHOICE 11: PROCESS NEXT PATIENT (CALL ONLY) ==========
        elif choice == 11:
            print_section("🚑 PROCESS NEXT PATIENT")
            # call_next_patient pops the highest-priority patient from the queue
            patient = queue.call_next_patient()
            if patient:
                print_success(f"Called patient {patient.pid} - {patient.name}. Patient remains in active database until discharged separately.")
            else:
                print_error("No patients in queue.")

        # ========== INVALID CHOICE ==========
        else:
            print_error("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
