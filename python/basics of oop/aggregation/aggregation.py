# aggregation - represents a relationship where one object(the whole)
# contains references to one or more independent objects the parts

# one objext behaves as a container - the whole, which can contain other objects - the parts

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"Title: {book.title}, Author: {book.author}" for book in self.books]

# library can exist without books and books can exist without library they are INDEPENDENT classes which can live off on their owb, thats the difference between aggregation and composition

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("new york public library")

book1 =  Book("the fall", "albert camcus")
book2 = Book("thus spoke zaratursta", "friedrich nietzsche")
book3 = Book("the brothers karamazov", "fryodor dostoevsky")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
print(library.list_books())

for i in library.list_books():
    print(i)