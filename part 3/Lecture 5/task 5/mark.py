
from student import Student

name1 = input()
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
s1 = Student(name1, mark1, mark2, mark3)

name2 = input()
mark4 = int(input())
mark5 = int(input())
mark6 = int(input())
s2 = Student(name2, mark4, mark5, mark6)

print(s1.name)
print(s1.total())
print(format(s1.average(), ".2f"))

print(s2.name)
print(s2.total())
print(format(s2.average(), ".2f"))
