import tempfile
import unittest
from pathlib import Path

from MedicalHistoryManagement import MedicalHistoryManagement
from patient import Patient
from patient_database import PatientDatabase
from save_file import load_medical_history_list, load_patient_list
from triage_patient import EmergencyQueue


class DataLoadingTests(unittest.TestCase):
    def test_load_patient_and_history_from_txt(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            patient_file = Path(tmpdir) / "patients.txt"
            history_file = Path(tmpdir) / "medical_history.txt"

            patient_file.write_text(
                "pid | name | age | phone | address | symptom | severity\np1 | Ana | 30 | 123 | Main St | cough | 2\n",
                encoding="utf-8",
            )
            history_file.write_text(
                "pid | symptom | timestamp\np1 | cough | 01/01/2026 00:00:00\n",
                encoding="utf-8",
            )

            patients = load_patient_list(str(patient_file))
            records = load_medical_history_list(str(history_file))

            self.assertEqual(len(patients), 1)
            self.assertEqual(patients[0].name, "Ana")
            self.assertEqual(patients[0].severity, 2)

            self.assertEqual(len(records), 1)
            self.assertEqual(records[0].symptom, "cough")

    def test_register_patient_auto_creates_medical_history_from_symptoms(self):
        from main import register_patient_with_history

        database = PatientDatabase()
        history = MedicalHistoryManagement()
        queue = EmergencyQueue()
        patient = Patient(pid="p2", name="Bob", age=25, phone="456", address="Elm St", symptom="fever", severity=3)

        result = register_patient_with_history(database, history, queue, patient)

        self.assertTrue(result)
        self.assertEqual(database.search_patient("p2").name, "Bob")
        records = history.find_records("p2")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].symptom, "fever")

    def test_persist_data_saves_patient_and_history(self):
        from main import persist_data, register_patient_with_history

        with tempfile.TemporaryDirectory() as tmpdir:
            patient_file = Path(tmpdir) / "patients.txt"
            history_file = Path(tmpdir) / "medical_history.txt"

            database = PatientDatabase()
            history = MedicalHistoryManagement()
            queue = EmergencyQueue()
            patient = Patient(pid="p3", name="Cara", age=32, phone="789", address="Maple St", symptom="cough", severity=2)

            register_patient_with_history(database, history, queue, patient)
            persist_data(database, history, str(patient_file), str(history_file))

            saved_patients = load_patient_list(str(patient_file))
            saved_records = load_medical_history_list(str(history_file))

            self.assertEqual(len(saved_patients), 1)
            self.assertEqual(saved_patients[0].pid, "p3")
            self.assertEqual(len(saved_records), 1)
            self.assertEqual(saved_records[0].symptom, "cough")


if __name__ == "__main__":
    unittest.main()
