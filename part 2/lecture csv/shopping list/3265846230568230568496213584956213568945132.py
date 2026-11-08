
import csv 
file_name = "shoppingList.csv"
with open(file_name,"w",newline="") as file:
    writer = csv.writer(file)

    # add the column names 
    column_names = ["Serial No.","Item Name","Quantity"]

    writer.writerow(column_names)
    shoppingList = [] 
    count = int(input("Enter number of items you want to add: "))

    for i in range(count): # 0 1 2 3 4 
        Item = []
        Item.append(i+1) # serial Number 
        name = input("Enter the Item Name: ")
        Item.append(name) # item name 
        quantity = int(input("Enter the Quantity: "))
        Item.append(quantity)

        # adding item to shopping list 
        shoppingList.append(Item)

    writer.writerows(shoppingList)
    print("Items are added succesfully")