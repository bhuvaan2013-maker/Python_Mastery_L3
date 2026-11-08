
class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def total(self):
        return self.mark1 + self.mark2 + self.mark3

    def average(self):
        return self.total() / 3
