# composition

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.booklist = []

    def add_book(self, book):
        self.booklist.append(book)


    def books(self):
        for book in self.booklist:
            print(book.title)

book = Book("harry potter")

library = Library()

library.add_book(book)
library.books()