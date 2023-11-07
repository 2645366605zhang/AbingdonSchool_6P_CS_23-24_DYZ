def checkISBN():
    isbn = [None, None, None, None, None, None, None, None, None, None, None, None, None]
    for count in range(13):
        isbn[count] = input("Please enter next digit of ISBN: ")
    calculatedDigit = 0
    count = 0
    while count < 12:
        calculatedDigit += int(isbn[count])
        #print(f"This is digit {count}, CD is now {calculatedDigit}")
        count += 1
        calculatedDigit += int(isbn[count]) * 3
        #print(f"This is digit {count}, CD is now {calculatedDigit}")
        count += 1
    while calculatedDigit >= 10:
        #print(f"CD ({calculatedDigit}) greater than 10, remove 10")
        calculatedDigit -= 10
    calculatedDigit = 10 - calculatedDigit
    #print(f"CD was {10 - calculatedDigit}, now {calculatedDigit}")
    if calculatedDigit == 10:
        calculatedDigit = 0
        #print(f"CD ({calculatedDigit}) is 10, clamping to 0")
    #print(f"Last digit is {isbn[12]}, CD is {calculatedDigit}")
    if calculatedDigit == int(isbn[12]):
        print("Valid ISBN")
    else:
        print("Invalid ISBN")

def betterCheckISBN(isbn: str):
    if len(isbn) != 13:
        return False
    calculatedDigit = 0
    isbnIndex = 0
    for digit in isbn:
        if (isbnIndex % 2) == 0:
            calculatedDigit += int(digit) * 3
        else:
            calculatedDigit += int(digit)
        isbnIndex += 1
    calculatedDigit = 10 - (calculatedDigit % 10)
    if calculatedDigit == 10:
        calculatedDigit = 0
    if calculatedDigit == int(isbn[12:]):
        return True
    else:
        return False

#checkISBN()
print(betterCheckISBN("9781510405196"))