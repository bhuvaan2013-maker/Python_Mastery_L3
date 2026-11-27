class Character:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def describe(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
class Warrior(Character):
    def __init__(self,name,health,strength):
        super().__init__(name,health)
        self.strength=strength
    def describe(self):
        super().describe()
        print(f"Strength: {self.strength}")
class Mage(Character):
    def __init__(self,name,health,mana):
        super().__init__(name,health)
        self.mana=mana
    def describe(self):
        super().describe()
        print(f"Mana: {self.mana}")
class Paladin(Warrior):
    def __init__(self,name,health,strength,shield):
        super().__init__(name,health,strength)
        self.shield=shield
    def describe(self):
        super().describe()
        print(f"Shield: {self.shield}")
name=input()
health=int(input())
strength=int(input())
shield=int(input())
hero=Paladin(name,health,strength,shield)
hero.describe()
mro_chain=" -> ".join(cls.__name__ for cls in Paladin.__mro__[:3])
print(mro_chain)
