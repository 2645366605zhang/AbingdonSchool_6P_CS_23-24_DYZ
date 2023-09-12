

validInteger = False
isANumber = False
targetIntegerA = 0
targetIntegerB = 0
lineResult = 0

while not(validInteger):
    isANumber = False
    try:
        targetIntegerB = int(input("Please enter the first integer.(Maximum 999)"))
        isANumber = True
    except ValueError:
        print("Not a number, please try again.")
    if isANumber:
        if targetIntegerB > 999 or targetIntegerB < 1:
            print("Number out of range, please try again.")
        elif not(str(targetIntegerB).isdecimal()):
            print("Not an integer, please try again.")
        else:
            validInteger = True

validInteger = False

while not(validInteger):
    isANumber = False
    try:
        targetIntegerA = int(input(f"Please enter an integer between 1 and {targetIntegerB}(inclusive)."))
        isANumber = True
    except ValueError:
        print("Not a number, please try again.")
    if isANumber:
        if targetIntegerA > targetIntegerB or targetIntegerA < 1:
            print("Number out of range, please try again.")
        elif not(str(targetIntegerA).isdecimal()):
            print("Not an integer, please try again.")
        else:
            validInteger = True

for number in range(1, (targetIntegerB + 1)):
    lineResult = targetIntegerA * number
    print(f"{targetIntegerA:3} × {number:3} = {lineResult:6}")

userConfirmation = input("Press enter to end the program.")