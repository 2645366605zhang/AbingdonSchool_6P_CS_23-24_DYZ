# Imports
from __future__ import annotations
import math
from typing import Any, Optional

# Empty
class Empty(Exception):
    pass

# Data Structure

class ArrayQueue:
    def __init__(self, maxLength: int) -> None:
        self._data: list[Any] = []
        self._maxLength: int = maxLength

    def __len__(self) -> int:
        return len(self._data)
    
    def display(self) -> None:
        for element in self._data:
            print(element)
    
    def isEmpty(self) -> bool:
        return len(self._data) == 0
    
    def isFull(self) -> bool:
        return len(self._data) == self._maxLength
    
    def add(self, element: Any) -> None:
        if len(self._data) <= self._maxLength:
            self._data.append(element)
        else:
            print("Queue is full")

    def remove(self) -> Any:
        if self.isEmpty():
            raise Empty("Queue is empty")
        return self._data.pop(0)
    
    def top(self) -> Any:
        if self.isEmpty():
            raise Empty("Queue is empty")
        return self._data[-1]
    
    def bottom(self) -> Any:
        if self.isEmpty():
            raise Empty("Queue is empty")
        return self._data[0]

class ArrayCircularQueue:
    def __init__(self, maxLength: int) -> None:
        self._data: list[Optional[Any]] = [None] * maxLength
        self._maxLength: int = maxLength
        self._pointerFront: int = -1
        self._pointerRear: int = -1

    def __str__(self) -> str:
        return str(self._data)
    
    def isEmpty(self) -> bool:
        return (self._pointerFront == -1) and (self._pointerRear == -1)
    
    def isFull(self) -> bool:
        return ((self._pointerRear + 1) % self._maxLength) == self._pointerFront
    
    def add(self, element: Any) -> None:
        if self.isEmpty():
            self._pointerFront = 0
            self._pointerRear = 0
            self._data[self._pointerRear] = element
        elif self.isFull():
            print("Queue is full")
        else:
            self._pointerRear = ((self._pointerRear + 1) % self._maxLength)
            self._data[self._pointerRear] = element

    def remove(self) -> Any:
        if self.isEmpty():
            raise Empty("Queue is empty")
        else:
            removed = self._data[self._pointerFront]
            self._data[self._pointerFront] = None  # Clear slot instead of pop to preserve circularity
            if self._pointerFront == self._pointerRear:
                self._pointerFront = -1
                self._pointerRear = -1
            else:
                self._pointerFront = ((self._pointerFront + 1) % self._maxLength)
            return removed

class Node:
    def __init__(self, data: Any, nextNode: Optional[Node]) -> None:
        self._data: Any = data
        self._nextNode: Optional[Node] = nextNode
    
    def getData(self) -> Any:
        return self._data
    
    def getNextNode(self) -> Optional[Node]:
        return self._nextNode
    
    def setData(self, newData: Any) -> None:
        self._data = newData
    
    def setNextNode(self, newNode: Optional[Node]) -> None:
        self._nextNode = newNode

class LinkedListStack:
    def __init__(self, headNodeData: Any, maxSize: int = -1, safeMode: bool = False) -> None:
        self._size: int = 1
        self._maxSize: int = maxSize
        self._headNode: Node = Node(headNodeData, None)
        self._safeMode: bool = safeMode

    def __len__(self) -> int:
        return self._size
    
    def __str__(self) -> str:
        lLString = "["
        currentNode = self._headNode
        while currentNode:
            lLString += f"{currentNode.getData()}, "
            currentNode = currentNode.getNextNode()
        return lLString.rstrip(", ") + "]" if self._size > 0 else "[]"

    def pop(self) -> Any:
        if len(self) > 0:
            returnData = self._headNode.getData()
            self._headNode = self._headNode.getNextNode()
            self._size -= 1
            return returnData
        elif self._safeMode:
            print("Failed to pop from the linked list since it is empty.")
        else:
            raise Exception("Failed to pop from the linked list since it is empty.")

    def push(self, data: Any) -> None:
        if (len(self) < self._maxSize) or (self._maxSize == -1):
            newNode = Node(data, self._headNode)
            self._headNode = newNode
            self._size += 1
        elif self._safeMode:
            print(f'Failed to push "{data}" to the linked list since it is full.')
        else:
            raise Exception(f'Failed to push "{data}" to the linked list since it is full.')
    
    def isEmpty(self) -> bool:
        return self._size == 0

    def peek(self) -> Optional[Node]:
        if self.isEmpty():
            return None
        return self._headNode
    
    def getList(self) -> list[Any]:
        currentNode = self._headNode
        dataList: list[Any] = []
        while currentNode:
            dataList.append(currentNode.getData())
            currentNode = currentNode.getNextNode()
        return dataList

class GraphNode:
    def __init__(self, name: str) -> None:
        self.links: dict[GraphNode, Any] = {}
        self.name: str = name

    def link(self, node: GraphNode, weight: Any) -> None:
        self.links[node] = weight
        node.links[self] = weight

    def unlink(self, node: GraphNode) -> bool:
        try:
            del self.links[node]
            del node.links[self]
        except KeyError:
            return False
        return True

    def connects(self, node: GraphNode) -> Optional[Any]:
        return self.links.get(node)

    def __str__(self) -> str:
        return self.name

    def __len__(self) -> int:
        return len(self.links)

# Geometry

class Rectangle:
    def __init__(self, x: float, y: float) -> None:
        self._x: float = x
        self._y: float = y

    def getPerimeter(self) -> float:
        return 2 * self._x + 2 * self._y
    
    def getArea(self) -> float:
        return round(self._x * self._y, 3)

    def getDiagonal(self) -> float:
        return round(math.sqrt(self._x ** 2 + self._y ** 2), 3)
    
    def getData(self) -> list[float]:
        return [self.getPerimeter(), self.getArea(), self.getDiagonal()]

    def __str__(self) -> str:
        return (f"The perimeter of this rectangle is {self.getPerimeter()}.\n"
                f"The area of this rectangle is {self.getArea()}.\n"
                f"The diagonal length of this rectangle is {self.getDiagonal()}.")
 
class VectorValue:
    def __init__(self, x: float, y: float, z: float) -> None:
        self._x: float = x
        self._y: float = y
        self._z: float = z

    def __add__(self, otherVector: 'VectorValue') -> 'VectorValue':
        resultVector = VectorValue(self._x, self._y, self._z)
        resultVector._x += otherVector._x
        resultVector._y += otherVector._y
        resultVector._z += otherVector._z
        return resultVector

    def __sub__(self, otherVector: 'VectorValue') -> 'VectorValue':
        resultVector = VectorValue(self._x, self._y, self._z)
        resultVector._x -= otherVector._x
        resultVector._y -= otherVector._y
        resultVector._z -= otherVector._z
        return resultVector

    def __str__(self) -> str:
        return f"({self._x}, {self._y}, {self._z})"

    def __mul__(self, otherVector: Any) -> 'VectorValue':
        if isinstance(otherVector, (int, float)):
            return VectorValue(self._x * otherVector, self._y * otherVector, self._z * otherVector)
        else:
            return VectorValue(
                (self._y * otherVector._z) - (self._z * otherVector._y),
                (self._z * otherVector._x) - (self._x * otherVector._z),
                (self._x * otherVector._y) - (self._y * otherVector._z)
            )

    def __rmul__(self, otherVector: Any) -> 'VectorValue':
        if isinstance(otherVector, (int, float)):
            return VectorValue(self._x * otherVector, self._y * otherVector, self._z * otherVector)
        else:
            return VectorValue(
                (self._y * otherVector._z) - (self._z * otherVector._y),
                (self._z * otherVector._x) - (self._x * otherVector._z),
                (self._x * otherVector._y) - (self._y * otherVector._z)
            )

    def magnitude(self) -> float:
        return math.sqrt((math.sqrt((self._x ** 2) + (self._y ** 2)) ** 2) + (self._z ** 2))
