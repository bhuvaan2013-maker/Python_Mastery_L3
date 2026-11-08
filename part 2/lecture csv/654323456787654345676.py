import csv 

columns = ["ItemID","Name","Quantity","Availability"]
def readfile():
    contents = []
    with open("warehouse.csv","r") as file:
        reader = csv.DictReader(file,fieldnames=columns)
        for row in reader:
            contents.append(row)
    return contents 

contents = readfile()

def writefile(contents):
    with open("warehouse.csv","w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=columns)
        # writer.writeheader()
        writer.writerows(contents)

def addItem(ItemID,Name,Quantity):
    if Quantity > 0 :
        Availability = "Available"
    else:
        Availability = "Out of Stock"
    
    contents.append({columns[0]:ItemID,columns[1]:Name,columns[2]:Quantity,columns[3]:Availability})
    writefile(contents)

def getItemIndex(ItemID):
    for i in range(len(contents)):
        if contents[i]["ItemID"] == str(ItemID):
            return i 
    return None 

def updateStock(ItemID,Quantity):
    index = getItemIndex(ItemID)
    if index == None:
        print("Cannot update the quantity try adding the item with id ",ItemID)
    else:
        item = contents[index]
        if Quantity > 0:
            item["Availability"] = "Available"
        else:
            item["Availability"] = "Out of stock"
        
        item["Quantity"] = int(item["Quantity"] )+ Quantity
        contents[index] = item 
        writefile(contents)
def displayItem(ItemID):
    index = getItemIndex(ItemID)
    if index == None:
        print("Item is not found")
    else:
        item = contents[index]
        print("######### ITEM DETAILS ########")
        print(f"ItemID: {item[columns[0]]}\tName: {item[columns[1]]}")
        print(f"Quantity: {item[columns[2]]}\tAvailability: {item[columns[3]]}")
        print("#"*20)

def display():
    print("######### ITEM DETAILS ########")
    for item in contents[1:]: 
        print(f"ItemID: {item[columns[0]]}\tName: {item[columns[1]]}")
        print(f"Quantity: {item[columns[2]]}\tAvailability: {item[columns[3]]}")
        print("-"*20)
    print("#"*20)


def checkAvailability(ItemID):
    index = getItemIndex(ItemID)
    if index == None:
        print("Item not found")
    else:
        print(f"ItemID:{contents[index][columns[0]]}\tAvailability: {contents[index][columns[3]]}")

def remove(ItemID,Quantity):
    index = getItemIndex(ItemID)
    if index == None:
        print("Item not found")
    else:
        item = contents[index]
        item_quantity = int(item["Quantity"])
        if Quantity <= item_quantity:
            new_quantity = item_quantity - Quantity
            if new_quantity == 0:
                item["Availability"] = "Out of Stock"
            item["Quantity"] = new_quantity
            contents[index] = item 
            writefile(contents)
        elif item_quantity == 0:
            print("Item out of Stock")
        else:
            print(f"choose quantity <= {item_quantity}")

        
print("Welcome to the inventory tracker")
while True:
    print("Here are the options:")
    print("1)Add an item to the inventory")
    print("2)Add quantity to an existing item")
    print("3)Remove stock from inventory")
    print("4)View items")
    print("5)Search for items")
    print("6)Check availability of an item")
    print("7)Leave")
    choice=input("What would you like to do:")
    if choice==1:
        ItemID=int(input("Enter the ID of the item you want to add:"))
        Name=input("Enter the name of the new product:")
        Quantity=int(input("Enter the quantity of the item you wish to add"))
        addItem(ItemID,Name,Quantity)
    if choice==2:
        ItemID=int(input("Enter the ID of the item you want to add to:"))
        Quantity=67