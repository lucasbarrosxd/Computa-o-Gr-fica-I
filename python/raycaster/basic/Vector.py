class Vector:
    def __init__(self, dx, dy, dz):
        if dx == dy == dz == 0:
            raise ValueError("Vector cannot have all values equal to zero.")

        self.dx = dx
        self.dy = dy
        self.dz = dz

    def __str__(self):
        return "({0}, {1}, {2})".format(self.dx, self.dy, self.dz)
    
    @property
    def dx(self):
        return self.dx

    @dx.setter
    def dx(self, value):
        if value != 0 or self.dy != 0 or self.dz != 0:
            self.dx = value
        else:
            raise ValueError("Vector cannot have all values equal to zero.")

    @property
    def dy(self):
        return self.dy

    @dy.setter
    def dy(self, value):
        if value != 0 or self.dz != 0 or self.dx != 0:
            self.dy = value
        else:
            raise ValueError("Vector cannot have all values equal to zero.")

    @property
    def dz(self):
        return self.dz

    @dz.setter
    def dz(self, value):
        if value != 0 or self.dy != 0 or self.dx != 0:
            self.dz = value
        else:
            raise ValueError("Vector cannot have all values equal to zero.")

    def norm(self):
        return (self.dx ** 2 + self.dy ** 2 + self.dz ** 2) ** 0.5


class Helper:
    @staticmethod
    def scalar(vector1, vector2):
        if not isinstance(vector1, Vector) or not isinstance(vector2, Vector):
            raise TypeError("Arguments must be of type 'Vector'.")
        return vector1.dx * vector2.dx + vector1.dy * vector2.dy + vector1.dz * vector2.dz

    @staticmethod
    def vectorial(vector1, vector2):
        if not isinstance(vector1, Vector) or not isinstance(vector2, Vector):
            raise TypeError("Arguments must be of type 'Vector'.")
        try:
            return Vector(
                vector1.dy * vector2.dz - vector1.dz * vector2.dy,
                vector1.dz * vector2.dx - vector1.dx * vector2.dz,
                vector1.dx * vector2.dy - vector1.dy * vector2.dx
            )
        except ValueError:
            pass
