def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    resultList = []
    for number in range(a, b + 1):
        digitCount = 0
        digitProduct = 0
        for digit in str(number):
            digitCount += 1
            if digitProduct == 0:
                digitProduct = int(digit)
            else:
                digitProduct = digitProduct + (int(digit) ** digitCount)
            #print(f"DigitProduct of {number} is now {digitProduct}\n")
        if digitProduct == number:
            resultList.append(number)
    return resultList

print(sum_dig_pow(1, 100))
print(sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])