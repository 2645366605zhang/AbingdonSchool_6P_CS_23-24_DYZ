# Imports

from time import sleep as wait
from math import sqrt

# Constants

def dec2FPBin(decNum: float, maxDP: int = 1024) -> str:
    # Integer Process
    integerResult = ""
    integerDecNum = int(decNum // 1)
    print(f"\n\nintegerDecNum: {integerDecNum}\n\n")
    while True:
        if integerDecNum == 0:
            break
        else:
            integerResult = f"{integerDecNum % 2}" + integerResult
            integerDecNum = integerDecNum // 2
        print(f"\nDebug:\nintegerDecNum: {integerDecNum}\nintegerResult: {integerResult}\n")
        wait(0.01)
    if integerResult == "":
        integerResult = "0"
    # Decimal Point Process
    decNum -= decNum // 1
    result = ""
    dpCount = 0
    recurring = False
    uniqueDPList = []
    while True:
        multipliedNum = decNum * 2
        if dpCount > maxDP:
            break
        elif round(multipliedNum, 6) in uniqueDPList:
            recurring = True
            recuttingStartNum = round(multipliedNum, 6)
            break
        elif multipliedNum == 1:
            result += "1"
            break
        elif multipliedNum > 1:
            result += "1"
            multipliedNum -= 1
        else:
            result += "0"
        decNum = round(multipliedNum, 6)
        print(f"\nDebug:\ndecNum: {decNum}\nmultipliedNum: {round(multipliedNum, 6)}\nresult: {result}\n")
        dpCount += 1
        uniqueDPList.append(decNum)
        wait(0.05)
    if recurring:
        for uniqueDPIndex in range(len(uniqueDPList)):
            if uniqueDPList[uniqueDPIndex] == recuttingStartNum:
                result = "|".join([result[:uniqueDPIndex], result[uniqueDPIndex:]])
                result += "|"
                break
    return (integerResult + "·" + result)

# Variables

# Functions

# Main

if __name__ == "__main__":
    #print(dec2FPBin(sqrt(2), 1024))
    print(dec2FPBin(114.514, 1024))