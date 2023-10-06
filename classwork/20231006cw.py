
class Empty(Exception):
    pass

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

cQueue0 = ArrayCircularQueue(8)
cQueue0.add(5)
cQueue0.add(9)
print(cQueue0)