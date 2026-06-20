from datetime import datetime

class patient:
    def __init__(self, name, ID, sympton, severity):
        self.name = name
        self.ID = ID
        self.sympton = sympton
        self.severity = severity
        self.registration_time = datetime.now()
    def __str__(self):
        return f"{self.name} - {self.ID} - sympton:{self.sympton} - severity:{self.severity} - Registered: {self.registration_time.strftime( '%d/%m/%Y %H:%M:%S' )}"
