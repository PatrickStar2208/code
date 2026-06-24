"""
Simple file save helper for the Hospital Management System.
Saves a list of patients to a text file.
"""


def save_patient_list(patients, filename="patients.txt"):
    """Save a list of Patient objects to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("pid | name | age | phone | address | symptom | severity\n")
        for patient in patients:
            line = (
                f"{patient.pid} | {patient.name} | {patient.age} | "
                f"{patient.phone} | {patient.address} | {patient.symptom} | {patient.severity}\n"
            )
            file.write(line)

def save_medical_history_list(records, filename="medical_history.txt"):
    """Save a list of MedicalRecord objects to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("pid | symptom | timestamp\n")
        for history in records:
            line = (
                f"{history.medpid}")
            file.write(line)

if __name__ == "__main__":
    print("Import save_patient_list() to save patient records to a text file.")
