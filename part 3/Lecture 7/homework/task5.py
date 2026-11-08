class Theatre:
    def __init__(self,seat):
        self.total_seat=seat
        self.price=0
        self.booked=0
    def set_ticket_price(self,price):
        if price<0 or price == str():
            print("Invalid price. Update rejected.")
        else:
            self.price=price
    def get_available_seats(self):
        return self.total_seat-self.booked
    def book_seats(self,count):
        if count<1:
            print("Invalid seat count.")
        elif count>self.total_seat-self.booked:
            print("Not enough seats available.")
        else:
            self.booked=count
    def cancel_seats(self,count):
        if count<1 or count>self.booked:
            print("Invalid seat count.")
        else:
            self.booked=self.booked-count
    def total_revenue(self):
        return self.booked*self.price
theatre = Theatre(20)
theatre.set_ticket_price(-50)
theatre.set_ticket_price(150)
theatre.book_seats(0)
theatre.book_seats(20)
print(theatre.get_available_seats())
theatre.book_seats(1)
theatre.cancel_seats(25)
theatre.cancel_seats(8)
print(theatre.get_available_seats())
print(theatre.total_revenue())