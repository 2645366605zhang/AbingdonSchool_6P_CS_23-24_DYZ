def pig_it(text):
    wordList = []
    letterList = []
    letterIndex = 0
    for letter in text:
        if letter.isalpha():
            letterList.append(letter)
        else:
            if letterList != []:
                letterList.append(letterList.pop(0))
                letterList.append("a")
                letterList.append("y")
                wordList.append(letterList)
                letterList = []
            wordList.append(letter)
        letterIndex += 1
        if letterIndex == len(text) and letterList != []:
            letterList.append(letterList.pop(0))
            letterList.append("a")
            letterList.append("y")
            wordList.append(letterList)
    wordListIndex = 0
    sentenceString = ""
    for word in wordList:
        if type(word) == list:
            wordString = ""
            for letter in word:
                wordString += letter
            wordList[wordListIndex] = wordString
        sentenceString += wordList[wordListIndex]
        wordListIndex += 1
    return sentenceString

print(pig_it("hi "))