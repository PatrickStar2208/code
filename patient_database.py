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
    
    def __init__(self):
        """Initialize an empty patient dictionary."""
        self.patients = {}  # Key: pid (string), Value: Patient object

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
        return True

    def search_patient(self, pid):
        """
        Find a patient by ID.
        
        Args:
            pid (str): Patient ID to search for
            
        Returns:
            Patient object if found, None otherwise
            
        Time Complexity: O(1) average case
        """
        # Dictionary .get() returns value or None if key not found
        return self.patients.get(pid)

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
        # Remove from dictionary and return the removed object
        return self.patients.pop(pid, None)

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