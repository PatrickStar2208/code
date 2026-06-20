from patient import Patient
from patient_database import PatientDatabase
from triage_patient import EmergencyQueue


class TriageSystem:
    def __init__(self, database=None):
        # Allow injecting an existing PatientDatabase to keep a single source of truth
        self.database = database if database is not None else PatientDatabase()
        self.queue = EmergencyQueue()

    def admit_patient(self, patient):
        # patient: Patient object already created
        self.database.register_patient(patient)
        self.queue.add_patient(patient)

    def process_next_patient(self):
        patient = self.queue.call_next_patient()
        if patient:
            # Do not discharge automatically; calling the patient is separate from discharge.
            return patient

    def show_status(self):
        self.database.display_all_patients()
        self.queue.display_queue()