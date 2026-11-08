class Cooker:
    def __init__(self,robot_name,price):
        self.robot_name=robot_name
        self.price=price
    def cook_dish(self,dish):
        print(f"Cooking {dish}")
class Cleaner:
    def __init__(self,robot_name,price):
        self.robot_name=robot_name
        self.price=price
    def clean_room(self,room):
        print(f"Cleaning the {room}")
class HouseRobot(Cooker,Cleaner):
    def __init__(self,robot_name,price):
        Cooker.__init__(self,robot_name,price)
        Cleaner.__init__(self,robot_name,price)
robot_name=input()
price=int(input())
dish=input()
room=input()
robo=HouseRobot(robot_name,price)
print(f"{robo.robot_name} costs {robo.price}")
robo.cook_dish(dish)
robo.clean_room(room)