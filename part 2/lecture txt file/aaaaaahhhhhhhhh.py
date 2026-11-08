doc = open("ayy mi gatito.txt",'r')
contents = doc.readlines()[1:]
# print(contents)
spends = []
for record in contents: 
    money = int(record.split(" ")[4])
    spends.append(money)

total_spent = sum(spends)
print(f"You spent {total_spent} Pounds this month")

doc = open("ayy mi gatito.txt","r")
contents = doc.readlines()
spends = map(int,contents)
print(f"Total: {sum(spends)} Pounds")
doc = open("data.txt","r")
content = doc.readline()

num = map(int,content.split(" "))


print(sum(num))

a = [1,2,3,4,5]

print(sum(a))