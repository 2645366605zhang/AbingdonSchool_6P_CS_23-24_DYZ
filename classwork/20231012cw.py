class Node:

    def __init__(self, data, nextNode):
        self._data = data
        self._nextNode = nextNode
    
    def getData(self):
        return (self._data)
    
    def getNextNode(self):
        return (self._nextNode)
    
    def setData(self, newData):
        self._data = newData
    
    def setNextNode(self, newNode):
        self._nextNode = newNode

class LinkedListStack:

    def __init__(self, maxSize, headNodeData):
        self._size = 1
        self._maxSize = maxSize
        self._headNode = Node(headNodeData, None)

    def pop(self):
        if self.getSize() > 0:
            headNodeData = self._headNode.getData()
            pointedNode = self._headNode.getNextNode()
            self._headNode = pointedNode
            self._size -= 1
            #print(f"size: {self.getSize()}")
            return headNodeData
        else:
            print("Failed to pop from the linked list since it is empty.")

    def push(self, data):
        if self.getSize() < self._maxSize:
            newNode = Node(data, self._headNode)
            self._headNode = newNode
            self._size += 1
        else:
            print(f'Failed to push "{data}" to the linked list since it is full.')

    def getSize(self):
        return self._size
    
thisLL = LinkedListStack(8, "A")
for integer in range(9):
    thisLL.push(integer)
for integer in range(9):
    print(thisLL.pop())
