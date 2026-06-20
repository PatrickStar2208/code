from MedicalHistoryManagement import MedicalHistoryManagement
from patient import patient
from patient_database import PatientDatabase
from menu import (
    display_menu, print_success, print_error, print_section,
    safe_input, input_int, Color
)


def main():
    history = MedicalHistoryManagement()
    database = PatientDatabase()

    while True:
        display_menu()
        choice = input_int("Select option: ")

        if choice == 0:
            print_section("Thank You & Goodbye!")
            print(f"  {Color.GREEN}Thanks for using Hospital Management System!{Color.END}\n")
            print(f"{Color.CYAN}{'='*60}{Color.END}\n")
            break

        if choice == 1:
            print_section("➕ ADD MEDICAL HISTORY")
            name = safe_input("Patient Name: ")
            pid = safe_input("Patient ID (Mã Bệnh Nhân): ")
            sympton = safe_input("Symptoms (Triệu Chứng): ")
            if name and pid and sympton:
                history.addrecord(patient(name, pid, sympton))
                print_success("Medical history added successfully!")
            else:
                print_error("Please enter all required information!")

        elif choice == 2:
            print_section("🗑️  DELETE LAST MEDICAL RECORD")
            history.deleteRecord()

        elif choice == 3:
            print_section("📖 DISPLAY MEDICAL HISTORY")
            history.display()

        elif choice == 4:
            print_section("🔍 FIND PATIENT HISTORY")
            pid = safe_input("Patient ID to search: ")
            if pid:
                history.getHistory(pid)
            else:
                print_error("Please enter a patient ID!")

        elif choice == 5:
            print_section("📝 REGISTER PATIENT")
            pid = safe_input("Patient ID (Mã Bệnh Nhân): ")
            name = safe_input("Patient Name (Tên Bệnh Nhân): ")
            sympton = safe_input("Symptoms (Triệu Chứng): ")
            severity = input_int("Severity Level (1-4): ")
            if pid and name and sympton and severity in [1, 2, 3, 4]:
                pat = patient(name, pid, sympton, severity)
                pat.pid = pid
                database.register_patient(pat)
                print_success("Patient registered successfully!")
            else:
                print_error("Please enter all required information!")

        elif choice == 6:
            print_section("🔎 FIND PATIENT")
            pid = safe_input("Patient ID to search: ")
            if pid:
                found = database.search_patient(pid)
                if found:
                    print(f"\n{Color.GREEN}{Color.BOLD}✓ SEARCH RESULT:{Color.END}")
                    print(f"  {found}\n")
                else:
                    print_error("Patient not found!")
            else:
                print_error("Please enter a patient ID!")

        elif choice == 7:
            print_section("✏️  UPDATE PATIENT")
            pid = safe_input("Patient ID to update: ")
            new_name = safe_input("New name (leave blank if no change): ") or None
            new_severity = input_int("New severity level (1-4, leave blank if no change): ")
            if pid:
                database.update_patient(pid, new_name=new_name, new_severity=new_severity)
                print_success("Patient information updated!")
            else:
                print_error("Please enter a patient ID!")

        elif choice == 8:
            print_section("📤 DISCHARGE PATIENT")
            pid = safe_input("Patient ID to discharge: ")
            if pid:
                database.discharge_patient(pid)
                print_success("Patient discharged successfully!")
            else:
                print_error("Please enter a patient ID!")

        elif choice == 9:
            print_section("📊 ALL PATIENTS LIST")
            database.display_all_patients()

        else:
            print_error("Invalid option! Please try again.")


if __name__ == "__main__":
    main()
