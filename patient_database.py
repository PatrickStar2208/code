"""
Patient Database Module
Manages the active patient registry using a dictionary (hash map).

Data Structure: Dictionary
- Key: Patient ID (string)
- Value: Patient object
- Time Complexity: O(1) for search, insert, delete (average case)

Note: This stores only ACTIVE patients currently in the hospital.
Medical history is stored separately in MedicalHistoryManagement (linked list).
"""
from save_file import save_patient_list  # Import the save function to save patient records to a file

class PatientDatabase:
    """
    Dictionary-based storage for active patients.
    
    Design Pattern: Repository Pattern
    - Encapsulates all database operations (CRUD: Create, Read, Update, Delete)
    - Single source of truth for patient data
    
    Key Concept: One-to-Many Relationship
    - One patient → Many medical history records
    - Database tracks the patient
    - MedicalHistoryManagement tracks their medical records
    """
    
    def __init__(self, filename="patients.txt"):
        """Initialize an empty patient dictionary."""
        self.patients = {}  # Key: pid (string), Value: Patient object
        self.filename = filename

    def register_patient(self, patient):
        """
        Add a new patient to the active database.
        Prevents duplicate registrations.
        
        Args:
            patient (Patient): Patient object to register
            
        Returns:
            None
            
        Raises:
            Prints error if patient ID already exists
        """
        if patient.pid in self.patients:
            return False

        self.patients[patient.pid] = patient
        self.save(self.filename)
        return True

    def search_patient(self, pid=None, name=None, phone=None):
        """
        Find a patient by ID, or fall back to name + phone.
        """
        if pid is not None:
            return self.patients.get(pid)

        if not name or not phone:
            return None

        normalized_name = name.strip().lower()
        normalized_phone = phone.strip()
        for patient in self.patients.values():
            if patient.name.lower() == normalized_name and patient.phone == normalized_phone:
                return patient

        return None

    def search_patient_by_name_and_phone(self, name, phone):
        """Find a patient using name and phone number."""
        return self.search_patient(name=name, phone=phone)

    def update_patient(self, pid, new_name=None, new_age=None, new_phone=None, new_address=None, new_symptom=None, new_severity=None):
        """
        Modify patient information.
        
        Args:
            pid (str): Patient to update
            new_name (str): New name (optional, skip if None)
            new_severity (int): New severity (optional, skip if None)
            
        Returns:
            None
            
        Note: Updates are performed in-place on the existing Patient object
        """
        # Find patient first
        patient = self.patients.get(pid)
        if patient is None:
            return False

        if new_name:
            patient.name = new_name

        if new_age is not None:
            try:
                age_int = int(new_age)
                if age_int > 0:
                    patient.age = age_int
            except Exception:
                pass

        if new_phone is not None:
            patient.phone = new_phone

        if new_address is not None:
            patient.address = new_address

        if new_symptom is not None:
            patient.symptom = new_symptom

        if new_severity is not None:
            patient.severity = new_severity

        self.save(self.filename)
        print(f"Updated: {patient}")
        return True

    def discharge_patient(self, pid):
        """
        Remove patient from active database (discharge from hospital).
        
        Args:
            pid (str): Patient to discharge
            
        Returns:
            Patient object if discharged, None if not found
            
        Note: Medical history records remain in MedicalHistoryManagement
              Only the active patient record is removed from this database
        """
        removed = self.patients.pop(pid, None)
        if removed is not None:
            self.save(self.filename)
        return removed

    def display_all_patients(self):
        """
        Print all currently registered patients.
        
        Iterates through all patients in the dictionary.
        """
        print("\nPatient Database")
        if not self.patients:
            print("No patients registered.")
            return

        # .values() returns all Patient objects
        for patient in self.patients.values():
            print(patient)

    def save(self, filename=None):
        """Save the current list of patients to a text file."""
        target_file = filename or self.filename
        patient_list = list(self.patients.values())
        save_patient_list(patient_list, target_file)