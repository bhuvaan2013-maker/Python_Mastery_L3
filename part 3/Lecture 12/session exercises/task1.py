class Product:
    def __init__(self,id,name,price,quantity):
        self.id=id
        self.name=name
        self.price=price
        self.quantity=quantity
class ShoppingCart(Product):
    def __init__(self,*products,name1:str="ShoppingCart"):
        self.cart=[product for product in range(*products)]
        self.namee=name1
    def add_product(self,product):
        self.cart.append(product)
    def __add__(self,other):
        self.newcart=self.cart + other.cart
        return self.newcart
    def __sub__(self,id):
        for product in self.cart:
            if super().id==id:
                self.cart.remove(product)
            else:
                pass
    def total_value(self):
        for product in self.cart:
            value=super().price*super().quality
            total_value=value+total_value
    def __eq__(self,other):
        return self.total_value()==other.total_value()
    def __gt__(self,other):
        if self.total_value()>other.total_value():
            print("Cart 1 is more expensive")
        elif self.total_value()<other.total_value():
            print("Cart 2 is more expensive")
        else:
            print("The same price for both")
    def __len__(self):
        return len(self.cart)
    def __str__(self,other):
        print(f"=========={self.namee}==========")
        for i in range (self.cart): 
            print(f"{super().name} - ₹{super().price} x {super().quantity}")
        print(f"Total: {self.total_value()}")
        print(f"========={other.namee}==========")
        for i in range (other.cart): 
            print(f"{super().name} - ₹{super().price} x {super().quantity}")
        print(f"Total: {other.total_value()}")
Banana=Product(1,"Banana",12,4)
Apple=Product(2,"Apple",12,7)
Watermelon=Product(3,"Watermelon",12,1)
Tissue=Product(5,"Tissue",12,2)
Table=Product(6,"Table",120,1)
cart1=ShoppingCart(Banana,Apple,Watermelon)
cart2=ShoppingCart(Banana,Apple,Table)
print(cart1+cart2)
        