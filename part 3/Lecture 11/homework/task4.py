class Pizza:
    def __init__(self,size):
        self.size=size
    def __eq__(self,other):
        return self.size==other.size
    def __gt__(self,other):
        return self.size>other.size
    def __lt__(self,other):
        return self.size<other.size
size1=int(input())
size2=int(input())
pizza1=Pizza(size1)
pizza2=Pizza(size2)
statement=(pizza1==pizza2)
statement2=(pizza1>pizza2)
statement3=(pizza1<pizza2)
print(f"a == b: {statement}")
print(f"a < b: {statement3}")
print(f"a > b: {statement2}")
if statement2==True:
    print(f"Largest pizza: {size1} inches")
elif statement3==True:
    print(f"Largest pizza: {size2} inches")
else:
    print("Both pizzas are the same size")    