"""
Medical History Management Module
Manages medical records using a doubly-linked list data structure.

Data Structure: Doubly-Linked List
- Each node contains a Patient object (represents a medical record)
- Each node has: value (Patient), next (pointer to next), prev (pointer to previous)
- Can traverse forward or backward
- Time Complexity: O(n) for search, O(1) for add/delete at ends

Key Concept:
- Medical records are GLOBAL (not tied to one patient)
- Multiple records can exist for the same patient
- Records are ordered by insertion time (FIFO: First In, First Out)
- This is a "log" of all medical activities in the hospital
"""

from node import node


class MedicalHistoryManagement:
    """
    Doubly-linked list for storing all medical records.
    
    Think of it as a hospital's medical log:
    - Every medical action is recorded
    - Records are timestamped and ordered chronologically
    - You can add new records or remove the most recent one
    """
    
    def __init__(self):
        """Initialize empty medical history."""
        self.head = None  # First record in the list
        self.tail = None  # Last record in the list
        self.size = 0     # Number of records

    def is_empty(self):
        """Check if medical history is empty."""
        return self.size == 0

    def addrecord(self, newrecord):
        """
        Add a new medical record to the end of the list.
        
        Args:
            newrecord (Patient): Patient object to add as a record
            
        Process:
        1. Create new node wrapping the patient data
        2. If list is empty: make it both head and tail
        3. If list has items: attach to tail and update pointers
        4. Increment size counter
        
        Time Complexity: O(1) - constant time
        """
        newPatient = node(newrecord)
        
        if self.size == 0:
            # Empty list: first node is both head and tail
            self.head = newPatient
            self.tail = newPatient
        else:
            # Non-empty list: append to tail
            self.tail.next = newPatient    # Old tail points to new node
            newPatient.prev = self.tail     # New node points back to old tail
            self.tail = newPatient          # New node becomes new tail
        
        self.size += 1  # Increment counter

    def updateRecord(self, patient_id, new_symptom):
        """
        Update the most recent medical record for a specific patient.
        Traverses the list and remembers the last matching node, then updates it.
        
        Args:
            patient_id (str): Patient ID to search for
            new_symptom (str): New symptom value to set
        Returns:
            True if updated, False if no matching record found
        """
        currentPatient = self.head
        last_match = None
        # Find the last matching record (most recent occurrence)
        while currentPatient is not None:
            if currentPatient.value.pid == patient_id:
                last_match = currentPatient
            currentPatient = currentPatient.next

        if last_match is not None:
            last_match.value.symptom = new_symptom
            return True
        return False

    def deleteRecord(self):
        """
        Delete the most recent medical record (remove tail).
        
        Returns:
            True if successful, None if list is empty
            
        Process:
        1. If empty: return None
        2. If one item: clear head and tail
        3. If multiple items: remove tail and update pointers
        
        Time Complexity: O(1) - constant time
        """
        if self.size == 0:
            # Can't delete from empty list
            return None
        
        if self.size == 1:
            # Last item in list
            self.head = None
            self.tail = None
        else:
            # Multiple items: remove tail
            nearTail = self.tail.prev  # Get the node before tail
            self.tail = nearTail        # Make it the new tail
            nearTail.next = None        # Break the link to old tail
        
        self.size -= 1  # Decrement counter
        return True

    def getHistory(self, patient):
        """
        Search for all records of a specific patient.
        
        Args:
            patient (str): Patient ID to search for
            
        Returns:
            Patient object if found, None otherwise
            
        Process:
        1. Start at head of list
        2. Traverse forward until patient found or end reached
        3. Check both pid and ID attributes (for compatibility)
        
        Time Complexity: O(n) - must check each node in worst case
        """
        currentPatient = self.head
        
        # Traverse the linked list
        while currentPatient is not None:
            # Check if this record belongs to the patient
            if currentPatient.value.pid == patient:
                print(currentPatient.value)
                return currentPatient.value
            currentPatient = currentPatient.next  # Move to next node
        
        # Not found
        print("Không tìm thấy lịch sử cho bệnh nhân này.")  # Vietnamese message
        return None

    def display(self):
        """
        Print all medical records in order.
        Traverses entire linked list from head to tail.
        
        Time Complexity: O(n) - must visit each node
        """
        currentPatient = self.head
        
        while currentPatient is not None:
            print(currentPatient.value)  # Print the patient record
            currentPatient = currentPatient.next  # Move to next node
            

