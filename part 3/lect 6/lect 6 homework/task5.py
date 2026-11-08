class Room:
    def __init__(self,booking):
        if booking== None:
            self.number=0
            self.room_type=""
            self.price=0
        else:
            self.number=booking.number
            self.room_type=booking.room_type
            self.price=booking.price
    def book(self,name):
        print(f"Room {self.number} booked for {name}")
    def display(self):
        print(f"Room {self.number} | {self.room_type} | Rs {self.price} per night")
room1 = Room(None)
room1.number = 101
room1.room_type = "Deluxe"
room1.price = 2500
room2 = Room(room1)
room2.number = 102
room1.book("Anita")
room2.book("Ravi")
room1.display()
room2.display()