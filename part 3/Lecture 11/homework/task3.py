class Time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def __add__(self,other):
        self.total1=self.minutes + other.minutes
        hours=self.total1//60
        self.total_hours=self.hours + other.hours + hours
        self.total=self.total1%60
        return Time(self.total_hours,self.total)
    def __str__(self):
        return f"{self.hours} hours {self.minutes} minutes"
num=input()
num1=input()
list2=num.split()
list1=num.split()
fred=Time(int(list2[0]),int(list2[1]))
fred1=Time(int(list1[0]),int(list1[1]))
print(fred+fred1)