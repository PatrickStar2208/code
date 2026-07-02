import tempfile
import unittest
from pathlib import Path

from save_file import load_medical_history_list, load_patient_list


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


if __name__ == "__main__":
    unittest.main()
