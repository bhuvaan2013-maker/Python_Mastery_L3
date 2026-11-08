class Notebook:
    def __init__(self,owner):
        self.owner=owner
    def write_note(self,text):
        print(f"{self.owner} wrote: {text}")
class Calculator:
    def __init__(self,brand):
        self.brand=brand
    def add(self,a,b):
        print(f"{self.brand} calculator says:{a}+{b}={a+b}")
class Smartablet(Notebook,Calculator):
    def __init__(self,owner,brand):
        Notebook.__init__(self,owner)
        Calculator.__init__(self,brand)
owner1=input()
brand1=input()
text1=input()
a=int(input())
b=int(input())
tablet=Smartablet(owner1,brand1)
tablet.write_note(text1)
tablet.add(a,b)