class Pet:  
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name,age) #need to link the variables together
        self.breed = breed
    def bark(self):
        print(f"{self.name} says Woof")
bruno = Dog("Bruno", 3, "Labrador")
bruno.eat()
bruno.bark()
print(bruno.age)