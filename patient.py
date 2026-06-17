class patient:
    def __init__(self, name, ID, sympton):
        self.name = name
        self.ID = ID
        self.sympton = sympton
    def __str__(self):
        return f"{self.name} - {self.ID} - sympton:{self.sympton}"