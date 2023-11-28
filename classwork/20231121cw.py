# Imports

import WordComposition

# Constants

dictFileName = "words.txt"
with open(dictFileName, "r") as englishDictionary:
    englishDictionaryList = englishDictionary.readlines()

# Functions

def main():
    userWord = input("Please enter a word:")
    resultList = []
    for word in englishDictionaryList:
        result = WordComposition.main(userWord, word)
        if not(result == None):
            resultList.append(result[:-2])
    return resultList

# Main

print(main())