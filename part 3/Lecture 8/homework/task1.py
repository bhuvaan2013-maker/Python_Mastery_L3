class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def show(self):
        print(f"{self.title} by {self.author}")
class EBook(Book):
    def __init__(self,title,author,file_size_mb):
        super().__init__(title,author)
        self.file_size_mb=file_size_mb
    def show_size(self):
        print(f"File Size: {self.file_size_mb}MB")
tung=Book("Harry Potter","J.K Rowling")
tung.show()
sahur=EBook("Harry Potter","J.K Rowling",12)
sahur.show_size()