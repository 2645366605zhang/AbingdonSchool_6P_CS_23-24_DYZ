# Imports

from math import factorial

# Constants

# Variables

# Functions

def Dec2Bin(decNum: int) -> int:
    resultString = ""
    while True:
        if decNum == 0:
            break
        else:
            resultString = f"{decNum % 2}" + resultString
            decNum = decNum // 2
    return int(resultString)

def Bin2Dec(binNum: int) -> int:
    power = 0
    resultInteger = 0
    for bit in reversed(str(binNum)):
        if bit == "1":
            resultInteger += 2 ** power
        power += 1
    return resultInteger

def Dec2Hex(decNum: int) -> str:
    resultString = ""
    digitString = "0123456789ABCDEF"
    while True:
        if decNum == 0:
            break
        else:
            resultString = f"{digitString[decNum % 16]}" + resultString
            decNum = decNum // 16
    return resultString

def Dec2B22(decNum: int) -> str:
    resultString = ""
    digitString = "甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥"
    while True:
        if decNum == 0:
            break
        else:
            resultString = f"{digitString[decNum % 22]}" + resultString
            decNum = decNum // 22
    return resultString

def Dec2B26(decNum: int) -> str:
    resultString = ""
    digitString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        if decNum == 0:
            break
        else:
            resultString = f"{digitString[decNum % 26]}" + resultString
            decNum = decNum // 26
    return resultString

def Dec2B32(decNum: int) -> str:
    resultString = ""
    digitString = "0123456789ABCDEFGHIJKLMNOPQRSTUV"
    while True:
        if decNum == 0:
            break
        else:
            resultString = f"{digitString[decNum % 32]}" + resultString
            decNum = decNum // 32
    return resultString

def Dec2B36(decNum: int) -> str:
    resultString = ""
    digitString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        if decNum == 0:
            break
        else:
            resultString = f"{digitString[decNum % 36]}" + resultString
            decNum = decNum // 36
    return resultString

def Dec2B42(decNum: int) -> str:
    resultString = ""
    digitString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZÄËÏÖÜß"
    while True:
        if decNum == 0:
            break
        else:
            resultString = f"{digitString[decNum % 42]}" + resultString
            decNum = decNum // 42
    return resultString

def Dec2B64(decNum: int) -> str:
    resultString = ""
    digitString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZÄËÏÖÜß甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥"
    while True:
        if decNum == 0:
            break
        else:
            resultString = f"{digitString[decNum % 64]}" + resultString
            decNum = decNum // 64
    return resultString

def Dec2B94(decNum: int) -> str:
    resultString = ""
    digitString = """`~1!2@3#4$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpP[{]}\|aAsSdDfFgGhHjJkKlL;:'"zZxXcCvVbBnNmM,<.>/?"""
    while True:
        if decNum == 0:
            break
        else:
            resultString = f"{digitString[decNum % 94]}" + resultString
            decNum = decNum // 94
    return resultString

def Dec2B122(decNum: int) -> str:
    resultString = ""
    digitString = """`~1!2@3#4$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpP[{]}\|aAsSdDfFgGhHjJkKlL;:'"zZxXcCvVbBnNmM,<.>/?ÄËÏÖÜß甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥"""
    while True:
        if decNum == 0:
            break
        else:
            resultString = f"{digitString[decNum % 122]}" + resultString
            decNum = decNum // 122
    return resultString

def Dec2BAny(baseNum: int, decNum: int) -> str:
    if baseNum > 36:
        raise ValueError("Dec2BAny() is not compatible for base number above 36.")
    resultString = ""
    digitString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZÄËÏÖÜß"
    while True:
        if decNum == 0:
            break
        else:
            resultString = f"{digitString[decNum % baseNum]}" + resultString
            decNum = decNum // baseNum
    return resultString

# Main

if __name__ == "__main__":
    myNum = 114514
    #print(Dec2Bin(mynum))
    #mynum = Dec2Bin(mynum)
    #print(Bin2Dec(mynum))
    print(f"\nBase 10:\n{str(myNum)}\n")
    print(f"\nBase 2: \n{Dec2Bin(myNum)}\n")
    print(f"\nBase 16: \n{Dec2Hex(myNum)}\n")
    print(f"\nBase 22: \n{Dec2B22(myNum)}\n")
    print(f"\nBase 26: \n{Dec2B26(myNum)}\n")
    print(f"\nBase 32: \n{Dec2B32(myNum)}\n")
    print(f"\nBase 36: \n{Dec2B36(myNum)}\n")
    print(f"\nBase 42: \n{Dec2B42(myNum)}\n")
    print(f"\nBase 64: \n{Dec2B64(myNum)}\n")
    print(f"\nBase 94: \n{Dec2B94(myNum)}\n")
    print(f"\nBase 122: \n{Dec2B122(myNum)}\n")
   #print(f"\nBase {myNum}: \n{Dec2BAny(myNum, myNum)}\n")
    