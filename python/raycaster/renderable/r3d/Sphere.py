# Importar arquivos do projeto.
from python.raycaster.physics import *


class Sphere:
    def __init__(self, center: Point, radius: float) -> None:
        self.center = center
        self.radius = radius

    @property
    def center(self) -> Point:
        return self._center

    @center.setter
    def center(self, value: Point) -> None:
        self._center = value

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = value

    def __str__(self):
        return "O: {0} r: {1}".format(self.center, self.radius)

    def __matmul__(self, other):
        # Argumento é uma reta.
        if isinstance(other, Line):
            # Interseção reta-esfera.
            return Sphere.intersection(self, other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para interseção com objetos de tipo '{1}'."
                    .format(self.__class__.__name__, type(other))
            )

    @staticmethod
    def intersection(sphere: "Sphere", line: Line, coef: bool = True, fwrd: bool = True) -> Point:
        raise NotImplementedError

    @staticmethod
    def _true_intersection(sphere: "Sphere", line: Line):
        v = line.direction
        prpo = sphere.center - line.origin

        a = v * v
        b = - 2 * prpo * v
        c = prpo * prpo - sphere.radius ** 2

        delta = b ** 2 - 4 * a * c

        if math.isclose(a, 0):
            if delta < 0:
                return None
            elif math.isclose(delta, 0):
                t = (-b) / (2 * a)

                return line(t)
            else:
                t1 = ((-b) - math.sqrt(delta)) / (2 * a)
                t2 = ((-b) - math.sqrt(delta)) / (2 * a)

                return line(t1), line(t2)
        else:
            if math.isclose(c, 0):
                return line
            else:
                return None
