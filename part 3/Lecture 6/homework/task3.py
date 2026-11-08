class Hero:
    def __init__(self,hero):
        if hero== None:
            self.name=""
            self.power=""
            self.health=0
        else:
            self.name=hero.name
            self.power=hero.power
            self.health=hero.health
    def display(self):
        print(self.name)
        print(self.power)
        print(self.health)
hero1 = Hero(None)
hero1.name = "Arya"
hero1.power = "Invisibility"
hero1.health = 100
hero2 = Hero(hero1)
hero2.name = "Arjun"
hero2.health = 80
hero1.display()
hero2.display()