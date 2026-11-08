from converter1 import Converter
km = float(input("Enter distance in kilometres: "))
kg = float(input("Enter weight in kilograms: "))
miles = Converter.km_to_miles(km)
pounds = Converter.kg_to_pounds(kg)
print("Distance in miles:",format(miles,".2f"))
print("Weight in pounds:",format(pounds,".2f"))


