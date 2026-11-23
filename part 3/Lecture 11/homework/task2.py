class Character:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def describe(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
class 