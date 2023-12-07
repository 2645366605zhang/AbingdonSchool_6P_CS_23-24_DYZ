#Skeleton Program for the AQA COMP1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA COMP1 Programmer Team
#developed in a Python 3.4 programming environment

import random

# Manipulate the content of the board according to the situation of game
def SetUpGameBoard(Board, Boardsize):
  for Row in range(1, BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if (Row == (BoardSize + 1) // 2 and Column == (BoardSize + 1) // 2 + 1) or (Column == (BoardSize + 1) // 2 and Row == (BoardSize + 1) // 2 + 1):
        Board[Row][Column] = "C"
      elif (Row == (BoardSize + 1) // 2 + 1 and Column == (BoardSize + 1) // 2 + 1) or (Column == (BoardSize + 1) // 2 and Row == (BoardSize + 1) // 2):
        Board[Row][Column] = "H"
      else:
        Board[Row][Column] = " "

# Take the user's input for how big the user wnat the board to be
def ChangeBoardSize():
  BoardSize = int(input("Enter a board size (between 4 and 9): "))
  while not(BoardSize >= 4 and BoardSize <= 9):
    BoardSize = int(input("Enter a board size (between 4 and 9): "))
  return BoardSize

# Take the user's input for where to put the user's pawn on the board
def GetHumanPlayerMove(PlayerName):
  print(PlayerName, "enter the coodinates of the square where you want to place your piece: ", end="")
  Coordinates = int(input())
  return Coordinates

# Randomly generate a coordinate for the computer to put its pawn on the board
def GetComputerPlayerMove(BoardSize):
  return random.randint(1, BoardSize) * 10 + random.randint(1, BoardSize)

# Reset the board after the game ends
def GameOver(Board, BoardSize):
  for Row in range(1 , BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if Board[Row][Column] == " ":
        return False
  return True

# Take the user's input for the user's name shown in the game
def GetPlayersName():
  PlayerName = input("What is your name? ")
  return PlayerName

# Check if the coordinate taken is valid(is inthe range of board and is empty)
def CheckIfMoveIsValid(Board, Move):
  Row = Move % 10
  Column = Move // 10
  MoveIsValid = False
  if Board[Row][Column] == " ":
    MoveIsValid = True
  return MoveIsValid

# Calculate the player's score my counting the number of pawns that belong to the player on the board
def GetPlayerScore(Board, BoardSize, Piece):
  Score = 0
  for Row in range(1, BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if Board[Row][Column] == Piece:
        Score = Score + 1
  return Score

# Check if any pawns can be fliped according to the game rules by looping through each pawn on the board
def CheckIfThereArePiecesToFlip(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection):
  RowCount = StartRow + RowDirection
  ColumnCount = StartColumn + ColumnDirection
  FlipStillPossible = True
  FlipFound = False
  OpponentPieceFound = False
  while RowCount <= BoardSize and RowCount >= 1 and ColumnCount >= 1 and ColumnCount <= BoardSize and FlipStillPossible and not FlipFound:
    if Board[RowCount][ColumnCount] == " ":
      FlipStillPossible = False
    elif Board[RowCount][ColumnCount] != Board[StartRow][StartColumn]:
      OpponentPieceFound = True
    elif Board[RowCount][ColumnCount] == Board[StartRow][StartColumn] and not OpponentPieceFound:
      FlipStillPossible = False
    else:
      FlipFound = True
    RowCount = RowCount + RowDirection
    ColumnCount = ColumnCount + ColumnDirection
  return FlipFound

# Actually flip the pieces by looping through the column&row given
def FlipOpponentPiecesInOneDirection(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection):
  FlipFound = CheckIfThereArePiecesToFlip(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection)
  if FlipFound:
    RowCount = StartRow + RowDirection
    ColumnCount = StartColumn + ColumnDirection
    while Board[RowCount][ColumnCount] != " " and Board[RowCount][ColumnCount] != Board[StartRow][StartColumn]:
      if Board[RowCount][ColumnCount] == "H":
        Board[RowCount][ColumnCount] = "C"
      else:
        Board[RowCount][ColumnCount] = "H"
      RowCount = RowCount + RowDirection
      ColumnCount = ColumnCount + ColumnDirection

# Have either the player or the computer decide where to make a move and place the pawn down, and then flip any available pawn
def MakeMove(Board, BoardSize, Move, HumanPlayersTurn):
  Row = Move % 10
  Column = Move // 10
  if HumanPlayersTurn:
    Board[Row][Column] = "H"
  else:
    Board[Row][Column] = "C"
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 1, 0)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, -1, 0)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 0, 1)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 0, -1)

# Displays the lines in the board
def PrintLine(BoardSize):
  print("   ", end="")
  for Count in range(1, BoardSize * 2):
    print("_", end="")
  print()

# Displays the acutal board
def DisplayGameBoard(Board, BoardSize):
  print()
  print("  ", end="")
  for Column in range(1, BoardSize + 1):
    print(" ", end="")
    print(Column, end="")
  print()
  PrintLine(BoardSize)
  for Row in range(1, BoardSize + 1):
    print(Row, end="")
    print(" ", end="")
    for Column in range(1, BoardSize + 1):
      print("|", end="")
      print(Board[Row][Column], end="")
    print("|")
    PrintLine(BoardSize)
    print()

# Displays the menu
def DisplayMenu():
  print("(p)lay game")
  print("(e)nter name")
  print("(c)hange board size")
  print("(q)uit")
  print()

# Take the user's input for the user's choice in the menu
def GetMenuChoice(PlayerName):
  print(PlayerName, "enter the letter of your chosen option: ", end="")
  Choice = input()
  return Choice

# Create a list to store the board used in the game
def CreateBoard():
  Board = []
  for Count in range(BoardSize + 1):
    Board.append([])
    for Count2 in range(BoardSize + 1):
      Board[Count].append("")
  return Board

# The main function of the game process, after setting up the board by using several functions,
# let the computer and player take moves until the board is full,
# and then check who won and display a message indicating the winner or draw
def PlayGame(PlayerName, BoardSize):
  Board = CreateBoard()
  SetUpGameBoard(Board, BoardSize)
  HumanPlayersTurn = False
  while not GameOver(Board, BoardSize):
    HumanPlayersTurn = not HumanPlayersTurn
    DisplayGameBoard(Board, BoardSize)
    MoveIsValid = False
    while not MoveIsValid:
      if HumanPlayersTurn:
        Move = GetHumanPlayerMove(PlayerName)
      else:
        Move = GetComputerPlayerMove(BoardSize)
      MoveIsValid = CheckIfMoveIsValid(Board, Move)
    if not HumanPlayersTurn:
      print("Press the Enter key and the computer will make its move")
      input()
    MakeMove(Board, BoardSize, Move, HumanPlayersTurn)
  DisplayGameBoard(Board, BoardSize)
  HumanPlayerScore = GetPlayerScore(Board, BoardSize, "H")
  ComputerPlayerScore = GetPlayerScore(Board, BoardSize, "C")
  if HumanPlayerScore > ComputerPlayerScore:
    print("Well done", PlayerName, ", you have won the game!")
  elif HumanPlayerScore == ComputerPlayerScore:
    print("That was a draw!")
  else:
    print("The computer has won the game!")
  print()

# Set up the seed used to random generate an integer for the computer's move
random.seed()
# Default size of the board
BoardSize = 6
# Declare variables
PlayerName = ""
Choice = ""
# Main menu process
while Choice != "q":
  DisplayMenu()
  Choice = GetMenuChoice(PlayerName)
  if Choice == "p":
    PlayGame(PlayerName, BoardSize)
  elif Choice == "e":
    PlayerName = GetPlayersName()
  elif Choice == "c":
    BoardSize = ChangeBoardSize()
