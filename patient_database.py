class PatientDatabase:
    def __init__(self):
        self.patients = {}

    def register_patient(self, patient):
        if patient.pid in self.patients:
            print(f"Patient {patient.pid} already exists.")
            return

        self.patients[patient.pid] = patient
        print(f"Registered: {patient.pid} - {patient.name}")

    def search_patient(self, patient_id):
        return self.patients.get(patient_id)

    def update_patient(self, patient_id, new_name=None, new_severity=None):
        patient = self.patients.get(patient_id)
        if patient is None:
            print("Patient not found.")
            return

        if new_name:
            patient.name = new_name

        if new_severity is not None:
            patient.severity = new_severity

        print(f"Updated: {patient}")

    def discharge_patient(self, patient_id):
        removed = self.patients.pop(patient_id, None)
        if removed is None:
            print("Patient not found.")
            return None

        print(f"Discharged: {removed}")
        return removed

    def display_all_patients(self):
        print("\nPatient Database")
        if not self.patients:
            print("No patients registered.")
            return

        for patient in self.patients.values():
            print(patient)