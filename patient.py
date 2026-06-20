"""
Patient Data Model
Represents a single patient with their basic information.
Used as the value stored in both PatientDatabase and MedicalHistory.
"""
from datetime import datetime


class Patient:
    """
    Represents a patient record.
    
    Attributes:
        pid (str): Patient ID - unique identifier
        name (str): Patient's full name
        symptom (str): Medical symptoms (can be comma-separated)
        severity (int): Emergency severity (1=lowest, 4=highest)
        registration_time (datetime): When patient was registered
        arrival_time (float): Unix timestamp of registration
    """
    def __init__(self, pid, name, age=0, phone="", address="", symptom="", severity=4):
        """
        Initialize a new patient.
        
        Args:
            pid (str): Unique patient identifier
            name (str): Patient's name
            symptom (str): Patient's symptoms (default empty string)
            severity (int): Severity level 1-4 (default 4 = highest)
        """
        # Basic patient identity and contact info
        self.pid = pid  # Primary identifier (string)
        self.name = name
        self.age = int(age) if age is not None and age != "" else 0
        self.phone = phone
        self.address = address
        # Medical info
        self.symptom = symptom  # Standardized spelling
        self.severity = severity
        self.registration_time = datetime.now()  # Current date/time
        self.arrival_time = self.registration_time.timestamp()  # Seconds since epoch

    def __str__(self):
        """
        String representation for printing patient information.
        Used when displaying patient records.
        """
        return (
            f"{self.pid} - {self.name} - age:{self.age} - phone:{self.phone} - "
            f"address:{self.address} - symptom:{self.symptom} - severity:{self.severity} - "
            f"Registered: {self.registration_time.strftime('%d/%m/%Y %H:%M:%S')}"
        )


# Alias for backward compatibility (lowercase 'patient' = class 'Patient')
patient = Patient
