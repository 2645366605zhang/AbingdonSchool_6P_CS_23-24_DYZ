from __future__ import annotations

class Node:

    def __init__(self, data, nextNode: Node | None):
        self._data = data
        self._nextNode = nextNode
    
    def getData(self):
        return self._data
    
    def getNextNode(self):
        return self._nextNode
    
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
    
thisLL = LinkedListStack("A", maxSize = 8, safeMode = True)
for integer in range(9):
    thisLL.push(integer)
print(thisLL)
print(thisLL.getList())
for integer in range(5):
    print(thisLL.pop())
