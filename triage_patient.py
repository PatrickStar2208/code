import heapq
from datetime import datetime

from patient import Patient


class EmergencyQueue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def get_severity_name(self, severity):
        priority_levels = {
            1: "Critical",
            2: "Urgent",
            3: "Moderate",
            4: "Normal"
        }
        return priority_levels.get(severity, "Unknown")

    def add_patient(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Expected a Patient object")
        heapq.heappush(self.queue, (patient.severity, patient.arrival_time, patient.pid, patient))
        print(f"Added patient {patient}")

    def call_next_patient(self):
        if self.isEmpty():
            print("No more patients to call")
            return None
        _, _, _, patient = heapq.heappop(self.queue)
        print(f"Calling next patient {patient}")
        return patient

    def display_queue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None

        print("Current Emergency Queue:")
        for priority, _, _, patient in sorted(self.queue):
            severity_text = self.get_severity_name(patient.severity)
            readable_time = datetime.fromtimestamp(patient.arrival_time).strftime("%H:%M:%S %d/%m/%Y")
            print(
                f"Priority {priority}, "
                f"ID {patient.pid}, "
                f"Patient {patient.name}, "
                f"Severity {severity_text}, "
                f"Arrival_time {readable_time}"
            )

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue[0][3]

    def update_patient_severity(self, pid, new_severity):
        if new_severity not in [1, 2, 3, 4]:
            print("Invalid severity")
            return

        for i, item in enumerate(self.queue):
            _, _, current_pid, patient = item
            if current_pid == pid:
                self.queue.pop(i)
                heapq.heapify(self.queue)
                patient.severity = new_severity
                heapq.heappush(self.queue, (patient.severity, patient.arrival_time, patient.pid, patient))
                return

        print("Patient not found")

    def size(self):
        return len(self.queue)
