import csv 
import math 
file_name = "studentmark.csv"
print("Welcome to mark calculator")
while True:
    print("You have 3 options:")
    print("1)Enter student details")
    print("2)See Minimum and Maximum marks")
    print("3)See student details")
    print("4)Quit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        with open(file_name,"w",newline="") as file:
            writer = csv.writer(file)
            column_names = ["Roll number","Name","marks"]
            writer.writerow(column_names)
            class1 = [] 
            count = int(input("Enter number of students you want to add: "))
            total_marks = 0
            min_marks = math.inf
            max_marks = - math.inf
            for f in range(count): 
                student_data = []
                student_data.append(f+1)  
                print(f"Student {f+1} Details:")
                name = input("Enter the student Name:")
                student_data.append(name)
                marks= int(input("Enter the marks:"))
                student_data.append(marks)
                class1.append(student_data)
                writer.writerows(class1)
                print("Students are added succesfully")
                print("="*101)
                min_marks = min(min_marks,marks)
                max_marks = max(max_marks,marks)
    elif choice==2:
        print("="*101)
        print("Min marks = ",min_marks)
        print("Max Marks = ",max_marks)
        print("="*101)
    elif choice==3:
        contents=[]
        with open("studentmark.csv","r") as file:
            columns = ["Roll No.","Name","Marks"]
            reader = csv.DictReader(file,fieldnames=columns)
            for row in reader:
                contents.append(row)
        print(contents)
    elif choice==4:
        print("Thank you for using this-bye")
        break
    else:
        print("Wrong input")