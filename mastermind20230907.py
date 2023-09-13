import math
import random
import os

localDirection = os.path.dirname(__file__)
relativeDirection = "txtfile/mastermind/scoreboard.txt"
scoreboardDirection = os.path.join(localDirection, relativeDirection)

legacyScore = [] #Score will be (100-tries)*difficulty(0.75 for easy, 1 for normal, 1.2 for hard) rounded down to an integer
debugMode = False

def readScoreboard(scoreboard):
    scoreboardFile = open(scoreboardDirection, "r")
    for line in scoreboardFile:
        dataList = line.split("|")
        name = dataList[0]
        score = int(dataList[1])
        scoreboard.append([name, score])
    scoreboardFile.close()
    return scoreboard

def writeScoreboard():
    scoreboardFile = open(scoreboardDirection, "w")
    for record in legacyScore:
        scoreboardFile.write(record[0])
        scoreboardFile.write("|")
        scoreboardFile.write(str(record[1]))
        scoreboardFile.write("\n")
    scoreboardFile.close()

def orderScoreboard(scoreboard):
    scoreboardLength = len(scoreboard)
    for i in range(scoreboardLength):
        scoreSorted = True
        for j in range(scoreboardLength - i - 1):
            if scoreboard[j][1] < scoreboard[j + 1][1]:
                scoreboard[j], scoreboard[j + 1] = scoreboard[j + 1], scoreboard[j]
                scoreSorted = False
        if scoreSorted:
            break
    return scoreboard

def menu():
    global debugMode
    global legacyScore
    programOn = True
    legacyScore = orderScoreboard(readScoreboard(legacyScore))
    while programOn:
        print("""
            M A S T E R M I N D            
            1.     START
            2.   SCOREBOARD
            3.  EXPORT SCORE
            4.      END
        """)
        try:
            menuChoice = int(input("\nPlease enter the number before your choice."))
            if menuChoice == 1:
                gameStart()
            elif menuChoice == 2:
                displayScore()
            elif menuChoice == 3:
                writeScoreboard()
            elif menuChoice == 4:
                programOn = False
            elif menuChoice == 114514:
                if debugMode:
                    debugMode = False
                    print("\nDEBUG MODE DEACTIVATED!\n")
                else:
                    debugMode = True
                    print("\nDEBUG MODE ACTIVATED!\n")
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")

    
def displayScore():
    rank = 0
    print("SCOREBOARD")
    for record in legacyScore:
        rank += 1
        recordName = record[0]
        recordScore = record[1]
        print(f"\n{rank:2}. {recordName:6}: {recordScore:3}")
    userConfirmation = input("\nPress enter to return to menu.")

def gameStart():
    global legacyScore
    numberStringList = ["_", "_", "_", "_"]
    difficultyChosen = False
    numberGuessed = False
    playerTries = 0
    playerScore = 0
    playerName = ""
    while not(difficultyChosen):
        print('Please choose the difficulty of this game.\n"E"for Easy, "N" for Normal, "H" for Hard.')
        difficulty = input().upper()
        if not(difficulty == "E" or difficulty == "N" or difficulty == "H"):
            print("Invalid input, please try again.")
        else:
            difficultyChosen = True
    numberList = numberGeneration(difficulty)
    while not(numberGuessed):
        playerGuessList = []
        playerGuessListIndex = 0
        correctDigit = 0
        if debugMode:
            print("DEBUG MODE:")
            for digit in numberList:
                print(digit)
        if difficulty == "H":
            try:
                playerGuess = int(input(f"\nPlease enter a 5 digit number, digits after the decimal point will be ignored.\nYou have tried {playerTries} times."))
                if not(len(str(playerGuess)) == 5):
                    print("Not a 5 digit number, please try again.")
                else:
                    playerTries += 1
                    for digit in str(playerGuess):
                        playerGuessList.append(digit)
                    for digit in playerGuessList:
                        if debugMode:
                            print(f"\nnumberList[playerGuessListIndex]: {numberList[playerGuessListIndex]}\ndigit: {digit}")
                        if numberList[playerGuessListIndex] == int(digit):
                            correctDigit += 1
                        playerGuessListIndex += 1
                    if correctDigit == 5:
                        print("You guessed the correct number, well done!")
                        numberGuessed = True
                    elif correctDigit > 0:
                        print(f"You got {correctDigit} digits right!")
                    else:
                        print("None of the digits you guessed is correct, try again.")
            except ValueError:
                print("Not a number, please try again.")
        elif difficulty == "N":
            try:
                playerGuess = int(input(f"\nPlease enter a 4 digit number.\nYou have tried {playerTries} times."))
                if not(len(str(playerGuess)) == 4):
                    print("Not a 4 digit number, please try again.")
                else:
                    playerTries += 1
                    for digit in str(playerGuess):
                        playerGuessList.append(digit)
                    for digit in playerGuessList:
                        if debugMode:
                            print(f"\nnumberList[playerGuessListIndex]: {numberList[playerGuessListIndex]}\ndigit: {digit}")
                        if numberList[playerGuessListIndex] == int(digit):
                            correctDigit += 1
                        playerGuessListIndex += 1
                    if correctDigit == 4:
                        print("You guessed the correct number, well done!")
                        numberGuessed = True
                    elif correctDigit > 0:
                        print(f"You got {correctDigit} digits right!")
                    else:
                        print("None of the digits you guessed is correct, try again.")
            except ValueError:
                print("Not a number, please try again.")
        else:
            print(f"\nNumber:\n{numberStringList[0]}{numberStringList[1]}{numberStringList[2]}{numberStringList[3]}")
            try:
                playerGuess = int(input(f"\nPlease enter a 4 digit number.\nYou have tried {playerTries} times."))
                if not(len(str(playerGuess)) == 4):
                    print("Not a 4 digit number, please try again.")
                else:
                    playerTries += 1
                    for digit in str(playerGuess):
                        playerGuessList.append(digit)
                    for digit in playerGuessList:
                        if debugMode:
                            print(f"\nnumberList[playerGuessListIndex]: {numberList[playerGuessListIndex]}\ndigit: {digit}")
                        if numberList[playerGuessListIndex] == int(digit):
                            if debugMode:
                                print(f"\nnumberStringList[playerGuessListIndex]: {numberStringList[playerGuessListIndex]}\nREPLACED BY\n{digit}")
                            numberStringList[playerGuessListIndex] = digit
                            correctDigit += 1
                        playerGuessListIndex += 1
                    if correctDigit == 4:
                        print("You guessed the correct number, well done!")
                        numberGuessed = True
                    elif correctDigit > 0:
                        print(f"You got {correctDigit} digits right!")
                    else:
                        print("None of the digits you guessed is correct, try again.")
            except ValueError:
                print("Not a number, please try again.")
    if numberGuessed:
        incompatibleCharacter = True
        validName = False
        if difficulty == "H":
            playerScore = math.floor((100 - playerTries) * 1.2)
        elif difficulty == "N":
            playerScore = math.floor(100 - playerTries)
        else:
            playerScore = math.floor((100 - playerTries) * 0.75)
        print(f"\nYou win!\n Your score: {playerScore}")
        while not(validName) or incompatibleCharacter:
            incompatibleCharacter = False
            playerName = input("\nPlease enter your name(Maximum 6 characters).")
            if len(playerName) <= 6:
                validName = True
            else:
                validName = False
            for character in playerName:
                if character == "|":
                    incompatibleCharacter = True
        playerRecord = [playerName, playerScore]
        legacyScore.append(playerRecord)
        legacyScore = orderScoreboard(legacyScore)
        displayScore()
    else:
        print("Unknown error, you shouldn't see this in a normal game.")
    
def numberGeneration(difficulty):
    numberList = []
    numberList.append(random.randint(1, 9))
    if difficulty == "H":
        for i in range(4):
            numberList.append(random.randint(0, 9))
    else:
        for i in range(3):
            numberList.append(random.randint(0, 9))
    return numberList

menu()