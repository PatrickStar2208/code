import heapq
from datetime import datetime

from patient import Patient


class EmergencyQueue:
    SEVERITY_NAMES = {
        1: "Critical",
        2: "Urgent",
        3: "Moderate",
        4: "Normal",
    }

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return not self.queue

    def get_severity_name(self, severity):
        return self.SEVERITY_NAMES.get(severity, "Unknown")

    def add_patient(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Expected a Patient object")

        heapq.heappush(self.queue, (patient.severity, patient.arrival_time, patient.pid, patient))
        return True

    def call_next_patient(self):
        if self.is_empty():
            return None

        _, _, _, patient = heapq.heappop(self.queue)
        return patient

    def display_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Current Emergency Queue:")
        for priority, _, _, patient in sorted(self.queue):
            severity_text = self.get_severity_name(patient.severity)
            readable_time = datetime.fromtimestamp(patient.arrival_time).strftime("%H:%M:%S %d/%m/%Y")
            print(
                f"Priority {priority}, ID {patient.pid}, Name {patient.name}, "
                f"Severity {severity_text}, Arrival {readable_time}"
            )

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0][3]

    def update_patient_severity(self, pid, new_severity):
        if new_severity not in self.SEVERITY_NAMES:
            return False

        for index, entry in enumerate(self.queue):
            _, _, current_pid, patient = entry
            if current_pid == pid:
                self.queue.pop(index)
                heapq.heapify(self.queue)
                patient.severity = new_severity
                heapq.heappush(self.queue, (patient.severity, patient.arrival_time, patient.pid, patient))
                return True
        return False

    def remove_patient(self, pid):
        for index, entry in enumerate(self.queue):
            _, _, current_pid, _ = entry
            if current_pid == pid:
                self.queue.pop(index)
                heapq.heapify(self.queue)
                return True
        return False

    def size(self):
        return len(self.queue)
