import json


def read_visit():
    try:
        with open("house_visit.json", "r") as file:
            data = json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        data = []
    return data


def visit_time(time):
    time_list = []
    data = read_visit()
    for i in range(len(data)):
        if data[i]["time"] == time:
            time_list.append(i)
    return time_list


def find_visitor(visitor_name):
    visitor_list = []
    data = read_visit()
    for i in range(len(data)):
        if data[i]["visitor_name"] == visitor_name:
            visitor_list.append(i)
    return visitor_list


def find_owner(owner_name):
    owner_list = []
    data = read_visit()
    for i in range(len(data)):
        if data[i]["owner_name"] == owner_name:
            owner_list.append(i)
    return owner_list


def readJSONFile(file_name="houses.json"):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        data = []
    return data


def writeJSONFile(content, file_name="houses.json"):
    with open(file_name, "w") as file:
        json.dump(content, file, indent=4)


def displayHouse(House):
    print(f"Owner: {House['owner']}")
    print("-" * 15)
    print(f"Owner contact info: {House['Contact_info']}")
    print("-" * 15)
    print(f"Location city: {House['location']['city']}")
    print("-" * 15)
    print(f"Location zip code: {House['location']['zip_code']}")
    print("-" * 15)
    print(f"Area: {House['Area']}")
    print("-" * 15)
    print(f"Bedrooms: {House['bed_rooms']}")
    print("-" * 15)
    print(f"Bathrooms: {House['bath_rooms']}")
    print("-" * 15)
    print(f"Price: {House['Price']}")
    print("=" * 20)


def displayAllHouses():
    data = readJSONFile()
    for house in data:
        displayHouse(house)


def getHouseByOwner(name):
    data = readJSONFile()
    for i in range(len(data)):
        if data[i]["owner"] == name:
            return i
    return -1


def transfer_ownership(old_owner, new_owner):
    data = readJSONFile()
    idx = getHouseByOwner(old_owner)

    if idx == -1:
        print("Cannot transfer ownership. House not found")
        return

    data[idx]["owner"] = new_owner
    writeJSONFile(data)
    print("Ownership transferred successfully")


def buy_house(old_owner, new_owner):
    card_number = input("Enter the card number: ")
    print("Payment Success")
    transfer_ownership(old_owner, new_owner)
    print("Property Purchase Success")


def schedule_visit(owner_name, visitor_name, num_visitors, date, time):
    data = readJSONFile()
    idx = getHouseByOwner(owner_name)

    if idx == -1:
        print("Cannot schedule a visit. House not found")
        return

    visit_data = readJSONFile("house_visit.json")

    # prevent duplicate visitor for same owner/date/time
    for visit in visit_data:
        if (
            visit["owner_name"] == owner_name
            and visit["visitor_name"] == visitor_name
            and visit["date"] == date
            and visit["time"] == time
        ):
            print("This visit is already scheduled")
            return

    # prevent same owner being booked at same date/time
    for visit in visit_data:
        if (
            visit["owner_name"] == owner_name
            and visit["date"] == date
            and visit["time"] == time
        ):
            print("This time slot is already booked")
            return

    visiting_info = {
        "owner_name": owner_name,
        "visitor_name": visitor_name,
        "number_of_visitors": num_visitors,
        "date": date,
        "time": time,
        "location": data[idx]["location"],
        "is_visited": False
    }

    visit_data.append(visiting_info)
    writeJSONFile(visit_data, "house_visit.json")

    print(f"Successfully scheduled the visit on {date} at {time}")


schedule_visit("Hemanth", "Sharukh", 2, "02/05/2026", "10:00")