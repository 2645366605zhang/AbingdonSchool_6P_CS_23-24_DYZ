import math

class VectorValue: # For all "Magic Methods" check https://python-course.eu/oop/magic-methods.php .

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __add__(self, otherVector):
        resultVector = VectorValue(self._x, self._y)
        resultVector._x += otherVector._x
        resultVector._y += otherVector._y
        return resultVector
    
    def __sub__(self, otherVector):
        resultVector = VectorValue(self._x, self._y)
        resultVector._x -= otherVector._x
        resultVector._y -= otherVector._y
        return resultVector

    def __str__(self):
        return (f"({self._x}, {self._y})")
    
    def __mul__(self, otherVector):
        if (type(otherVector) in [int, float]):
            return (VectorValue((self._x * otherVector), (self._y * otherVector)))
        else:
            return (VectorValue((self._x * otherVector._x), (self._y * otherVector._y)))
    
    def __rmul__(self, otherVector):
        if (type(otherVector) in [int, float]):
            return (VectorValue((self._x * otherVector), (self._y * otherVector)))
        else:
            return (VectorValue((self._x * otherVector._x), (self._y * otherVector._y)))
    
    def magnitude(self):
        return (math.sqrt((self._x ** 2) + (self._y ** 2)))

vector0 = VectorValue(2, 2)
vector1 = VectorValue(1, 3)
vector2 = vector0 + vector1
vector3 = vector0 - vector1
vector4 = vector2 * vector3
vector5 = vector3 * 5
vector6 = 5 * vector3
print(f"{vector2}\n{vector3}\n{vector4}\n{vector5}\n{vector6}")
