import time
from datetime import datetime
class Patient:
    def __init__(self, pid, name , age, severity):
        self.name = name
        self.pid = pid
        self.severity = severity
        self.age = age
        self.arrival_time = time.time()
    def __str__(self):
        time_obj = datetime.fromtimestamp(self.arrival_time)
        readable_time = time_obj.strftime('%Y-%m-%d %H:%M:%S')
        return f"Patient {self.pid} {self.name} {self.age} {self.severity} {readable_time}"