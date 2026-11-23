class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def details(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
class VehicleCar(Vehicle):
    def __init__(self,brand,year,doors):
        super().__init__(brand,year)
        self.doors=doors
        self.type="car"
    def full_details(self):
        self.details()
        print(f"Type: {self.type}")
        print(f"Number of doors: {self.doors}")
class Bike(Vehicle):
    def __init__(self,brand,year,style):
        super().__init__(brand,year)
        self.style=style
        self.type="bike"
    def full_details(self):
        self.details()
        print(f"Type: {self.type}")
        print(f"Style: {self.style}")
        

type=input()
brand=input()
year=int(input())
feature=input()

if type=="car":
    car=VehicleCar(brand,year,feature)
    car.full_details()
elif type=="bike":
    bike=Bike(brand,year,feature)
    bike.full_details()