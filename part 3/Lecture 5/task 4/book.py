
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_details(self):
        print(self.title)
        print(self.author)
        print(self.pages)

    def reading_time(self):
        return self.pages * 2


title = input()
author = input()
pages = int(input())

book = Book(title, author, pages)
book.show_details()
print(book.reading_time())
