doc = open("ayy mi gatito.txt",'r')
contents = doc.readlines()[1:]
# print(contents)
marks = []
for mark in contents: 
    markss = int(mark.split(" ")[4])
    marks.append(markss)
total_mark = sum(marks)
print(f"You got {total_mark} out of {(len(marks))*50} marks in ")