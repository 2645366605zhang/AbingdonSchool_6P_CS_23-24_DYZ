import random
import platform
import copy

class Board():

    def __init__(self, size: int) -> None:
        self._size = size
        self._boardList = [[" " for _ in range(size)] for _ in range(size)]
    
    def __str__(self) -> list:
        return self._boardList

    def objectPresent(self, id: int) -> bool:
        return (self._boardList[id // self._size][id % self._size] != " ")
    
    def getObject(self, id: int) -> str:
        return (self._boardList[id // self._size][id % self._size])

class KCBoard(Board):

    def __init__(self, playerName: str) -> None:
        self._size = 3
        self._objectPalette = ["O", "X"]
        self._boardList = [[" " for _ in range(3)] for _ in range(3)]
        self._availablePosition = [[[0, 8], [1, 2], [2, 8]], [[3, 2], [4, 32], [5, 2]], [[6, 8], [7, 2], [8, 8]]]
        self._objectPresent = 0
        self._playerName = playerName
        self._aiName = platform.processor()
    
    def display(self) -> None:
        print(f"""
Player 0: {self._playerName}
Player 1: {self._aiName}

 {self.getObject(0)} | {self.getObject(1)} | {self.getObject(2)}
---+---+---
 {self.getObject(3)} | {self.getObject(4)} | {self.getObject(5)}
---+---+---
 {self.getObject(6)} | {self.getObject(7)} | {self.getObject(8)}
""")

    def displayWithMap(self) -> None:
        print(f"""
Player 0: {self._playerName}
Player 1: {self._aiName}

 {self.getObject(0)} | {self.getObject(1)} | {self.getObject(2)}           0 | 1 | 2
---+---+---         ---+---+---
 {self.getObject(3)} | {self.getObject(4)} | {self.getObject(5)}           3 | 4 | 5
---+---+---         ---+---+---
 {self.getObject(6)} | {self.getObject(7)} | {self.getObject(8)}           6 | 7 | 8
""")
    
    def updateWeight(self):
        for index in range(self._size ** 2):
            if self._availablePosition[index // self._size][index % self._size][1] != 0:
                if self.checkIfWin(index) == self._aiName:
                    self._availablePosition[index // self._size][index % self._size][1] += 512
                if self.checkIfWin(index) == self._playerName:
                    self._availablePosition[index // self._size][index % self._size][1] += 128

    def placeObject(self, object: str, id: int) -> str:
        self._boardList[id // self._size][id % self._size] = object
        self._availablePosition[id // self._size][id % self._size][1] = 0
        return object

    def playerTurn(self) -> str:
        validInput = False
        while not(validInput):
            try:
                placeID = int(input(f"Please enter the integer ID of the place you want to place."))
                if not(placeID in range(self._size ** 2)):
                    print("Invalid ID, please try again.")
                elif self.objectPresent(placeID):
                    print(f"Object {self.getObject(placeID)} is already at this position, please try again.")
                else:
                    validInput = True
            except ValueError:
                print("Not an integer, please try again.")
        self.placeObject(self._objectPalette[0], placeID)
        self._objectPresent += 1
        return (f"\n{self._playerName} placed {self._objectPalette[0]} at {placeID}!\n")
    
    def playerAiTurn(self) -> str:
        validInput = False
        while not(validInput):
            try:
                placeID = int(input(f"Please enter the integer ID of the place you want to place."))
                if not(placeID in range(self._size ** 2)):
                    print("Invalid ID, please try again.")
                elif self.objectPresent(placeID):
                    print(f"Object {self.getObject(placeID)} is already at this position, please try again.")
                else:
                    validInput = True
            except ValueError:
                print("Not an integer, please try again.")
        self.placeObject(self._objectPalette[1], placeID)
        self._objectPresent += 1
        return (f"\n{self._playerName} placed {self._objectPalette[0]} at {placeID}!\n")

    def aiTurn(self) -> str:
        targetID = random.randint(1, (self._size ** 2)) - 1
        while self.objectPresent(targetID):
            targetID = random.randint(1, (self._size ** 2)) - 1
        self.placeObject(self._objectPalette[1], targetID)
        self._objectPresent += 1
        return (f"\n{self._aiName} placed {self._objectPalette[1]} at {targetID}!\n")
    
    def newAiTurn(self) -> str:
        self.updateWeight()
        # Generate weight
        totalWeight = 0
        lastWeightBoundary = 0
        weightList = []
        for row in self._availablePosition:
            for column in row:
                if column[1] != 0:
                    lastWeightBoundary = totalWeight
                    totalWeight += column[1]
                    weightList.append([column[0], lastWeightBoundary, totalWeight - 1])
        # Choose
        weightSeed = random.randint(0, totalWeight - 1)
        for position in weightList:
            if weightSeed in range(position[1], position[2] + 1):
                targetID = position[0]
                break
        print(f"\nrandomseed: {weightSeed}\nweightlist: {weightList}") # Debug Mode
        # Place
        self.placeObject(self._objectPalette[1], targetID)
        self._objectPresent += 1
        return (f"\n{self._aiName} placed {self._objectPalette[1]} at {targetID}!\n")

    def checkDraw(self) -> bool:
        if self._objectPresent < (self._size ** 2):
            return False
        elif (self._objectPresent >= (self._size ** 2)) and (self.checkWin() != None):
            return False
        else:
            return True
    
    def checkIfWin(self, id: int):
        testBoardList_O = copy.deepcopy(self._boardList)
        testBoardList_X = copy.deepcopy(self._boardList)
        testBoardList_O[id // self._size][id % self._size] = "O"
        testBoardList_X[id // self._size][id % self._size] = "X"
        # O
        # Same horizontally
        for row in testBoardList_O:
            if all(space == "O" for space in row):
                return self._playerName
            elif all(space == "X" for space in row):
                return self._aiName
        # Same vertically
        for index in range(self._size):
            if ((testBoardList_O[index // self._size][index % self._size])) == (testBoardList_O[(index + self._size) // self._size][(index + self._size) % self._size]) == (testBoardList_O[(index + (self._size * 2)) // self._size][(index + (self._size * 2)) % self._size]):
                if (self._boardList[index // self._size][index % self._size]) == "O":
                    return self._playerName
                elif (self._boardList[index // self._size][index % self._size]) == "X":
                    return self._aiName
        # Same across
        if (testBoardList_O[0][0] == testBoardList_O[1][1] == testBoardList_O[2][2]) or (testBoardList_O[0][2] == testBoardList_O[1][1] == testBoardList_O[2][0]):
            if testBoardList_O[1][1] == "O":
                return self._playerName
            elif testBoardList_O[1][1] == "X":
                return self._aiName
        # X
        # Same horizontally
        for row in testBoardList_X:
            if all(object == "O" for space in row):
                return self._playerName
            elif all(object == "X" for space in row):
                return self._aiName
        # Same vertically
        for index in range(self._size):
            if ((testBoardList_X[index // self._size][index % self._size])) == (testBoardList_X[(index + self._size) // self._size][(index + self._size) % self._size]) == (testBoardList_X[(index + (self._size * 2)) // self._size][(index + (self._size * 2)) % self._size]):
                if (self._boardList[index // self._size][index % self._size]) == "O":
                    return self._playerName
                elif (self._boardList[index // self._size][index % self._size]) == "X":
                    return self._aiName
        # Same across
        if (testBoardList_X[0][0] == testBoardList_X[1][1] == testBoardList_X[2][2]) or (testBoardList_X[0][2] == testBoardList_X[1][1] == testBoardList_X[2][0]):
            if testBoardList_X[1][1] == "O":
                return self._playerName
            elif testBoardList_X[1][1] == "X":
                return self._aiName
        return None

    def checkWin(self):
        # Same horizontally
        for row in self._boardList:
            if all(space == "O" for space in row):
                return self._playerName
            elif all(space == "X" for space in row):
                return self._aiName
        # Same vertically
        for index in range(self._size):
            if (self.getObject(index)) == (self.getObject(index + self._size)) == (self.getObject(index + (self._size * 2))):
                if self.getObject(index) == "O":
                    return self._playerName
                elif self.getObject(index) == "X":
                    return self._aiName
        # Same across
        if (self._boardList[0][0] == self._boardList[1][1] == self._boardList[2][2]) or (self._boardList[0][2] == self._boardList[1][1] == self._boardList[2][0]):
            if self.getObject(4) == "O":
                return self._playerName
            elif self.getObject(4) == "X":
                return self._aiName
        return None

if __name__ == "__main__":
    myboard = KCBoard("Tester")
    myboard.placeObject(myboard._objectPalette[0], 0)
    myboard.placeObject(myboard._objectPalette[0], 1)
    print(myboard.checkIfWin(2))