# Imports

import math

# Global Variables

# Functions

def checkIntIsPrime(number: int) -> bool:
    isPrime = True
    if number <= 1:
        return (isPrime)
    else:
        for factor in range(2, int(math.sqrt(number) + 1)):
            if number % factor == 0:
                isPrime = False
                break
    return (isPrime)

def showPrimeBetween(lowerBound: int, upperBound: int) -> list:
    primeNumberList = []
    for number in range(lowerBound, upperBound):
        if checkIntIsPrime(number):
            primeNumberList.append(number)
    return (primeNumberList)

def sieveOfErastothenes(upperbound: int) -> list:
    primeBooleanList = [True for i in range(upperbound + 1)]
    nextPrime = 2
    while((nextPrime ** 2) < upperbound):
        if primeBooleanList[nextPrime]:
            for index in range(nextPrime ** 2, upperbound + 1, nextPrime):
                primeBooleanList[index] = False
        nextPrime += 1
    return (primeBooleanList)

def readSieve(primeBooleanList: list):
    for number in range(2, len(primeBooleanList)):
        if primeBooleanList[number]:
            print(number)

# Main

"""while True:
    userInput = input("Please enter an integer: ")
    print(checkIntIsPrime(int(userInput)))
    if input('Do you want to stop?\nEnter "No" to stop, press Enter to continue.\n').lower() == "no":
        break"""

"""for number in showPrimeBetween(0, 10000000):
    print(number)"""

if __name__ == "__main__":
    readSieve(sieveOfErastothenes(100000000))