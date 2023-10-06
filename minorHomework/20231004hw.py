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

vector0 = VectorValue(2, 2)
vector1 = VectorValue(1, 3)
vector2 = vector0 + vector1
vector3 = vector0 - vector1
print(f"{vector2}\n{vector3}")
