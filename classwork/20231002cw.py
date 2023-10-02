# A Python list atht acts like a stack

"""

stack = []

def stackOperation(stack):
    highWatermarkPointer = 128 # 128 for 8 bits, 2048 for 12 bits
    topStackPointer = -1
    baseStackPointer = 0
    while topStackPointer < highWatermarkPointer:
        for item in range(highWatermarkPointer):
            topStackPointer += 1
            stack.append(item)
            print(f"Item {item} inserted into the stack.")
    print("\nStack Full")
    while topStackPointer >= baseStackPointer:
        print(f"Item {stack[topStackPointer]} popped from the stack.")
        stack.pop(topStackPointer)
        topStackPointer -= 1
    print("\nStack Empty")

stackOperation(stack)

"""

class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self._data) == 0
    
    def push(self, element):
        self._data.append(element)

    def top(self):
        if self.isEmpty():
            raise Empty("Stack is empty")
        return self._data[-1]
    
    def pop(self):
        if self.isEmpty():
            raise Empty("Stack is empty")
        return self._data.pop()
    
newStack = ArrayStack()
# Will output "__main__.Empty: Stack is empty"
#newStack.pop()