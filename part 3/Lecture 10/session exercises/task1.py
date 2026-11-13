class VehicleNotAvailableError(Exception):
    pass
class RentalPeriodExceededError(Exception):
    pass
class Vehicle:
    def __init__(self,brand,model,rental_price):
        self.brand=brand
        self.model=model
        self.rental_price=rental_price
    def set_brand(self,brand):
        if isinstance(brand,int,float):
            raise ValueError("Brand needs to be a string")
        else:
            self.brand=brand
    def set_model(self,model):
        if isinstance(model,int,float):
            raise ValueError("Model needs to be a string")
        else:
            self.model=model
    def set_model_price(self,model_price):
        if isinstance(model_price,int,float):
            self.model_price=model_price
        else:
            raise ValueError("Brand needs to be a string")
    def get_brand(self):
        return self.brand
    def get_model(self):
        return self.model
    def get_model_price(self):
        return self.model_price
    def display_vehicle(self):
        self.get_brand
        self.get_model
        self.get_model_price
class RentalVehicle(Vehicle):
    def __init__(self,vehicle_number,brand,model,rental_price):
        super().__init__(brand,model,rental_price)
        self.vehicle_number=vehicle_number
        self.available=True
    def rent_vehicle(self):
        if self.available==True:
            print("Vehicle is available and has been rented by you")
            self.available=False
        else:
            raise VehicleNotAvailableError("Vehicle is not available")
class CustomerRental(RentalVehicle):
    def __init__(self,vehicle_number,brand,model,rental_price,customer_name):
        super().__init__(vehicle_number,brand,model,rental_price)
        self.customer_name=customer_name
    def set_rental_days(self,rental_days):
        if rental_days>30:
            raise RentalPeriodExceededError("The rental period is too long")
        else:
            self.rental_days=rental_days
    def get_rental_days(self):
        return self.rental_days
    def calculate_bill(self):
        return self.rental_days*self.rental_price
    def display_details(self):
        print(self.display_details())
        print(self.customer_name)
    def return_vehicle(self):
        if self.available==True:
            raise VehicleNotAvailableError("Vehicle is already availiable")
        else:
            print("Vehicle returned")
            self.available==True
tung=CustomerRental(1,"Toyota","Circus",43,"Toby")
tung.rent_vehicle()
tung.set_rental_days(43)
tung.calculate_bill()
tung.return_vehicle()