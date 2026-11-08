class Player:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def take_damage(self,amount):
        if amount<0:
            print("Invalid damage given")
        elif (self.health-amount)<1:
            self.health=0
        else:
            self.health=self.health-amount
    def is_alive(self):
        if self.health==0:
            return False
        else:
            return True
    def show_status(self):
        print(f"{self.name} HP:{self.health}")
class Wizard(Player):
    def __init__(self,name,health,mana):
        super().__init__(name,health)
        self.mana=mana
    def cast_spell(self,cost):
        if cost<=0:
            print("Invalid cost")
        elif cost>self.mana:
            print(f"{self.name} does not have enough mana")
        else:
            print(f"{self.name} casts a spell")
            self.mana=self.mana-cost
            print(f"Mana left: {self.mana}")
merlin = Wizard("Merlin", 50, 30)
merlin.cast_spell(20)
merlin.take_damage(15)
merlin.show_status()
merlin.cast_spell(15)
merlin.take_damage(60)
merlin.show_status()
print(merlin.is_alive())