
class Television:
    def __init__(self, brand, model, size):
        self.brand = brand
        self.model = model
        self.size = size
    def switch_on(self):
        print("TV power on")
    def switch_off(self):
        print("TV shutdown")
    def show_details(self):
        print(self.brand)
        print(self.model)
        print(self.size)

    
        