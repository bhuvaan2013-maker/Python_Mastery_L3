import random
with open("breakfast.txt","r") as response:
    brekkie=response.readlines()
with open("lunch.txt","r") as response:
    lunch=response.readlines()
with open("dinner.txt","r") as response:
    dinner=response.readlines()
menu=f"""
        Menu Maker:
        Breakfast: {random.choice(brekkie)}
        Lunch: {random.choice(lunch)}
        Dinner: {random.choice(dinner)}"""
print(menu)
