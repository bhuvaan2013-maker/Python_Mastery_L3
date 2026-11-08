file_name = "./timetable/timetables.txt"
print("Welcome to the time table tracker")
while True:
    print("1.add the subject and day\n2.Read the time table\n3.search for subject\n4.exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        day = input("Enter the day (mon/tue/wed/thu/fri):")
        subject = input("Enter the subject:")
        with open(file_name,"a") as doc:
            doc.write(f"{day}-{subject}\n")
    elif choice==2:
        with open(file_name,"r") as docR:
            contents = docR.readlines()
            for line in contents:
                print(line)
    elif choice == 3:
        with open(file_name,"r") as doc:
            contents = doc.readlines()
            day = input("Enter the day: ").title()
            for row in contents:
                row_content = row.split("-")
                if row_content[0] == day:
                    print(f"Day={row_content[0]}")
                    print(f"From={row_content[1]}")
                    print(f"To={row_content[2]}")
                    print(f"Subject={row_content[3]}")
    elif choice == 4:
        print("exiting time table planner-bye")
        break 