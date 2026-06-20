"""
Node Class for Linked List
Represents a single node in a doubly-linked list structure.

Structure:
[prev] <---> [NODE] <---> [next]
             [value/patient data]
"""


class node:
    """
    A doubly-linked list node.
    
    Attributes:
        value: The data stored in this node (Patient object)
        patient: Alias for value (for compatibility)
        next: Pointer to the next node (or None if at end)
        prev: Pointer to the previous node (or None if at start)
    """
    
    def __init__(self, value):
        """
        Create a new node containing patient data.
        
        Args:
            value (Patient): Patient object to store in this node
        """
        self.value = value      # Store the patient data
        self.patient = value    # Alias for compatibility
        self.next = None        # Initially no next node
        self.prev = None        # Initially no previous node

