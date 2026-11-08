class Pizza:
    def __init__(self,size,crust,topping):
        self.size=size
        self.crust=crust
        self.topping=topping
    def describe(self):
        print(f"{self.size} pizza with {self.crust} crust and {self.topping}")
    def bake(self,time):
        print(f"Baking the {self.topping} pizza for {time} minutes........")
pizza1 = Pizza("Large", "thin", "mushrooms")
pizza2 = Pizza("Small", "cheese-burst", "paneer")
pizza1.describe()
pizza1.bake(12)
pizza2.describe()
pizza2.bake(10)