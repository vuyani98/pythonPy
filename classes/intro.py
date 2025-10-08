
class Book:
    #constructor
    #in every method of a class, the first parameter is always self
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def displayInfo(self):
        print(f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}")
        

firstBook = Book("1984", "George Orwell", "Dystopian") #object
secondBook = Book("To Kill a Mockingbird", "Harper Lee", "Fiction") #object

bookList = [firstBook, secondBook]

#dictionary
libraryMember = { "name": 'Alice', "memberID": 12345, "borrowedBooks": [firstBook]}

print(f"{libraryMember['name']} has borrowed {libraryMember['borrowedBooks'][0].title}")

