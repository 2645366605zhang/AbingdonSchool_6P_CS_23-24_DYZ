import datetime

def calc_next_birthday():
    dob = datetime.date(1982, 9, 11)
    today = datetime.date.today()

    print("My date of birth is: ", dob)
    print("Today is: ", today)
    birthday_this_year = datetime.date(today.year, dob.month, dob.day)
    birthday_next_year = datetime.date(today.year+1, dob.month, dob.day)

    if birthday_this_year > today:
        next_birthday = birthday_this_year
    else:
        next_birthday = birthday_next_year

    print('Next birthday: ', next_birthday)
    days_to_birthday = (next_birthday - today).days
    age = (next_birthday - dob).days // 365     # Note, this doesn't take account of leap years so isn't perfect.
    print('Days to next birthday: ', days_to_birthday)
    print('Age at next birthday: ', age)

calc_next_birthday()
