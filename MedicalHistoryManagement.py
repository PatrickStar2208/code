from node import node


class MedicalHistoryManagement:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def addrecord(self, newrecord):
        newPatient = node(newrecord)
        if self.size == 0:
            self.head = newPatient
            self.tail = newPatient
        else:
            self.tail.next = newPatient
            newPatient.prev = self.tail
            self.tail = newPatient
        self.size += 1

    def deleteRecord(self):
        if self.size == 0:
            return None
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            nearTail = self.tail.prev
            self.tail = nearTail
            nearTail.next = None
        self.size -= 1
        return True

    def getHistory(self, patient):
        currentPatient = self.head
        while currentPatient is not None:
            if currentPatient.value.pid == patient or currentPatient.value.ID == patient:
                print(currentPatient.value)
                return currentPatient.value
            currentPatient = currentPatient.next
        print("Không tìm thấy lịch sử cho bệnh nhân này.")
        return None

    def display(self):
        currentPatient = self.head
        while currentPatient is not None:
            print(currentPatient.value)
            currentPatient = currentPatient.next

