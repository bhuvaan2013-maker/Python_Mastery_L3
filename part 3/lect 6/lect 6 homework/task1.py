class Book:
    def __init__(self):
        self.title="Untitled"
        self.pages=0
        self.author="Unknown"
    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
    def open_book(self):
        print(f"Opening {self.title}....")
    def close_book(self):
        print(f"Closing {self.title}....")
book1 = Book()
book2 = Book()
book2.title = "The Clever Fox"
book2.author = "Meera Rao"
book2.pages = 120
book1.show_info()
book2.show_info()
book2.open_book()
book2.close_book()