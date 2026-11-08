import csv 
with open("67.csv","w",newline="") as file:
    writer = csv.writer(file)
    # add the columns 
    writer.writerow(["Roll No.","Name","Marks","Grade"])
    students = [
        ["1","Hemanth","100","8"],
        ["2","Bhuvan","100","8"]
    ]
    # adding multiple rows of data 
    writer.writerows(students)
    print("done")