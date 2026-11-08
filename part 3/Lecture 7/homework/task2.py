class Lamp:
    def __init__(self):
        self.brightness = 0
    def set_brightness(self, level):
        self.brightness = level #self. needs to be added in front 
    def get_brightness(self):
        return self.brightness # return needs to be added not print
    def is_bright(self):
        return self.brightness > 50
lamp = Lamp()
lamp.set_brightness(70)
print(f"Brightness: {lamp.get_brightness()}")
print(f"Bright: {lamp.is_bright()}")