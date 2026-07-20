"""
Medical history manager using a simple doubly-linked list.
Each medical history record stores a patient ID and symptoms.
"""

from datetime import datetime
from node import Node
from save_file import save_medical_history_list  # Import the save function to save medical history records to a file

class MedicalRecord:
    def __init__(self, medpid, symptom):
        self.medpid = medpid
        self.symptom = symptom
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.medpid} | {self.symptom} | {self.timestamp.strftime('%d/%m/%Y %H:%M:%S')}"


class MedicalHistoryManagement:
    def __init__(self, filename="medical_history.txt"):
        self.head = None
        self.tail = None
        self.size = 0
        self.filename = filename

    def is_empty(self):
        return self.size == 0

    def add_record(self, pid, symptom):
        if not pid or not symptom:
            return False

        record = MedicalRecord(pid, symptom)
        node = Node(record)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1
        self.save(self.filename)
        return True

    def update_record(self, pid, new_symptom):
        if not pid or not new_symptom:
            return False

        current = self.head
        last_record = None
        while current is not None:
            if current.value.medpid == pid:
                last_record = current
            current = current.next

        if last_record is None:
            return False

        last_record.value.symptom = new_symptom
        last_record.value.timestamp = datetime.now()
        self.save(self.filename)
        return True

    def add_record_by_patient(self, database, name, phone, symptom):
        """Find a patient by name and phone, then add a new medical history record for them."""
        if not name or not phone or not symptom:
            return False

        patient = None
        for existing_patient in database.patients.values():
            if existing_patient.name.lower() == name.lower() and existing_patient.phone == phone:
                patient = existing_patient
                break

        if patient is None:
            return False

        self.add_record(patient.pid, symptom)
        return True

    def delete_record_by_pid(self, pid):
        if not pid:
            return False
        current = self.head
        while current is not None:
            if current.value.medpid == pid:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.size -= 1
                self.save(self.filename)
                return True
            current = current.next

    def find_records(self, pid):
        records = []
        current = self.head
        while current is not None:
            if current.value.medpid == pid:
                records.append(current.value)
            current = current.next
        return records

    def find_records_by_patient(self, database, name, phone):
        """Find medical history records by patient name and phone number."""
        patient = database.search_patient_by_name_and_phone(name, phone)
        if patient is None:
            return []
        return self.find_records(patient.pid)

    def display_history(self):
        if self.is_empty():
            print("No medical history records.")
            return

        print("Medical History Records:")
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def save(self, filename=None):
        """Save the current list of medical history records to a text file."""
        target_file = filename or self.filename
        records = []
        current = self.head
        while current is not None:
            records.append(current.value)
            current = current.next
        save_medical_history_list(records, target_file)

