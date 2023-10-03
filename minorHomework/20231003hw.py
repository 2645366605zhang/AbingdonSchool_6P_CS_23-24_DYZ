import math

class rectangle:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getPerimeter(self):
        return(2 * self._x + 2 * self._y)
    
    def getArea(self):
        return(self._x * self._y)

    def getDiagonal(self):
        return(math.sqrt(self._x ** 2 + self._y ** 2))
    
    def display(self):
        print(f"The perimeter of this rectangle is {self.getPerimeter()}.\nThe area of this triangle is {self.getArea()}.\nThe diagonal length of this triangle is {self.getDiagonal()}.")
    
rect0 = rectangle(10, 10)
rect0.display()