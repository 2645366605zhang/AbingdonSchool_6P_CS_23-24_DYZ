import math

rectTest = [
    [[10, 10], [40, 100, 14.142]], 
    [[114, 514], [1256, 58596, 526.49]], 
    [[1919, 810], [5458, 1554390, 2082.945]], 
    [[64, 128], [384, 8192, 143.108]], 
    [[3.14, 3.14], [12.56, 9.86, 4.441]], 
]

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

def functionTest(testList):
    for testObject in testList:
        testData = Rectangle(testObject[0][0], testObject[0][1]).getData()
        if testData == ([testObject[1][0], testObject[1][1], testObject[1][2]]):
            result = "Success"
        else:
            result = "Failure"
        print(f"Test object {testObject[0]} should return {testObject[1]},\nactually returned {testData}.\nThis test is a {result}.\n")

#print(Rectangle(10, 10))

functionTest(rectTest)