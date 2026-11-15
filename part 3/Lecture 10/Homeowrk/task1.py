class Athelete:
    def __init__(self,name):
        self.name=name
class Runner(Athelete):
    def __init__(self,name,speed):
        super().__init__(name)
        self.speed=speed
class MarathonRunner(Runner):
    def __init__(self,name,speed,distance):
        super().__init__(name,speed)
        self.distance=distance
    def race_time(self):
        return self.distance/self.speed
name=input()
speed=int(input())
distance=int(input())
tung=MarathonRunner(name,speed,distance)
print(f"{tung.name} runs {tung.distance} in {tung.speed}km/h and needs {tung.race_time()} hours")