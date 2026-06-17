from patient import Patient
from patient_database import PatientDatabase
from emergency_queue import EmergencyQueue

class TriageSystem:

    def __init__(self):

        self.database = PatientDatabase()
        self.queue = EmergencyQueue()

    def admit_patient(self,pid,name,severity):

        patient = Patient(pid,name,severity)

        self.database.register_patient(patient)

        self.queue.enqueue(patient)

    def process_next_patient(self):

        patient = self.queue.call_next_patient()

        if patient:
            self.database.discharge_patient(patient.pid)

    def show_status(self):

        self.database.display_all_patients()

        self.queue.display_queue()