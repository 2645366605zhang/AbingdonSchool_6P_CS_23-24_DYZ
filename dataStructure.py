# Imports

from __future__ import annotations
import math

# Empty

class Empty(Exception):
    pass

# Data Structure

class ArrayQueue:

    def __init__(self, maxLength):
        self._data = []
        self._maxLength = maxLength

    def __len__(self):
        return len(self._data)
    
    def display(self):
        for element in self._data:
            print(element)
    
    def isEmpty(self):
        return len(self._data) == 0
    
    def isFull(self):
        return len(self._data) == self._maxLength
    
    def add(self, element):
        if len(self._data) <= self._maxLength:
            self._data.append(element)
        else:
            print("Queue is full")

    def remove(self):
        if self.isEmpty():
            raise Empty("Queue is empty")
        return self._data.pop(0)
    
    def top(self):
        if self.isEmpty():
            raise Empty("Queue is empty")
        return self._data[-1]
    
    def bottom(self):
        if self.isEmpty():
            raise Empty("Queue is empty")
        return self._data[0]
    
class ArrayCircularQueue:

    def __init__(self, maxLength):
        self._data = []
        for loopCount in range(maxLength):
            self._data.append(None)
        self._maxLength = maxLength
        self._pointerFront = -1
        self._pointerRear = -1

    def __str__(self):
        return str(self._data)
    
    def isEmpty(self):
        return (self._pointerFront == -1) and (self._pointerRear == -1)
    
    def isFull(self):
        return ((self._pointerRear + 1) % self._maxLength) == self._pointerFront
    
    def add(self, element):
        if self.isEmpty():
            self._pointerFront = 0
            self._pointerRear = 0
            self._data[self._pointerRear] = element
        elif self.isFull():
            print("Queue is full")
        else:
            self._pointerRear = ((self._pointerRear + 1) % self._maxLength)
            self._data[self._pointerRear] = element

    def remove(self):
        if self.isEmpty():
            raise Empty("Queue is empty")
        else:
            self._data.pop(self._pointerFront)
            if self._pointerFront == self._pointerRear:
                self._pointerFront = -1
                self._pointerRear = -1
            else:
                self._pointerFront = ((self._pointerFront + 1) % self._maxLength)

class Node:

    def __init__(self, data, nextNode: Node | None):
        self._data = data
        self._nextNode = nextNode
    
    def getData(self):
        return (self._data)
    
    def getNextNode(self):
        return (self._nextNode)
    
    def setData(self, newData):
        self._data = newData
    
    def setNextNode(self, newNode: Node | None):
        self._nextNode = newNode

class LinkedListStack:

    def __init__(self, headNodeData, maxSize: int = -1, safeMode: bool | None = False): # Set maxSize to -1 to make it infinite, set safeMode to True to remove all exception raised
        self._size = 1
        self._maxSize = maxSize
        self._headNode = Node(headNodeData, None)
        self._safeMode = safeMode

    def __len__(self) -> int:
        return self._size
    
    def __str__(self) -> str:
        lLString = "["
        currentNode = self._headNode
        while currentNode:
            lLString += (f"{currentNode.getData()}, ")
            currentNode = currentNode.getNextNode()
        lLString += "\b\b]"
        return lLString

    def pop(self):
        if len(self) > 0:
            returnData = self._headNode.getData()
            self._headNode = self._headNode.getNextNode()
            self._size -= 1
            return returnData
        elif self._safeMode:
            print("Failed to pop from the linked list since it is empty.")
        else:
            raise Exception("Failed to pop from the linked list since it is empty.")

    def push(self, data):
        if (len(self) < self._maxSize) or (self._maxSize == -1):
            newNode = Node(data, self._headNode)
            self._headNode = newNode
            self._size += 1
        elif self._safeMode:
            print(f'Failed to push "{data}" to the linked list since it is full.')
        else:
            raise Exception(f'Failed to push "{data}" to the linked list since it is full.')
    
    def isEmpty(self):
            return (self._size == 0)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self._headNode
    
    def getList(self):
        currentNode = self._headNode
        dataList = []
        while currentNode:
            dataList.append(currentNode.getData())
            currentNode = currentNode.getNextNode()
        return dataList

# Geometry

class Rectangle:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getPerimeter(self):
        return (2 * self._x + 2 * self._y)
    
    def getArea(self):
        return (round((self._x * self._y), 3))

    def getDiagonal(self):
        return (round((math.sqrt(self._x ** 2 + self._y ** 2)), 3))
    
    def getData(self):
        dataList = [(self.getPerimeter()), (self.getArea()), (self.getDiagonal())]
        return dataList

    def __str__(self):
        return (f"The perimeter of this rectangle is {self.getPerimeter()}.\nThe area of this triangle is {self.getArea()}.\nThe diagonal length of this triangle is {self.getDiagonal()}.")
 
class VectorValue: # For all "Magic Methods" check https://python-course.eu/oop/magic-methods.php .

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, otherVector):
        resultVector = VectorValue(self._x, self._y, self._z)
        resultVector._x += otherVector._x
        resultVector._y += otherVector._y
        resultVector._z += otherVector._z
        return resultVector

    def __sub__(self, otherVector):
        resultVector = VectorValue(self._x, self._y, self._z)
        resultVector._x -= otherVector._x
        resultVector._y -= otherVector._y
        resultVector._z -= otherVector._z
        return resultVector

    def __str__(self):
        return (f"({self._x}, {self._y}, {self._z})")

    def __mul__(self, otherVector):
        if (type(otherVector) in [int, float]):
            return (VectorValue((self._x * otherVector), (self._y * otherVector), (self._z * otherVector)))
        else:
            return (VectorValue(((self._y * otherVector._z) - (self._z * otherVector._y)), ((self._z * otherVector._x) - (self._x * otherVector._z)), ((self._x * otherVector._y) - (self._y * otherVector._z))))

    def __rmul__(self, otherVector):
        if (type(otherVector) in [int, float]):
            return (VectorValue((self._x * otherVector), (self._y * otherVector), (self._z * otherVector)))
        else:
            return (VectorValue(((self._y * otherVector._z) - (self._z * otherVector._y)), ((self._z * otherVector._x) - (self._x * otherVector._z)), ((self._x * otherVector._y) - (self._y * otherVector._z))))

    def magnitude(self):
        return (math.sqrt((math.sqrt((self._x ** 2) + (self._y ** 2)) ** 2) + (self._z ** 2)))
