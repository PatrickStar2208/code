"""
Hospital Patient Management System - Main Application
Entry point for the hospital system. Manages all user interactions and coordinates:
- Patient Database (active registered patients)
- Medical History (all medical records as linked list)
- Menu UI (formatting and user input)
"""
from MedicalHistoryManagement import MedicalHistoryManagement, MedicalRecord
from patient import Patient
from patient_database import PatientDatabase
from triage_patient import EmergencyQueue
from save_file import load_patient_list, load_medical_history_list


DEFAULT_PATIENT_FILE = "patients.txt"
DEFAULT_HISTORY_FILE = "medical_history.txt"
from menu import (
    display_menu, print_success, print_error, print_section,
    safe_input, input_int, input_symptoms, input_age, input_phone, input_address, Color, InputCancelledError
)


def register_patient_with_history(database, history, queue, patient):
    """Register a patient and create an initial medical history entry from the given symptoms."""
    registered = database.register_patient(patient)
    if not registered:
        return False

    queue.add_patient(patient)

    if patient.symptom and not history.find_records(patient.pid):
        history.add_record(patient.pid, patient.symptom)

    return True


def persist_data(database, history, patient_file=DEFAULT_PATIENT_FILE, history_file=DEFAULT_HISTORY_FILE):
    """Save patient and medical history data automatically."""
    database.save(patient_file)
    history.save(history_file)


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

    # Load saved data from text files when the program starts
    try:
        for patient in load_patient_list(DEFAULT_PATIENT_FILE):
            database.register_patient(patient)
            queue.add_patient(patient)
    except FileNotFoundError:
        pass

    try:
        for record in load_medical_history_list(DEFAULT_HISTORY_FILE):
            history.add_record(record.medpid, record.symptom)
    except FileNotFoundError:
        pass

    while True:  # Infinite loop until user exits
        display_menu()
        choice = input_int("Select option: ")

        # Handle None or invalid choice
        if choice is None or choice < 0:
            print_error("Please enter a valid menu option (0-11)!")
            continue

        # ========== CHOICE 0: EXIT ==========
        if choice == 0:
            print_section("Thank You & Goodbye!")
            print(f"  {Color.GREEN}Thanks for using Hospital Management System!{Color.END}\n")
            print(f"{Color.CYAN}{'='*60}{Color.END}\n")
            break

        # ========== CHOICE 1: REGISTER NEW PATIENT ==========
        elif choice == 1:
            try:
                print_section("📝 REGISTER PATIENT")
                pid = safe_input("Patient ID: ")
                name = safe_input("Patient Name: ")
                age = input_age()
                phone = input_phone()
                address = input_address()
                symptom = input_symptoms()
                severity = input_int("Severity Level (1-4): ")

                if not pid or not name:
                    raise InputCancelledError("Please enter Patient ID and Name!")
                if age is None:
                    raise InputCancelledError("Please provide a valid age!")
                if phone is None:
                    raise InputCancelledError("Please provide a valid phone number!")
                if address is None:
                    raise InputCancelledError("Please provide a valid address!")
                if severity is None or severity not in [1, 2, 3, 4]:
                    raise InputCancelledError("Please enter a valid severity level (1-4)!")

                patient = Patient(pid=pid, name=name, age=age, phone=phone, address=address, symptom=symptom, severity=severity)
                ok = register_patient_with_history(database, history, queue, patient)
                if ok:
                    persist_data(database, history)
                    print_success("Patient registered and added to triage queue successfully!")
                else:
                    print_error("Registration failed: duplicate patient ID.")
            except InputCancelledError as exc:
                print_error(str(exc))

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
            try:
                print_section("✏️  UPDATE PATIENT")
                pid = safe_input("Patient ID to update: ")
                if not pid:
                    raise InputCancelledError("Please enter a patient ID!")

                new_name = safe_input("New name (leave blank to skip): ", allow_blank=True) or None
                new_age = input_age("New age (leave blank to skip): ", allow_blank=True)
                new_phone = input_phone("New phone (leave blank to skip): ", allow_blank=True)
                new_address = input_address("New address (leave blank to skip): ", allow_blank=True)
                new_symptom = input_symptoms("New symptoms (leave blank to skip): ", allow_blank=True) or None
                new_severity = input_int("New severity level 1-4 (leave blank to skip): ", allow_blank=True)

                updated = database.update_patient(pid, new_name=new_name, new_age=new_age, new_phone=new_phone, new_address=new_address, new_symptom=new_symptom, new_severity=new_severity)
                if updated:
                    if new_severity is not None:
                        queue.update_patient_severity(pid, new_severity)
                    persist_data(database, history)
                    print_success("Patient updated successfully!")
                else:
                    print_error("Patient not found.")
            except InputCancelledError as exc:
                print_error(str(exc))

        # ========== CHOICE 4: DISCHARGE PATIENT ==========
        elif choice == 4:
            try:
                print_section("📤 DISCHARGE PATIENT")
                pid = safe_input("Patient ID to discharge: ")
                if not pid:
                    raise InputCancelledError("Please enter a patient ID!")

                removed = database.discharge_patient(pid)
                if removed:
                    queue.remove_patient(pid)
                    persist_data(database, history)
                    print_success("Patient discharged successfully!")
                else:
                    print_error("Patient not found.")
            except InputCancelledError as exc:
                print_error(str(exc))

        # ========== CHOICE 5: DISPLAY ALL PATIENTS ==========
        elif choice == 5:
            print_section("📊 DISPLAY ALL PATIENTS")
            database.display_all_patients()

        # ========== CHOICE 6: DELETE LAST MEDICAL RECORD ==========
        elif choice == 6:
            try:
                print_section("🗑️ DELETE RECORD")
                pid = safe_input("Patient ID of record to delete: ")
                if not pid:
                    raise InputCancelledError("Please enter a patient ID!")

                history.delete_record_by_pid(pid)
                persist_data(database, history)
            except InputCancelledError as exc:
                print_error(str(exc))

        # ========== CHOICE 7: DISPLAY MEDICAL HISTORY ==========
        elif choice == 7:
            print_section("📖 DISPLAY MEDICAL HISTORY")
            if history.is_empty():
                print_error("No medical history records found.")
            else:
                history.display_history()

        # ========== CHOICE 8: FIND SPECIFIC PATIENT'S HISTORY ==========
        elif choice == 8:
            try:
                print_section("🔍 FIND PATIENT HISTORY")
                medpid = safe_input("Patient ID to search: ")
                if not medpid:
                    raise InputCancelledError("Please enter a patient ID!")
                history.find_records(medpid)
            except InputCancelledError as exc:
                print_error(str(exc))

        # ========== CHOICE 9: ADD NEW MEDICAL RECORD ==========
        elif choice == 9:
            try:
                print_section("📝 ADD NEW MEDICAL RECORD")
                name = safe_input("Patient name: ")
                phone = safe_input("Patient phone: ")
                if not name or not phone:
                    raise InputCancelledError("Please enter patient name and phone number!")

                new_symptom = input_symptoms("New symptoms (comma-separated): ")
                if not new_symptom:
                    raise InputCancelledError("Please enter new symptoms!")

                updated = history.add_record_by_patient(database, name, phone, new_symptom)
                if updated:
                    persist_data(database, history)
                    print_success("New medical record added successfully!")
                else:
                    print_error("No matching patient found.")
            except InputCancelledError as exc:
                print_error(str(exc))

        # ========== CHOICE 10: PROCESS NEXT PATIENT (CALL ONLY) ==========
        elif choice == 10:
            print_section("🚑 PROCESS NEXT PATIENT")
            patient = queue.call_next_patient()
            if patient:
                print_success(f"Called patient {patient.pid} - {patient.name}. Patient remains in active database until discharged separately.")
            else:
                print_error("No patients in queue.")

        elif choice == 11:
            print_section("📥 DISPLAY QUEUE")
            queue.display_queue()

        else:
            print_error("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
