class Laptop:
    def __init__(self,my_laptop):
        if my_laptop== None:
            self.brand="Lenovo"
            self.processor="XC-9090"
            self.screen_size="16 inch"
            self.operating_system="Linux"
            self.battery="47%"
            self.sound="39"
        else:
            self.brand=my_laptop.brand
            self.processor=my_laptop.processor
            self.screen_size=my_laptop.screen_size
            self.operating_system=my_laptop.operating_system
            self.battery=my_laptop.battery
            self.sound=my_laptop.sound
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
my_lap=Laptop(None)
my_lap.brand="Lenovo"
my_lap.processor="XC-9090"
my_lap.screen_size="16 inch"
my_lap.operating_system="Linux"
my_lap.battery="47%"
my_lap.sound="39"
copy=Laptop(my_lap)
copy.display()