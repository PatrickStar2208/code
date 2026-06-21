"""
Node class for a linked list.
Each node stores a value and points to the next and previous nodes.
"""


class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

