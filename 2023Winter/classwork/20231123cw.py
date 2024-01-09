usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']

def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    number = int(usernumber)
    print("Welcome", usernames[number], "user number", number,".")
    division = 301 / number
    print(f"301 divided by {number} = {division}")

def login_handled(number: int):
    try:
        number = int(number)
        print("\n -- The Enhanced Version --\n")
        print(f"Welcome{usernames[number]}\nUser ID: {number}.")
        print(f"301 divided by {number} = {float(301 / number)}")
    except ZeroDivisionError:
        print("\nIt is impossible to divide by zero, please try again.")
    except ValueError:
        print("\nNot an integer, please try again.")
    except IndexError:
        print("\nUser ID doesn't exist, please try again.")
    except Exception:
        print("\nUnknown error, please try again.")

def login_condition(number: int):
    if number.isdigit():
        number = int(number)
        print("\n -- The Enhanced Version --\n")
        if number != 0:
            if number < len(usernames):
                print(f"Welcome{usernames[number]}\nUser ID: {number}.")
                print(f"301 divided by {number} = {float(301 / number)}")
            else:
                print("\nUser ID doesn't exist, please try again.")
        else:
            print("\nIt is impossible to divide by zero, please try again.")
    else:
        print("\nNot an integer, please try again.")

while True:
    #inp = input("\nType in a number: ")
    #login_unhandled(inp)
    #inp = input("\nType in a number: ")
    #login_handled(inp)
    inp = input("\nType in a number: ")
    login_condition(inp)
