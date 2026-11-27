class Instrument:
    def play(self):
        print("Playing an instrument")
class Guitar(Instrument):
    def play(self):
        print("Strumming the guitar")
class Bike(Instrument):
    def play(self):
        print("Beating the drum")
class Band:
    def introduce(*members):
        for member in members:
            print(f"Member: {member}")
intrument=input()
members=input()
member=members.split(",")
if intrument.title()=="Guitar":
    player=Guitar()
    player.play()
elif intrument.title()=="Drum":
    player=Guitar()
    player.play()
meow=Band()
meow.introduce(*member)