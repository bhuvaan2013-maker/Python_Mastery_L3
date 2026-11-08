import csv 
import math 
file_name = "./lecture csv/student.csv"
with open(file_name,"w",newline="") as file:
    writer = csv.writer(file)

    # add the column names 
    column_names = ["Roll number","Name","marks"]

    writer.writerow(column_names)
    class1 = [] 
    count = int(input("Enter number of students you want to add: "))
    total_marks = 0
    min_marks = math.inf
    max_marks = - math.inf

    for i in range(count): # 0 1 2 3 4 
        student_data = []
        student_data.append(i+1) # serial Number 
        print(f"Student {i+1} Details: ")
        name = input("Enter the student Name: ")
        student_data.append(name) # item name 
        marks= int(input("Enter the marks: "))
        student_data.append(marks)
        total_marks = total_marks + marks 
        print("="*101)
        min_marks = min(min_marks,marks)
        max_marks = max(max_marks,marks)

        # adding item to shopping list 
        class1.append(student_data)

    writer.writerows(class1)
    print("Students are added succesfully")
    print("="*101)
    print("Average marks=" ,total_marks/count)
    print("Min marks = ",min_marks)
    print("Max Marks = ",max_marks)
    print("="*101)