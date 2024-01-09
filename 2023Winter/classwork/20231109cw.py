class Wagon():

    def __init__(self, ownerName: str, weight: float, numberOfWheels: int):
        self._ownerName = ownerName
        self._weight = weight
        self._numberOfWheels = numberOfWheels
    
    def getOwnerName(self):
        return self._ownerName
    
    def getWeight(self):
        return self._weight
    
    def getNumberOfWheels(self):
        return self._numberOfWheels

class OpenWagen(Wagon):
    pass

class ClosedWagon(Wagon):

    def __init__(self, ownerName: str, weight: float, height: float, numberOfWheels: int, numberOfDoors: int, suitableForFoodStuffs: bool):
        self._ownerName = ownerName
        self._weight = weight
        self._height = height
        self._numberOfWheels = numberOfWheels
        self._numberOfDoors = numberOfDoors
        self._suitableForFoodStuffs = suitableForFoodStuffs
    
    def getHeight(self):
        return self._height
    
    def getNumberOfDoors(self):
        return self._numberOfDoors
    
    def getSuitableForFoodStuffs(self):
        return self._suitableForFoodStuffs

class Slidings():

    def __init__(self):
        self._wagons = [None] * 30
        self._topOfStackPointer = -1
    
    def isEmpty(self):
        return (self._topOfStackPointer == -1)

    def isFull(self):
        return (self._topOfStackPointer == 29)

    def push(self, pushContent: Wagon):
        if not(self.isFull()):
            self._topOfStackPointer += 1
            self._wagons[self._topOfStackPointer] = pushContent
        else:
            raise Exception("The sliding is full, failed to push onto it.")

    def pop(self):
        if not(self.isEmpty()):
            returnWagon = self._wagons[self._topOfStackPointer]
            self._wagons[self._topOfStackPointer] = None
            self._topOfStackPointer -= 1
            return returnWagon
        else:
            raise Exception("The sliding is empty, failed to pop from it.")
    
    def checkTop(self):
        if self.isEmpty():
            return None
        else:
            return (self._wagons[self._topOfStackPointer])

class Yard():
    
    def __init__(self, numberOfSlidings: int):
        self._numberOfSlidings = numberOfSlidings
        self._slidings = [Slidings()] * numberOfSlidings
    
    def addWagon(self, slidingID: int, newWagon: Wagon):
        if slidingID < len(self._slidings):
            self._slidings[slidingID].push(newWagon)
        else:
            raise Exception("Invalid sliding ID, failed to add wagon to it.")
    
    def removeWagon(self, slidingID: int):
        if slidingID < len(self._slidings):
            return self._slidings[slidingID].pop()
        else:
            raise Exception("Invalid sliding ID, failed to remove wagon from it.")
    
    def getWagon(self, slidingID: int):
        if slidingID < len(self._slidings):
            return self._slidings[slidingID].checkTop()
        else:
            raise Exception("Invalid sliding ID, failed to get wagon from it.")
    
    def showAllWagon(self, slidingID):
        if slidingID < len(self._slidings):
            for wagon in self._slidings[slidingID]._wagons:
                if not(wagon == None):
                    print(wagon.getOwnerName())
        else:
            raise Exception("Invalid sliding ID, failed show wagons.")

if __name__ == "__main__":
    testYard = Yard(5)
    testYard.addWagon(0, OpenWagen("James G", 3.0, 12))
    testYard.addWagon(0, OpenWagen("James I", 2.0, 9))
    testYard.addWagon(0, ClosedWagon("Guan James", 2.0, 10.0, 16, 4, True))
    for i in range(27):
        testYard.addWagon(0, OpenWagen(f"PLACEHOLDER{i}", 5.5, 6))
    #testYard.addWagon(0, Wagon("PLACEHOLDER114514", 2.0, 12)) # This will raise an exception as the sliding is full
    for i in range(30):
        print(testYard.removeWagon(0).getOwnerName())
    #testYard.removeWagon(1) # This will raise an exception as sliding 1 in yard testYard is empty