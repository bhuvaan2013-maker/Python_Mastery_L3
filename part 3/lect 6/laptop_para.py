class Laptop:
    def __init__(self,brand,processor,screen_size,operating_system,battery,sound):
        self.brand=brand
        self.processor=processor
        self.screen_size=screen_size
        self.operating_system=operating_system
        self.battery=battery
        self.sound=sound
        self.video="a"
    def typing(self, sentence):
        print(f"You typed: {sentence}")
        print(f"Laptop printed: {sentence}")
    def show_battery(self):
        print(self.battery)
    def charging(self):
        print(f"Charging from {self.battery}")
    def sound_percentage(self):
        print(f"The sound level is: {self.sound}")
    def play_video(self):
        print(f"Video is being played: {(self.video)*997}")
    def display(self):
        print(self.brand)
        print(self.processor)
        print(self.screen_size)
        print(self.operating_system)
        print(self.battery)
        print(self.sound)
my_laptop=Laptop("lenovo","XC-9090","16 inch","Linux","99%","64")
my_laptop.show_battery()
my_laptop.charging()
my_laptop.typing("Profesora manana manananananananananana")
my_laptop.sound_percentage()
my_laptop.play_video()
my_laptop.display()