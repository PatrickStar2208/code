class PatientDatabase:

    def __init__(self):
        self.patients = {}

    def register_patient(self, patient):

        self.patients[patient.pid] = patient

        print(f"Registered: {patient.pid} - {patient.name}")

    def search_patient(self, patient_id):

        return self.patients.get(patient_id)
        
        if patient:
            return patient

        return None

    def update_patient(self, patient_id, new_name=None, new_severity=None):

        if patient_id not in self.patients:
            print("Patient not found.")
            return

        patient = self.patients[patient_id]

        if new_name:
            patient.name = new_name

        if new_severity is not None:
            patient.severity = new_severity

        print(f"Updated: {patient}")

    def discharge_patient(self, patient_id):

        if patient_id not in self.patients:
            print("Patient not found.")
            return

        removed = self.patients.pop(patient_id)

        print(f"Discharged: {removed}")

        return removed

    def display_all_patients(self):

        print("\n Patient Database ")

        for patient in self.patients.values():
            print(patient)