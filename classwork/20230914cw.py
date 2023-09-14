import datetime

def untilChristmas():
    today = datetime.datetime.today()
    christmasDate = datetime.datetime(today.year, 12, 25)
    daysUntil = christmasDate - today
    if daysUntil.days < 0:
        christmasDate = datetime.datetime((today.year + 1), 12, 25)
        daysUntil = christmasDate - today
    return daysUntil.days

def untilBirthday():
    today = datetime.datetime.today()
    invalidMonth = True
    invalidDate = True
    while invalidMonth:
        try:
            birthdayMonth = int(input("Please enter the month of your birthday(integer 1 - 12 inclusive)."))
            if (birthdayMonth >= 1) and (birthdayMonth <= 12):
                invalidMonth = False
            else:
                print("Number given out of range, please try again.")
        except ValueError:
            print("Not a number, please try again")
    if birthdayMonth == 2:
        maxDate = 28
    elif (birthdayMonth == 4) or (birthdayMonth == 6) or (birthdayMonth == 9) or (birthdayMonth == 11):
        maxDate = 30
    else:
        maxDate = 31
    while invalidDate:
        try:
            birthdayDay = int(input(f"Please enter the date of your birthday(integer 1 - {maxDate} inclusive).\n(If your birthday is at Feburary the 29th, please input 28 as the date.)"))
            if (birthdayMonth >= 1) and (birthdayMonth <= maxDate):
                invalidDate = False
            else:
                print("Number given out of range, please try again.")
        except ValueError:
            print("Not a number, please try again")
    birthdayDate = datetime.datetime(today.year, birthdayMonth, birthdayDay)
    daysUntil = birthdayDate - today
    if daysUntil.days < 0:
        birthdayDate = datetime.datetime((today.year + 1), birthdayMonth, birthdayDay)
        daysUntil = birthdayDate - today
    return daysUntil.days

print(untilChristmas())
print(untilBirthday())