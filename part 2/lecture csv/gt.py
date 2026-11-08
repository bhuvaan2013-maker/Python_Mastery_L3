import csv 
while True:
    file_name=input("Enter the file name you want to use:")
    format=input("What mode would you like(dictionary or normal and exit to leave):")
    if format.lower()=="dictionary":
        with open(file_name,"r") as file:
            contents = csv.DictReader(file)
            columns=input("What column would you like (0 if no columns are needed):")
            for row in contents:
                print(f"{columns.title()}:{row[columns.lower()]}")
    elif format.lower()=="normal":
        with open(file_name,"r") as file:
            reader = csv.reader(file)
            readers=csv.Dictreader(file)
            content=list(reader)
            contents=content[1:]
            for row in contents:
                print("5")
    elif format.lower()=="exit":
        print("It was nice to see you-bye")
        break
    else:
        print("INVALID")