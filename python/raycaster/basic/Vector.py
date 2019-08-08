class Vector:
    def __init__(self, dx, dy, dz):
        if dx == dy == dz == 0:
            raise ValueError("Vector cannot have all values equal to zero.")

        self.dx = dx
        self.dy = dy
        self.dz = dz

    def norm(self):
        return (self.dx ** 2 + self.dy ** 2 + self.dz ** 2) ** 0.5
