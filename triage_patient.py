import heapq
from patient import Patient
from datetime import datetime
class Emergency_queue:
    def __init__(self):
        self.queue = []
    # Convert severity number into text
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
    # Add patient into queue
    def add_patient(self, patient):
        heapq.heappush(self.queue, (patient.severity, patient.arrival_time, patient.pid, patient))
        print(f"Added patient {patient}")
    # Remove highest priority pantient
    def call_next_patient(self):
        if self.isEmpty():
            print("No more patients to call")
            return None
        priority, arrival_time, pid, patient = heapq.heappop(self.queue)
        print(f"Calling next patient {patient}")
        return patient
    def display_queue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        print("Current Emergency Queue: ")
        sorted_queue = sorted(self.queue)
        for priority, arrival_time, pid, patient in sorted_queue:
            severity_text =(self.get_severity_name(patient.severity))
            time_obj = datetime.fromtimestamp(patient.arrival_time)
            readable_time = time_obj.strftime("%H:%M:%S %d/%m/%Y")
            print(
                f"Priority {priority}, "
                f"ID {patient.pid}, "
                f"Patient {patient.name}, "
                f"Age {patient.age}, "
                f"Severity {severity_text}, "
                f"Arrival_time {readable_time}, "
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
        for i in range(len(self.queue)):
            priority, arrival_time, pid, patient = (self.queue[i])
            if patient.pid == pid:
                self.queue.pop(i)
                heapq.heapify(self.queue)
                patient.severity = new_severity
                heapq.heappush(self.queue, (patient.severity, patient.arrival_time, patient.pid, patient))
                severity_text = (self.get_severity_name(patient.severity))
                return
        print("Patient not found")
    def size(self):
        return len(self.queue)
