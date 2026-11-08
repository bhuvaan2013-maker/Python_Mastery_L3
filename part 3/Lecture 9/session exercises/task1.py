import time
import random
class SecuritySystem:
    def __init__(self,system_name,price):
        self.price=price
        self.system_name=system_name
        raw=time.gmtime()
        self.setup_date=time.strftime("%d/%m/%Y",raw)
    def activate_alarm(self):
        print(f"Alarm has been activated at: {time.strftime("%I:%M:%S",time.gmtime())} on {time.strftime("%d:%m:%Y",time.gmtime())}")
    def check_door_status(self):
        status=random.randint(0,1)
        if status==0:
            print("Door is open")
        elif status==1:
            print("Door is closed")
    def motion_detected(self):
        print("Motion has been detected")
class HomeEntertainment:
    def __init__(self,system_name,price):
        self.price=price
        self.system_name=system_name
        raw=time.gmtime()
        self.setup_date=time.strftime("%d/%m/%Y",raw)
    def play_music(self,song):
        print(f"The song {song} is playing right now")
    def adjust_volume(self,level):
        print(f"The volume adjusted to: {level}")
    def connect_bluetooth(self,device):
        print(f"Bluetooth has been connected to {device}")
class SmartHome(HomeEntertainment,SecuritySystem):
    def __init__(self,model,price):
        SecuritySystem.__init__(self,model,price)
        HomeEntertainment.__init__(self,model,price)
    def control_lights(self,status):
        if status.lower()=="on":
            print("Lights are on")
        if status.lower()=="off":
            print("Lights are off")
    def check_temperature(self):
        temp=random.randint(1,40)
        print(f"The current room temperature is: {temp} degrees celcius")
alexa=SmartHome("Google",1400)
alexa.check_door_status()
alexa.activate_alarm()
alexa.play_music("Believer")
alexa.connect_bluetooth("Google")
alexa.control_lights("on")
alexa.check_temperature()
print(alexa.system_name)
print(alexa.price)