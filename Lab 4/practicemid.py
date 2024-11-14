class Student:
    
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def equality(self, other):
        return self.name == other.name

    def lessthan(self, other):
        pass

    def greaterthan(self, other):
        return self.name >= other.name
