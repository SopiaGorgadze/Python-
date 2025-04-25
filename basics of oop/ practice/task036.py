# nested classes

 

class Library:
    
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author
        
        def display(self):
            print(f"title: {self.title}, author: {self.author}")


library = Library()
book = library.Book("pride and prejudice", "jane austen")
book2 = library.Book("1984", "george orwell")

book.display()
book2.display()