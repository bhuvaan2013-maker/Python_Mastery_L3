class Thermometer:
    def __init__(self):
        self.celcius=0
    def get_celsius(self):
        return self.celcius
    def set_celsius(self,value):
        if value == str():
            print("Please enter a number")
        else:
            self.celcius=value
    def get_fahrenheit(self):
        return self.celcius*9/5+32
    def is_freezing(self):
        if self.celcius<1:
            return True
        else:
            return False
thermometer = Thermometer()
thermometer.set_celsius(25)
print(f"Celsius: {thermometer.get_celsius()}")
print(f"Fahrenheit: {thermometer.get_fahrenheit()}")
print(f"Freezing: {thermometer.is_freezing()}")