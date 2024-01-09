users = ["James G", "Alex Van", "Ed", "Jack S"]

class Car:

    def __init__(self, owner, model, color, wheels, capacity, horsePower, price, personalName):
        self._owner = owner
        self._model = model
        self._color = color
        self._wheels = wheels
        self._capacity = capacity
        self._horsePower = horsePower
        self._price = price
        self._personalName = personalName

# For all "Magic Methods" check https://python-course.eu/oop/magic-methods.php .