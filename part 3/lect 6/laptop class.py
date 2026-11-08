class Laptop:
    def __init__(self):
        self.brand="Lenovo"
        self.processor="XC-9090"
        self.screen_size="15 inch"
        self.operating_system="Windows"
        self.battery="67%"
        self.sound="48"
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
my_laptop=Laptop()
my_laptop.show_battery()
my_laptop.charging()
my_laptop.typing("Profesora manana manananananananananana")
my_laptop.sound_percentage()
my_laptop.play_video()