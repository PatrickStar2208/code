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
from save_file import save_patient_list
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

        # Handle None or invalid choice
        if choice is None or choice < 0:
            print_error("Please enter a valid menu option (0-13)!")
            continue

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

            # Validate all inputs
            if not pid or not name:
                print_error("Please enter Patient ID and Name!")
            elif age is None:
                print_error("Please provide a valid age!")
            elif phone is None:
                print_error("Please provide a valid phone number!")
            elif address is None:
                print_error("Please provide a valid address!")
            elif severity is None or severity not in [1, 2, 3, 4]:
                print_error("Please enter a valid severity level (1-4)!")
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
            if not pid:
                print_error("Please enter a patient ID!")
            else:
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
            medpid = safe_input("Patient ID: ")
            if not medpid:
                print_error("Please enter a patient ID!")
                continue

            patient = database.search_patient(medpid)
            if not patient:
                print_error("Patient not found. Please register the patient first.")
                continue

            if history.find_records(medpid):
                print_error("Patient already has a medical history record. Please update the existing record instead.")
                continue

            symptom = input_symptoms("Symptoms (comma-separated): ")
            if not symptom:
                print_error("Please enter symptoms!")
                continue

            # only add symptoms, severity, and timestamps in medical history; other patient info is already in the database
            new_record = Patient(pid=medpid, name=patient.name, symptom=symptom, severity=patient.severity)
            history.add_record(new_record, symptom)
            print_success("Medical history record added successfully!")


        # ========== CHOICE 7: DELETE LAST MEDICAL RECORD ==========
        elif choice == 7:
            print_section("🗑️ DELETE RECORD")
            pid = safe_input("Patient ID of record to delete: ")
            if pid:
                history.delete_record_by_pid(pid)
            else:
                print_error("Please enter a patient ID!")

        # ========== CHOICE 8: DISPLAY MEDICAL HISTORY ==========
        elif choice == 8:
            print_section("📖 DISPLAY MEDICAL HISTORY")
            if history.is_empty():
                print_error("No medical history records found.")
            else:
                history.display_history()

        # ========== CHOICE 9: FIND SPECIFIC PATIENT'S HISTORY ==========
        elif choice == 9:
            print_section("🔍 FIND PATIENT HISTORY")
            medpid = safe_input("Patient ID to search: ")
            if medpid:
                history.find_records(medpid)
            else:
                print_error("Please enter a patient ID!")

        # ========== CHOICE 10: UPDATE MEDICAL HISTORY ==========
        elif choice == 10:
            print_section("🛠️ UPDATE MEDICAL HISTORY")
            medpid = safe_input("Patient ID to update history for: ")
            if medpid:
                new_symptom = input_symptoms("New symptoms (comma-separated): ")
                if new_symptom:
                    updated = history.updateRecord(medpid, new_symptom)
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
        
        elif choice == 12:
            print_section("💾 SAVE PATIENTS TO FILE")
            filename = safe_input("Enter filename to save (default: patients.txt): ") or "patients.txt"
            database.save(filename)
            print_success(f"Patient records saved to {filename} successfully!")
        
        elif choice == 13:
            print_section("💾 SAVE MEDICAL HISTORY TO FILE")
            filename = safe_input("Enter filename to save (default: medical_history.txt): ") or "medical_history.txt"
            history.save(filename)
            print_success(f"Medical history records saved to {filename} successfully!")
        

        # ========== INVALID CHOICE ==========
        else:
            print_error("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

