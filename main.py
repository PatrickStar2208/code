from MedicalHistoryManagement import MedicalHistoryManagement
from patient import Patient
from patient_database import PatientDatabase


def input_int(prompt, default=None):
    try:
        return int(input(prompt).strip())
    except ValueError:
        return default


def main():
    history = MedicalHistoryManagement()
    database = PatientDatabase()

    while True:
        print("\n=== Emergency System Menu ===")
        print("1. Thêm lịch sử y tế")
        print("2. Xóa lịch sử y tế cuối")
        print("3. Hiển thị lịch sử y tế")
        print("4. Tìm lịch sử bệnh nhân")
        print("5. Đăng ký bệnh nhân")
        print("6. Tìm bệnh nhân")
        print("7. Cập nhật bệnh nhân")
        print("8. Xuất viện bệnh nhân")
        print("9. Xuất tất cả bệnh nhân")
        print("0. Thoát")

        choice = input_int("Chọn số: ")

        if choice == 0:
            print("Thoát chương trình.")
            break

        if choice == 1:
            pid = input("Mã bệnh nhân: ").strip()
            name = input("Tên bệnh nhân: ").strip()
            symptom = input("Triệu chứng: ").strip()
            history.addrecord(Patient(pid=pid, name=name, symptom=symptom))

        elif choice == 2:
            history.deleteRecord()

        elif choice == 3:
            history.display()

        elif choice == 4:
            pid = input("Mã bệnh nhân cần tìm: ").strip()
            history.getHistory(pid)

        elif choice == 5:
            pid = input("Mã bệnh nhân: ").strip()
            name = input("Tên bệnh nhân: ").strip()
            symptom = input("Triệu chứng: ").strip()
            patient = Patient(pid=pid, name=name, symptom=symptom)
            database.register_patient(patient)

        elif choice == 6:
            pid = input("Mã bệnh nhân cần tìm: ").strip()
            found = database.search_patient(pid)
            if found:
                print(found)
            else:
                print("Patient not found.")

        elif choice == 7:
            pid = input("Mã bệnh nhân cần cập nhật: ").strip()
            new_name = input("Tên mới (để trống nếu không đổi): ").strip() or None
            new_severity = input_int("Mức độ mới (1-4, để trống nếu không đổi): ")
            database.update_patient(pid, new_name=new_name, new_severity=new_severity)

        elif choice == 8:
            pid = input("Mã bệnh nhân cần xuất viện: ").strip()
            database.discharge_patient(pid)

        elif choice == 9:
            database.display_all_patients()

        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()
