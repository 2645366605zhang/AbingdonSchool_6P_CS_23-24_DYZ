import datetime

class Book():

    def __init__(self, title: str, author: str, isbn: int, onLoan: bool, dateAcquired: datetime):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._onLoan = onLoan
        self._dateAcquired = dateAcquired

    def __str__(self):
        return self.getBookDetails()
    
    def getBookDetails(self):
        bookDetails = (f"Title: {self._title}\nAuthor: {self._author}\nISBN: {self._isbn}\nAcquired on {self._dateAcquired.isoformat()}")
        if self._onLoan:
            bookDetails += "\nThis book is currently on loan."
        else:
            bookDetails += "\nThis book is currently not on loan."
        return bookDetails
    
    def displayBookDetails(self):
        print(self.getBookDetails())

    def setLoan(self):
        self._onLoan = True
    
    def returnLoan(self):
        self._onLoan = False

exampleBook = Book("The Example Book", "PLACEHOLDER", 0000000000000, True, datetime.date.today())
exampleBook.displayBookDetails()