class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks<40:
            print(f"{self.name} Failed")
        else:
            print(f"{self.name} Passed")
class Prefect(Student):
    def __init__(self,name,marks,house):
        super().__init__(name,marks)
        self.house=house
    def duty(self):
        print(f"{self.name} leads {self.house} house")
s1 = Student("Anu", 35)
s2 = Prefect("Ravi", 72, "Blue")
s1.result()
s2.result()
s2.duty()