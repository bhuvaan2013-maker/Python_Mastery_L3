class Book:
    def __init__(self):
        self.title=""
        self.pages=0
    def get_title(self):
        return self.title
    def get_pages(self):
        return self.pages
    def set_title(self,title):
        if title=="":
            print("Invalid title")
        else:
            self.title=title
    def set_pages(self,pages):
        if pages== str() or pages<1:
            print("Only a number more than 0 can be entered")
        else:
            self.pages=pages
    def is_long(self):
        if self.pages>299:
            return True
        else:
            return False
title = "Space Tales"
pages = 450
book = Book()
book.set_title(title)
book.set_pages(pages)
print(f"Title: {book.get_title()}")
print(f"Pages: {book.get_pages()}")
print(f"Long book: {book.is_long()}")