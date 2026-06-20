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
        # Check if patient already registered (avoid duplicates)
        if patient.pid in self.patients:
            print(f"Patient {patient.pid} already exists.")
            return

        # Add to dictionary
        self.patients[patient.pid] = patient
        print(f"Registered: {patient.pid} - {patient.name}")

    def search_patient(self, patient_id):
        """
        Find a patient by ID.
        
        Args:
            patient_id (str): Patient ID to search for
            
        Returns:
            Patient object if found, None otherwise
            
        Time Complexity: O(1) average case
        """
        # Dictionary .get() returns value or None if key not found
        return self.patients.get(patient_id)

    def update_patient(self, patient_id, new_name=None, new_severity=None):
        """
        Modify patient information.
        
        Args:
            patient_id (str): Patient to update
            new_name (str): New name (optional, skip if None)
            new_severity (int): New severity (optional, skip if None)
            
        Returns:
            None
            
        Note: Updates are performed in-place on the existing Patient object
        """
        # Find patient first
        patient = self.patients.get(patient_id)
        if patient is None:
            print("Patient not found.")
            return

        # Update only provided fields (allows partial updates)
        if new_name:
            patient.name = new_name

        if new_severity is not None:
            patient.severity = new_severity

        print(f"Updated: {patient}")

    def discharge_patient(self, patient_id):
        """
        Remove patient from active database (discharge from hospital).
        
        Args:
            patient_id (str): Patient to discharge
            
        Returns:
            Patient object if discharged, None if not found
            
        Note: Medical history records remain in MedicalHistoryManagement
              Only the active patient record is removed from this database
        """
        # Remove from dictionary and return the removed object
        removed = self.patients.pop(patient_id, None)
        if removed is None:
            print("Patient not found.")
            return None

        print(f"Discharged: {removed}")
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