import random

def binarySearchAnimal(listOfData, target):
    targetNotFound = True
    result = [False, None]
    topPointer = 0
    endPointer = (len(listOfData) - 1)
    midPointer = (topPointer + ((endPointer - topPointer) // 2))
    while targetNotFound:
        #print(f"topP: {topPointer}\nendP: {endPointer}\nmidP: {midPointer}\n") # Debug
        if listOfData[midPointer] == target:
            targetNotFound = False
            result = [True, midPointer]
        elif midPointer == topPointer:
            break
        else:
            letterIndex = 0
            dataGreaterThanTarget = False
            for letter in listOfData[midPointer]:
                if letter > target[letterIndex]:
                    break
                elif letter < target[letterIndex]:
                    dataGreaterThanTarget = True
                    break
                letterIndex += 1
            if dataGreaterThanTarget:
                topPointer = midPointer
                midPointer = (topPointer + ((endPointer - topPointer) // 2))
            else:
                endPointer = midPointer
                midPointer = (topPointer + ((endPointer - topPointer) // 2))
    return result

myAnimalList = ["alligator", "bee", "cat", "dog", "elephant", "fish", "gazelle", "grasshopper", "hippopotamus", "horse", "hyena", "iguana", "jaguar", "jellyfish"]
randomAnimal = myAnimalList[random.randint(0, (len(myAnimalList) - 1))]
print(f"\nAnimal: {randomAnimal}\nResult: {binarySearchAnimal(myAnimalList, randomAnimal)}\n")