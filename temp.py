def top_3_words(text):
    currentWord = ""
    wordList = []
    wordOccuranceList = []
    wordCoposition = "abcdefghijklmnopqrstuvwxyz'ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in text:
        if letter in wordCoposition:
            currentWord += letter.lower()
        else:
            wordNotPresent = True
            for wordIndex in range(len(wordList)):
                if wordList[wordIndex] == currentWord:
                    wordOccuranceList[wordIndex] += 1
                    wordNotPresent = False
                    currentWord = ""
                    break
            if wordNotPresent and (currentWord != "") and (currentWord != len(currentWord) * "'"):
                wordList.append(currentWord)
                wordOccuranceList.append(1)
                currentWord = ""
    wordNotPresent = True
    for wordIndex in range(len(wordList)):
        if wordList[wordIndex] == currentWord:
            wordOccuranceList[wordIndex] += 1
            wordNotPresent = False
            currentWord = ""
            break
    if wordNotPresent and (currentWord != "") and (currentWord != len(currentWord) * "'"):
        wordList.append(currentWord)
        wordOccuranceList.append(1)
        currentWord = ""
    print(wordList)
    print(wordOccuranceList)
    if len(wordList) < 3:
        returnList = [""] * len(wordList)
    else:
        returnList = [""] * 3
    for wordIndex in range(len(returnList)):
        returnList[wordIndex] = wordList[wordOccuranceList.index(max(wordOccuranceList))]
        wordList.pop(wordOccuranceList.index(max(wordOccuranceList)))
        wordOccuranceList.pop(wordOccuranceList.index(max(wordOccuranceList)))
    return returnList

#print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
#print(top_3_words("  '  "))
print(top_3_words("TWUEgeKNfF _ceel,TWUEgeKNfF,!?;-TWUEgeKNfF//-!:ceel,-TWUEgeKNfF?_ceel;TWUEgeKNfF-/ceel; ,,TWUEgeKNfF__ceel.:;ceel.TWUEgeKNfF.:: ceel/TWUEgeKNfF-ceel!-  TWUEgeKNfF  :/ TWUEgeKNfF--TWUEgeKNfF._?.!TWUEgeKNfF/!-, TWUEgeKNfF//.TWUEgeKNfF /:-TWUEgeKNfF_,,TWUEgeKNfF?!ceel,_.ceel.;:ceel-_,TWUEgeKNfF,TWUEgeKNfF-ceel ;!TWUEgeKNfF!//TWUEgeKNfF.,_TWUEgeKNfF._!ceel?TWUEgeKNfF?TWUEgeKNfF_ _ ceel?_;ceel.!  ;TWUEgeKNfF:ceel;/-TWUEgeKNfF_TWUEgeKNfF:?:?"))