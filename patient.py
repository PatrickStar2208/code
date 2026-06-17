from datetime import datetime


class Patient:
    def __init__(self, pid, name, symptom="", severity=4):
        self.pid = pid
        self.ID = pid
        self.name = name
        self.symptom = symptom
        self.sympton = symptom
        self.severity = severity
        self.registration_time = datetime.now()
        self.arrival_time = self.registration_time.timestamp()

    def __str__(self):
        return (
            f"{self.name} - {self.pid} - symptom:{self.symptom} "
            f"- severity:{self.severity} - Registered: "
            f"{self.registration_time.strftime('%d/%m/%Y %H:%M:%S')}"
        )


patient = Patient
