# Object Oriented Programming in Python

class Metal:

    def __init__(self, sbl, num):
        self._symbol = sbl
        self._number = num

    def show(self):
        print(f"\nNumber of metal {self._symbol}: {self._number}")
    
    def add(self, num):
        self._number += num
        print(f"\n{num} {self._symbol} added.")
    
    def use(self, num):
        self._number -= num
        print(f"\n{num} {self._symbol} used.")

iron = Metal("Fe", 20)
iron.show()
iron.add(20)
iron.show()
iron.use(5)
iron.show()

class Mob:

    def __init__(self, id, name, hpLimit, atk):
        self._id = id
        self._name = name
        self._alive = True
        self._hpLimit = hpLimit
        self._hp = hpLimit
        self._atk = atk

    def displayInformation(self):
        print(f"\nName: {self._name}\nHP: {self._hp}/{self._hpLimit}")

    def checkStatus(self):
        if self._hp <= 0:
            self._alive = False
            print(f"\n{self._name} is dead!")
        elif(self._hp) > self._hpLimit:
            self._hp = self._hpLimit

    def attack(self, attackFactor):
        thisAttack = [self._name]
        thisAttack.append(self._atk * attackFactor)
        print(f"\n{self._name} attacks!")
        return(thisAttack)
    
    def receiveDamage(self, receivedFromInfo):
        self._hp -= receivedFromInfo[1]
        print(f"\n{self._name} received {receivedFromInfo[1]} damage from {receivedFromInfo[0]}!")

zombie0 = Mob(0, "Zombie 0", 10, 1)
zombie1 = Mob(0, "Zombie 1", 10, 1)

zombie1.receiveDamage(zombie0.attack(10))

zombie1.checkStatus()

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
    
newQueue = ArrayQueue(8)
if newQueue.isEmpty():
    while not(newQueue.isFull()):
        newQueue.add("AVD")
    newQueue.display()