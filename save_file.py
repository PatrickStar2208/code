"""
Simple file save helper for the Hospital Management System.
Saves and loads patient and medical history data from text files.
"""

from datetime import datetime


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


def load_patient_list(filename="patients.txt"):
    """Load a list of Patient objects from a text file."""
    from patient import Patient

    patients = []
    with open(filename, "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            pid, name, age, phone, address, symptom, severity = [part.strip() for part in line.strip().split("|")]
            patients.append(
                Patient(pid=pid, name=name, age=age, phone=phone, address=address, symptom=symptom, severity=int(severity))
            )

    return patients


def save_medical_history_list(records, filename="medical_history.txt"):
    """Save a list of MedicalRecord objects to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("pid | symptom | timestamp\n")
        for history in records:
            timestamp = history.timestamp.strftime("%d/%m/%Y %H:%M:%S")
            line = f"{history.medpid} | {history.symptom} | {timestamp}\n"
            file.write(line)


def load_medical_history_list(filename="medical_history.txt"):
    """Load a list of MedicalRecord objects from a text file."""
    from MedicalHistoryManagement import MedicalRecord

    records = []
    with open(filename, "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            pid, symptom, timestamp_text = [part.strip() for part in line.strip().split("|")]
            record = MedicalRecord(medpid=pid, symptom=symptom)
            record.timestamp = datetime.strptime(timestamp_text, "%d/%m/%Y %H:%M:%S")
            records.append(record)

    return records

