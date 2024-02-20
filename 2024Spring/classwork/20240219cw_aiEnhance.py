from time import sleep as wait

def dec2FPBin(decNum: float, maxDP: int = 1024) -> str:
    """
    Convert a decimal number to its binary representation in floating-point format.

    :param decNum: Decimal number to convert.
    :param maxDP: Maximum number of decimal places to consider (default is 1024).
    :return: Binary representation of the decimal number in floating-point format.
    """
    # Integer Process
    integerResult = bin(int(decNum))[2:]

    # Decimal Point Process
    decNum -= int(decNum)
    result = ""
    dpCount = 0
    recurring = False
    uniqueDPList = []
    recuttingStartNum = 0

    while dpCount <= maxDP:
        multipliedNum = decNum * 2

        if round(multipliedNum, 6) in uniqueDPList:
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
        dpCount += 1
        uniqueDPList.append(decNum)
        wait(0.05)

    if recurring:
        result = f"{result[:uniqueDPList.index(recuttingStartNum)]}|{result[uniqueDPList.index(recuttingStartNum):]}|"

    return integerResult + "·" + result

if __name__ == "__main__":
    print(dec2FPBin(114.514))