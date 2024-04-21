decimalNumber = int(input("Please enter a decimal nuber:    "))
binaryString = ""
while decimalNumber >= 1:
    binaryString = str(decimalNumber % 2) + binaryString
    decimalNumber = decimalNumber // 2
print(binaryString)