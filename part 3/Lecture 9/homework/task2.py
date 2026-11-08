class Screen:
    def __init__(self, size):
        self.size = size
    def show(self):
        print(f"Showing on {self.size} inch screen")
class Controller:
    def __init__(self, buttons):
        self.buttons = buttons
    def press(self):
        print(f"Pressing one of {self.buttons} buttons")
class GameConsole(Screen, Controller):
    def __init__(self, size, buttons):
        Screen.__init__(self, size)
        Controller.__init__(self, buttons)
    def start_game(self):
        self.show()
        self.press()
        print("Game started")
console = GameConsole(32, 12)
console.start_game()
print(console.size + console.buttons)