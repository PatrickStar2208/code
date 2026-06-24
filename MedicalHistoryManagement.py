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
        return f"{self.medpid} - {self.symptom} - {self.timestamp.strftime('%d/%m/%Y %H:%M:%S')}"


class MedicalHistoryManagement:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

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
        return True

    def update_record(self, pid, new_symptom):
        if not pid or not new_symptom:
            return False

        current = self.head
        last_record = None
        while current is not None:
            if current.value.pid == pid:
                last_record = current
            current = current.next

        if last_record is None:
            return False

        last_record.value.symptom = new_symptom
        last_record.value.timestamp = datetime.now()
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

    def display_history(self):
        if self.is_empty():
            print("No medical history records.")
            return

        print("Medical History Records:")
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def save(self, filename="medical_history.txt"):
        """Save the current list of medical history records to a text file."""
        records = []
        current = self.head
        while current is not None:
            records.append(current.value)
            current = current.next
        save_medical_history_list(records, filename)

