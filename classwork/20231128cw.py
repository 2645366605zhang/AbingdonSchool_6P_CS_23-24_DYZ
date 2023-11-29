# Imports

import KCSys as sys
import os

# Functions

def clearConsole():
    os.system("cls")

def game():
    # Initialisation
    clearConsole()
    gameBoard = sys.KCBoard(input("Please enter your username: "))
    clearConsole()
    attempt = 0
    while True and attempt < 5:
        if gameBoard.checkWin() != None:
            break
        gameBoard.displayWithMap()
        print(gameBoard.playerTurn())
        clearConsole()
        if (gameBoard.checkWin() != None) or (gameBoard.checkDraw()):
            break
        print(gameBoard.newAiTurn())
        #print(gameBoard.aiTurn())
        #print(gameBoard.playerAiTurn())
        attempt += 1
    gameBoard.display()
    if gameBoard.checkWin() != None:
        print(f"{gameBoard.checkWin()} wins!\n")
    else:
        print("This game is a draw!\n")
    userConfirmation = input("Press Enter to return to the menu.")

def main():
    # Menu
    while True:
        validInput = False
        try:
            clearConsole()
            userChoice = int(input("""
-------------------------
K N O T  A N D  C R O S S
-------------------------
1. S T A R T  G A M E
2. Q U I T

Please enter the integer of your choice.

"""))
        except ValueError:
            print("Invalid input, please try again.")
        if userChoice == 1:
            game()
        elif userChoice == 2:
            break
        else:
            print("Invalid input, please try again.")

# Main

main()