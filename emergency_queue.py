from node import node


class EmergencyQueue:
    def __init__(self):
        self.front = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, patient):
        new_node = node(patient)

        if self.is_empty():
            self.front = new_node
            return

        if patient.severity < self.front.patient.severity:
            new_node.next = self.front
            self.front = new_node
            return

        current = self.front
        while current.next and current.next.patient.severity <= patient.severity:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        patient = self.front.patient
        self.front = self.front.next
        return patient

    def call_next_patient(self):
        patient = self.dequeue()

        if patient:
            print(f"\nNow Treating: {patient}")
        else:
            print("\nNo patients waiting.")

        return patient

    def display_queue(self):
        if self.is_empty():
            print("\nQueue Empty")
            return

        current = self.front
        print("\nEmergency Queue")
        while current:
            print(current.patient)
            current = current.next