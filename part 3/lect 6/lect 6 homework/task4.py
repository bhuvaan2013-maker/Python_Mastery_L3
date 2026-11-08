class Robot:
    def __init__(self, name, battery):
        self.name = name #need to add self. infront of name
        self.battery = battery
    def greet(self): #need to call upon self
        print(f"Hello, I am {self.name}")
    def show_battery(self):
        print(f"Battery: {self.battery}%")
r1 = Robot("Tinku",80) # needs two variables one for name and one for battery
r1.greet()
r1.show_battery()