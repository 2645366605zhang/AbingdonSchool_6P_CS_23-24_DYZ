# Imports
import os
import fileinput

# Constants
localDirection = os.path.dirname(__file__)
relativeFolderDirection = "txtfile/txteditor/"
fileDirection = os.path.join(localDirection, relativeFolderDirection)
unaccptedFileCharacters = [r"/", "\\", r":", r"*", r"?", r'"', r"<", r">", r"|"]

# Functions
def createFile():
    validFileName = False
    while not(validFileName):
        fileName = input('Please enter the name of the file you want to create.\nEnter "Cancel" to cancel this action.')
        if fileName.upper() == "CANCEL":
            break
        elif not(fileName.endswith(".txt")):
            fileName += ".txt"
            for character in fileName:
                if character in unaccptedFileCharacters:
                    print(f'Contains character "{character}" in your file name "{fileName}", please try again.')
                else:
                    validFileName = True
    if validFileName:
        relativeDirection = relativeFolderDirection + fileName
        fileDirection = os.path.join(localDirection, relativeDirection)
        try:
            creatingFile = open(fileDirection, "r", encoding = "utf8")
            creatingFile.close()
            print(f"{fileName} already exists!")
        except FileNotFoundError:
            creatingFile = open(fileDirection, "w", encoding = "utf8")
            creatingFile.close()
            print(f"Successfully Created file {fileName}!")

def displayText():
    validFileName = False
    while not(validFileName):
        fileName = input('Please enter the name of the file you want to browse.\nEnter "Cancel" to cancel this action.')
        if fileName.upper() == "CANCEL":
            break
        elif not(fileName.endswith(".txt")):
            fileName += ".txt"
        relativeDirection = relativeFolderDirection + fileName
        fileDirection = os.path.join(localDirection, relativeDirection)
        try:
            with open(fileDirection, "r", encoding = "utf8") as readingFile:
                validFileName = True
                for line in (readingFile.readlines()):
                    print(line, end = "")
                userConfirmation = input("\nPress Enter to return to menu.")
        except FileNotFoundError:
            print(f"{fileName} not found, please try again.")

def writeText():
    validFileName = False
    while not(validFileName):
        fileName = input('Please enter the name of the file you want to write to.\nEnter "Cancel" to cancel this action.')
        if fileName.upper() == "CANCEL":
            break
        elif not(fileName.endswith(".txt")):
            fileName += ".txt"
        relativeDirection = relativeFolderDirection + fileName
        fileDirection = os.path.join(localDirection, relativeDirection)
        try:
            with open(fileDirection, "w", encoding = "utf8") as writingFile:
                validFileName = True
                while True:
                    userInput = input(f'Please enter the content you want to add to the line, press Enter to write the next line.\nEnter "Cancel" to cancel this action.')
                    if userInput.upper() == "CANCEL":
                        break
                    else:
                        writingFile.write(userInput)
                userConfirmation = input("\nPress Enter to return to menu.")
        except FileNotFoundError:
            print(f"{fileName} not found, please try again.")

def appendText():
    validFileName = False
    while not(validFileName):
        fileName = input('Please enter the name of the file you want to append to.\nEnter "Cancel" to cancel this action.')
        if fileName.upper() == "CANCEL":
            break
        elif not(fileName.endswith(".txt")):
            fileName += ".txt"
        relativeDirection = relativeFolderDirection + fileName
        fileDirection = os.path.join(localDirection, relativeDirection)
        try:
            with open(fileDirection, "a", encoding = "utf8") as writingFile:
                validFileName = True
                while True:
                    userInput = input(f'Please enter the content you want to append to the text, press Enter to write the next line.\nEnter "Cancel" to cancel this action.')
                    if userInput.upper() == "CANCEL":
                        break
                    else:
                        writingFile.write(userInput)
                userConfirmation = input("\nPress Enter to return to menu.")
        except FileNotFoundError:
            print(f"{fileName} not found, please try again.")

def editText():
    validFileName = False
    while not(validFileName):
        fileName = input('Please enter the name of the file you want to edit.\nEnter "Cancel" to cancel this action.')
        if fileName.upper() == "CANCEL":
            break
        elif not(fileName.endswith(".txt")):
            fileName += ".txt"
        relativeDirection = relativeFolderDirection + fileName
        fileDirection = os.path.join(localDirection, relativeDirection)
        try:
            with open(fileDirection, "r+", encoding = "utf8") as editingFile:
                validFileName = True
                while True:
                    editingFileIndex = 0
                    try:
                        editingFile.seek(0)
                        targetIndex = int(input(f'Please enter the line number of the line you would like to check or edit.\nPress enter to return.'))
                        for line in editingFile.readlines():
                            editingFileIndex += 1
                            if editingFileIndex == targetIndex:
                                userInput = input(f'\n{line}\nIf you would like to replace this line, type "Edit".\nPress enter to return.')
                                if userInput.upper() == "EDIT":
                                    userInput = input("Please enter the content you want to replace this line with.\nPress enter to return.")
                                    if not(userInput == ""):
                                        lineList = []
                                        editingFile.seek(0)
                                        for l in editingFile.readlines():
                                            lineList.append(l)
                                        lineList[editingFileIndex - 1] = userInput + "\n"
                                        editingFile.seek(0)
                                        editingFile.mode = "w"
                                        for l in lineList:
                                            editingFile.write(l)
                                        editingFile.mode = "r+"
                                        break
                                    else:
                                        break
                                else:
                                    break
                    except ValueError:
                        break
        except FileNotFoundError:
            print(f"{fileName} not found, please try again.")

def menu():
    while True:
        print("""
         ┌───────────┐
         │.txt Editor│
         └───────────┘

1. Create a .txt file
2. Display an existing .txt file
3. Overwrite an existing .txt file
4. Append to an existing .txt file
5. Edit an existing .txt file
6. Quit
        """)
        try:
            menuChoice = int(input("\nPlease enter the number of your choice."))
            if menuChoice == 1:
                createFile()
            elif menuChoice == 2:
                displayText()
            elif menuChoice == 3:
                writeText()
            elif menuChoice == 4:
                appendText()
            elif menuChoice == 5:
                editText()
            elif menuChoice == 6:
                break
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")

# Main
menu()