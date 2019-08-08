from .Point import *
from .Vector import *


class Line:
    def __init__(self, origin, direction):
        if not isinstance(origin, Point):
            raise TypeError("Argument 'origin' must be of type 'Point'.")
        if not isinstance(direction, Vector):
            raise TypeError("Argument 'direction' must be of type 'Vector'.")
        self.origin = origin
        self.direction = direction

    def __str__(self):
        return "O: {0} V: {1}".format(str(self.origin), str(self.direction))

    @property
    def origin(self):
        return self.origin

    @origin.setter
    def origin(self, value):
        if not isinstance(value, Point):
            raise TypeError("Argument 'origin' must be of type 'Point'.")
        self.origin = value

    @property
    def direction(self):
        return self.direction

    @direction.setter
    def direction(self, value):
        if not isinstance(value, Vector):
            raise TypeError("Argument 'direction' must be of type 'Vector'.")
        self.direction = value
