import json 

# to get the json file data 
def readJSONFile(file_name="houses.json"):
    with open(file_name,"r") as file:
        data = json.load(file)
    return data 

def writeJSONFile(content,file_name="houses.json"):
    with open(file_name,"w") as file:
        file.write(content)
        
def displayHouse(House):
    print(f"Owner: {House["owner"]}")
    print("-"*15)
    print(f"Owner contact info: {House["Contact_info"]}")
    print("-"*15)
    print(f"Location city: {House["location"]["city"]}")
    print("-"*15)
    print(f"Location zip code: {House["location"]["zip_code"]}")
    print("-"*15)
    print(f"Area: {House["Area"]}")
    print("-"*15)
    print(f"Bedrooms: {House["bed_rooms"]}")
    print("-"*15)
    print(f"Bathrooms: {House["bath_rooms"]}")
    print("-"*15)
    print(f"Price: {House["Price"]}")
    print("="*20)


# data["location"]
def displayAllHouses():

    data = readJSONFile()
    for house in data:
        displayHouse(house)
        
def getHouseByOwner(name):
    data = readJSONFile()
    for i in range(len(data)):
        if data[i]["owner"] == name:
            return i 
    return -1 # owner not found 

def convert_JSON_to_string(contents):
    contents = str(contents)
    contents = contents.replace("'",'"')
    return contents 

def transfer_ownership(old_owner,new_owner):
    data = readJSONFile()
    idx = getHouseByOwner(old_owner)
    if idx == -1:
        print("Cannot transfer ownership house not found")
        return 
    else:
        data[idx]["owner"] = new_owner
        contents = convert_JSON_to_string(data)
        writeJSONFile(contents)

transfer_ownership("Sharukh","Bhuvaan")
displayAllHouses()

