from random import randint

def shuffleList(originalList: list) -> list:
    halfLength = int(len(originalList) / 2)
    firstHalf = []
    secondHalf = []
    finalList = []
    maxPushSize = 3
    for index in range(halfLength):
        firstHalf.append(originalList.pop(index))
    secondHalf = originalList
    print(f"FirstHalfL: {len(firstHalf)}, SecondHalfL: {len(secondHalf)}")
    while True:
        print(f"Current Final: {finalList}")
        if len(firstHalf) < maxPushSize:
            maxPushSize = len(firstHalf) - 1
        elif len(secondHalf) < maxPushSize:
            maxPushSize = len(secondHalf) - 1
        if maxPushSize <= 0:
            break
        firstPushSize, secondPushSize = randint(0, maxPushSize), randint(0, maxPushSize)
        while firstPushSize > 0:
            print(f"First: Size: {len(firstHalf)}, Index: {firstPushSize}\n")
            finalList.append(firstHalf.pop(0))
            firstPushSize -= 1
        while secondPushSize > 0:
            print(f"Second: Size: {len(secondHalf)}, Index: {secondPushSize}\n")
            finalList.append(secondHalf.pop(0))
            secondPushSize -= 1
    return finalList + firstHalf + secondHalf

print(shuffleList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]))