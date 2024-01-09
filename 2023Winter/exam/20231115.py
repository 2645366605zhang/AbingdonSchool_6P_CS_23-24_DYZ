# Imports

# Constants

# Functions

def main():
    targetWord = input("Please enter the first word.")
    materialWord = input("Please enter the second word.")
    if tryConstructWord(wordToLetterList(targetWord), wordToLetterList(materialWord)):
        print(f"The word {targetWord} can be created using the letters from the word {materialWord}.")
    else:
        print(f"The word {targetWord} can't be created using the letters from the word {materialWord}.")

def wordToLetterList(word):
    letterList = []
    for letter in word:
        letterList = checkIfLetterRepeated(letterList, letter.upper())
    return letterList

def checkIfLetterRepeated(letterList, newLetter):
    letterListIndex = 0
    for letterItem in letterList:
        if letterItem[0] == newLetter:
            letterList[letterListIndex][1] += 1
            return letterList
        letterListIndex += 1
    letterList.append([newLetter, 1])
    return letterList

def tryConstructWord(targetletterList, materialLetterList):
    for targetLetterItem in targetletterList:
        letterFound = False
        for i in range(targetLetterItem[1]):
            materialLetterListIndex = 0
            for materialLetterItem in materialLetterList:
                if targetLetterItem[0] == materialLetterItem[0]:
                    letterFound = True
                    materialLetterList[materialLetterListIndex][1] -= 1
                    if materialLetterList[materialLetterListIndex][1] < 0:
                        return False
                materialLetterListIndex += 1
        if not(letterFound):
            return False
    return True

# Main

main()