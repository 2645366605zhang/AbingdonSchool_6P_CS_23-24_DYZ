# Imports

import datetime

# Classes

class Empty(Exception):
    pass

class StockItem():

    def __init__(self, title: str, dateAcquired: datetime = datetime.date.today(), description: str = "item", onLoan: bool = False):
        self._title = title
        self._dateAcquired = dateAcquired
        self._description = description
        self._onLoan = onLoan

    def __str__(self) -> str:
        return self.getDetails()

    def setLoan(self):
        self._onLoan = True
    
    def returnLoan(self):
        self._onLoan = False
    
    def getLoanDetails(self):
        if self._onLoan:
            return (f"\nThis {self._description} is currently on loan.")
        else:
            return (f"\nThis {self._description} is currently not on loan.")

    def getTitle(self):
        return (f"Title: {self._title}")

    def getDetails(self):
        details = (f"Title: {self._title}\nAcquired on {self._dateAcquired.isoformat()}") + self.getLoanDetails()
        return details

    def displayDetails(self):
        print("\n" + self.getDetails())

class Book(StockItem):

    def __init__(self, title: str, author: str, isbn: str, dateAcquired: datetime = datetime.date.today(), description: str = "book", onLoan: bool = False):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._dateAcquired = dateAcquired
        self._description = description
        self._onLoan = onLoan
        if not(self.checkISBN()):
            print(f'Warning: The Book named "{self._title}" has a invalid ISBN: {self._isbn}')
    
    def checkISBN(self):
        if len(self._isbn) != 13:
            return False
        calculatedDigit = 0
        isbnIndex = 0
        for digit in self._isbn:
            if (isbnIndex % 2) == 0:
                calculatedDigit += int(digit) * 3
            else:
                calculatedDigit += int(digit)
            isbnIndex += 1
        calculatedDigit = 10 - (calculatedDigit % 10)
        if calculatedDigit == 10:
            calculatedDigit = 0
        if calculatedDigit == int(self._isbn[12:]):
            return True
        else:
            return False
    
    def getDetails(self):
        details = self.getTitle() + (f"\nAuthor: {self._author}\nISBN: {self._isbn}\nAcquired on {self._dateAcquired.isoformat()}") + self.getLoanDetails()
        return details

class Disk(StockItem):

    def __init__(self, title: str, artist: str, playingTime: int, dateAcquired: datetime = datetime.date.today(), description: str = "disk", onLoan: bool = False):
        self._title = title
        self._artist = artist
        self._playingTime = playingTime
        self._dateAcquired = dateAcquired
        self._description = description
        self._onLoan = onLoan
    
    def getDetails(self):
        details = self.getTitle() + (f"\nArtist: {self._artist}\nPlaying Time: {self._playingTime}s\nAcquired on {self._dateAcquired.isoformat()}") + self.getLoanDetails()
        return details

# Examples

if __name__ == "__main__":
    exampleBook = Book("The Example Book", "PLACEHOLDER", "1145141919810")
    exampleBook.displayDetails()
    exampleDisk = Disk("Never Gonna Give You Up", "Rick Astley", 212)
    exampleDisk.setLoan()
    print("\n", end = "")
    print(exampleDisk)