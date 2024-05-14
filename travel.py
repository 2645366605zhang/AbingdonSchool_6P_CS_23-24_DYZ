# IMPORTS

from __future__ import annotations
import os
from math import sqrt, pi
from code_repo.dataStructure import GraphNode as Node
from code_repo.locationLevel import LocationLevel, locationLevels

# CONSTANTS

# CLASSES

class InterFace:

    def __init__(self) -> None:
        self.Main()

    def Main(self) -> None:
        while True:
            pass
    
    def ShowStart(self) -> None:
        pass

    def ShowMapMenu(self) -> None:
        pass

    def CreateMap(self) -> None:
        pass

    def SaveMap(self) -> None:
        pass

    def LoadMap(self) -> None:
        pass

class Person:

    def __init__(self, position: int, name: str, symbol: str) -> None:
        self._position = position
        self._name = name
        self._symbol = symbol

    def GetName(self) -> str:
        return self._name
    
    def GetSymbol(self) -> str:
        return self._symbol
    
    def GetPosition(self) -> int:
        return self._position
    
    def moveTo(self, position) -> int:
        self._position = position
        return self._position

class TravelMap:

    def __init__(self, name: str) -> None:
        self._name = name
        self._locationList = []
    
    def GetName(self) -> str:
        return self._name
    
    def GetNumberOfLocation(self) -> int:
        return len(self._locationList)
    
    def GetLocation(self, index: int) -> Location:
        return self._locationList[index]
    
    def AddLocation(self, name: str = "Default", levelIdentifier: str = "NML") -> int: # Add a "Location" onto the map
        if name == "Default":
            name = f"Location{self.GetNumberOfLocation()}"
        self._locationList.append(Location(name, levelIdentifier))
        return (self.GetNumberOfLocation() - 1)
    
    def LinkLocation(self, locationIndex0: int, locationIndex1: int, distance: float) -> None: # Connect two "Locations"
        self.GetLocation(locationIndex0).AddRoute(self.GetLocation(locationIndex1), distance)
    
    def SetLevel(self, index: int, levelIdentifier: str) -> None:
        self.GetLocation(index).UpdateLevel(levelIdentifier)
    
    def Navigate(self, locationIndex0: int, locationIndex1: int) -> list: # Find out the distance between two "Locations", return the distance and the route(with all "Locations in between")
        distances = [float('inf')] * self.GetNumberOfLocation()
        predecessors = [None] * self.GetNumberOfLocation()
        distances[locationIndex0] = 0
        visited = [False] * self.GetNumberOfLocation()

        for i in range(self.GetNumberOfLocation()):
            minDistance = float('inf')
            u = None
            for index in range(self.GetNumberOfLocation()):
                if not(visited[index]) and (distances[index] < minDistance):
                    minDistance = distances[index]
                    u = index
            if (u is None) or (u == locationIndex1):
                break
            visited[u] = True
            for v in range(self.GetNumberOfLocation()):
                if (self.GetLocation(u).CheckRoute(self.GetLocation(v)) != None) and not(visited[v]):
                    alt = distances[u] + self.GetLocation(u).CheckRoute(self.GetLocation(v))
                    if alt < distances[v]:
                        distances[v] = alt
                        predecessors[v] = u
        
        path = []
        pathID = []
        current = locationIndex1
        while current is not None:
            path.insert(0, str(self.GetLocation(current)))
            pathID.insert(0, current)
            current = predecessors[current]
            if current == locationIndex0:
                path.insert(0, str(self.GetLocation(locationIndex0)))
                pathID.insert(0, locationIndex0)
                break
        path = " — ".join(path)

        return [distances[locationIndex1], path, pathID]

class CartesianMap(TravelMap):

    def __init__(self, name: str, xSize: int, ySize: int, distance: int | float) -> None:
        super().__init__(name)
        self._xSize = xSize
        self._ySize = ySize
        self._coordinateDistance = distance
        self._coordinateList = []
        self._personDict = {}
        for x in range(self._xSize):
            xLocationList = []
            for y in range(self._ySize):
                xLocationList.append(self.GetNumberOfLocation())
                self.AddLocation(f"[{self.GetNumberOfLocation()}]: {x}, {y}", "GND")
            self._coordinateList.append(xLocationList)
        self._maxDigit = 1
        for x in range(self._xSize):
            for y in range(self._ySize):
                if len(str(self._coordinateList[x][y])) > self._maxDigit:
                    self._maxDigit = len(str(self._coordinateList[x][y]))
        self.UpdateLink()
    
    def UpdateLink(self) -> None:
        # Clear all routes between all Locations
        for x in range(self._xSize):
            for y in range(self._ySize):
                self.GetLocation(self._coordinateList[x][y]).ClearLocalRoute()
        # Links every Location with the 8 other Locations around it
        for x in range(self._xSize):
            for y in range(self._ySize):
                if x != 0:
                    try: # Left of this Location
                        if self.GetLocation(self._coordinateList[x][y]).CheckRoute(self.GetLocation(self._coordinateList[x - 1][y])) == None:
                            self.LinkLocation(self._coordinateList[x][y], self._coordinateList[x - 1][y], self._coordinateDistance)
                    except IndexError:
                        print(f"Coordinate {x}, {y} has index out of range, skip\n")
                    try: # Top left of this Location
                        if self.GetLocation(self._coordinateList[x][y]).CheckRoute(self.GetLocation(self._coordinateList[x - 1][y + 1])) == None:
                            self.LinkLocation(self._coordinateList[x][y], self._coordinateList[x - 1][y + 1], sqrt(2 * (self._coordinateDistance ** 2)))
                    except IndexError:
                        print(f"Coordinate {x}, {y} has index out of range, skip\n")
                if y != 0:
                    try: # Bottom of this Location
                        if self.GetLocation(self._coordinateList[x][y]).CheckRoute(self.GetLocation(self._coordinateList[x][y - 1])) == None:
                            self.LinkLocation(self._coordinateList[x][y], self._coordinateList[x][y - 1], self._coordinateDistance)
                    except IndexError:
                        print(f"Coordinate {x}, {y} has index out of range, skip\n")
                    try: # Bottom right of this Location
                        if self.GetLocation(self._coordinateList[x][y]).CheckRoute(self.GetLocation(self._coordinateList[x + 1][y - 1])) == None:
                            self.LinkLocation(self._coordinateList[x][y], self._coordinateList[x + 1][y - 1], sqrt(2 * (self._coordinateDistance ** 2)))
                    except IndexError:
                        print(f"Coordinate {x}, {y} has index out of range, skip\n")
                if x != 0 and y != 0:
                    try: # Bottom left of this Location
                        if self.GetLocation(self._coordinateList[x][y]).CheckRoute(self.GetLocation(self._coordinateList[x - 1][y - 1])) == None:
                            self.LinkLocation(self._coordinateList[x][y], self._coordinateList[x - 1][y - 1], sqrt(2 * (self._coordinateDistance ** 2)))
                    except IndexError:
                        print(f"Coordinate {x}, {y} has index out of range, skip\n")
                try: # Top right of this Location
                    if self.GetLocation(self._coordinateList[x][y]).CheckRoute(self.GetLocation(self._coordinateList[x + 1][y + 1])) == None:
                        self.LinkLocation(self._coordinateList[x][y], self._coordinateList[x + 1][y + 1], sqrt(2 * (self._coordinateDistance ** 2)))
                except IndexError:
                    print(f"Coordinate {x}, {y} has index out of range, skip\n")
                try: # Right of this Location
                    if self.GetLocation(self._coordinateList[x][y]).CheckRoute(self.GetLocation(self._coordinateList[x + 1][y])) == None:
                        self.LinkLocation(self._coordinateList[x][y], self._coordinateList[x + 1][y], self._coordinateDistance)
                except IndexError:
                    print(f"Coordinate {x}, {y} has index out of range, skip\n")
                try: # Top of this Location
                    if self.GetLocation(self._coordinateList[x][y]).CheckRoute(self.GetLocation(self._coordinateList[x][y + 1])) == None:
                        self.LinkLocation(self._coordinateList[x][y], self._coordinateList[x][y + 1], self._coordinateDistance)
                except IndexError:
                    print(f"Coordinate {x}, {y} has index out of range, skip\n")
    
    def GetCoordString(self) -> str:
        mapStringList = []
        seperatorH = "—" * (self._maxDigit + 2)
        seperatorV = "|"
        seperatorC = "|"
        for y in range(self._ySize):
            lineList = []
            for x in range(self._xSize):
                lineList.append(f"{f"{self._coordinateList[x][y]}":^{self._maxDigit + 2}}")
            mapStringList.insert(0, f"{seperatorV}".join(lineList))
        return f"\n{f"{seperatorH}{seperatorC}" * (self._xSize - 1)}{seperatorH}\n".join(mapStringList)
    
    def GetLocString(self) -> str:
        mapStringList = []
        seperatorH = "—" * (self._maxDigit + 2)
        seperatorV = "|"
        seperatorC = "|"
        for y in range(self._ySize):
            lineList = []
            for x in range(self._xSize):
                lineList.append(f"{f"{self.GetLocation(self._coordinateList[x][y]).GetLevel().GetLocalization()}":^{self._maxDigit + 2}}")
            mapStringList.insert(0, f"{seperatorV}".join(lineList))
        return f"\n{f"{seperatorH}{seperatorC}" * (self._xSize - 1)}{seperatorH}\n".join(mapStringList)
    
    def GetPersonString(self) -> str:
        mapStringList = []
        seperatorH = "—" * (self._maxDigit + 2)
        seperatorV = "|"
        seperatorC = "|"
        for y in range(self._ySize):
            lineList = []
            for x in range(self._xSize):
                lineList.append(f"{f"{self.GetPerson(self._coordinateList[x][y]).GetSymbol()}":^{self._maxDigit + 2}}")
            mapStringList.insert(0, f"{seperatorV}".join(lineList))
        return f"\n{f"{seperatorH}{seperatorC}" * (self._xSize - 1)}{seperatorH}\n".join(mapStringList)
    
    def LinkLocation(self, locationIndex0: int, locationIndex1: int, distance: float) -> None:
        if self.GetLocation(locationIndex0).GetLevel().GetLocalization() != "▓" and self.GetLocation(locationIndex1).GetLevel().GetLocalization() != "▓":
            if self.GetLocation(locationIndex0).GetLevel().GetLocalization() == "▒" or self.GetLocation(locationIndex1).GetLevel().GetLocalization() == "▒":
                self.GetLocation(locationIndex0).AddRoute(self.GetLocation(locationIndex1), distance * 1.5)
            else:
                self.GetLocation(locationIndex0).AddRoute(self.GetLocation(locationIndex1), distance)
        else:
            self.GetLocation(locationIndex0).AddRoute(self.GetLocation(locationIndex1), float('inf'))
    
    def SetLevel(self, index: int, levelIdentifier: str) -> None:
        super().SetLevel(index, levelIdentifier)
        self.UpdateLink()

    def AddPerson(self, position: int, name: str, symbol: str):
        self._personDict[position] = Person(position, name, symbol)
        print(self._personDict)
    
    def GetNumberOfPerson(self) -> int:
        return len(self._personDict)
    
    def GetPerson(self, coordIndex: int) -> Person:
        if coordIndex in self._personDict:
            return self._personDict[coordIndex]
        else:
            return Person(-1, "Null", "")
    
    def MovePerson(self, personCoordIndex: int, destCoordIndex: int):
        self._personDict[self.GetPerson(personCoordIndex).moveTo(destCoordIndex)] = self.GetPerson(personCoordIndex)
        del self._personDict[personCoordIndex]

class Location(Node):

    def __init__(self, name: str, levelIdentifier: str) -> None:
        super().__init__(name)
        self._level = locationLevels[levelIdentifier]

    def GetLevel(self) -> LocationLevel:
        return self._level
    
    def AddRoute(self, node: Location, distance: float) -> None:
        self.links[node] = distance
        node.links[self] = distance
    
    def ClearLocalRoute(self) -> None:
        self.links = {}

    def CheckRoute(self, node: Location) -> float:
        return self.links.get(node, None)
    
    def UpdateLevel(self, levelIdentifier: str) -> None:
        self._level = locationLevels[levelIdentifier]

# FUNCTIONS

def Main():
    pass

# MAIN

Main()

# TEST

if __name__ == "__main__":
    """testMap = TravelMap("Abingdon School")
    testMap.AddLocation("Amey Theatre") # 0
    testMap.AddLocation("Big School") # 1
    testMap.AddLocation("Cresent House") # 2
    testMap.AddLocation("DT Department") # 3
    testMap.AddLocation("Economics Classroom") # 4
    testMap.AddLocation("Faringdon Lodge") # 5
    testMap.AddLocation("Greening Court") # 6
    testMap.LinkLocation(0, 1, 2)
    testMap.LinkLocation(0, 3, 3)
    testMap.LinkLocation(3, 6, 1)
    testMap.LinkLocation(4, 5, 1)
    testMap.LinkLocation(1, 4, 4)
    testMap.LinkLocation(1, 5, 3)
    testMap.LinkLocation(2, 5, 2.5)
    navigationResult = testMap.Navigate(0, 6)
    print(f'In map "{testMap.GetName()}", such route exists:\nRoute Length: {round(navigationResult[0], 2)}\nRoute Detail: {navigationResult[1]}')"""

    testMap = CartesianMap("CMap", 4, 5, 1)
    testMap.SetLevel(6, "WAL")
    testMap.SetLevel(7, "WAL")
    testMap.SetLevel(8, "COV")
    testMap.SetLevel(11, "COV")
    startCoordinate = 1
    endCoordinate = 19
    testMap.AddPerson(startCoordinate, "PLACEHOLDER", "P")
    navigationResult = testMap.Navigate(startCoordinate, endCoordinate)
    print(f'In map "{testMap.GetName()}", such route exists:\nRoute Length: {round(navigationResult[0], 2)}\nRoute Detail: {navigationResult[1]}')
    print(f"Raw PathID: {navigationResult[2]}")
    print(f"\n{testMap.GetCoordString()}\n")
    print(f"\n{testMap.GetLocString()}\n")
    print(f"Move From:\n{testMap.GetPersonString()}\n")
    testMap.MovePerson(startCoordinate, endCoordinate)
    print(f"To:\n{testMap.GetPersonString()}\n")