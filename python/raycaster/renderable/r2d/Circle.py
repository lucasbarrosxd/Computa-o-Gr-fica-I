# Importar arquivos do projeto.
from python.raycaster.physics import *


class Circle:
    def __init__(self, center: Point, normal: Vector, radius: float) -> None:
        self.center = center
        self.normal = normal
        self.radius = radius

    @property
    def center(self) -> Point:
        return self._center

    @center.setter
    def center(self, value: Point) -> None:
        self._center = value

    @property
    def normal(self) -> Vector:
        return self._normal

    @normal.setter
    def normal(self, value: Vector) -> None:
        self._normal = value

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = value

    def __str__(self):
        return "O: {0} N: {1} r: {2}".format(self.center, self.normal, self.radius)

    def __matmul__(self, other):
        # Argumento é uma reta.
        if isinstance(other, Line):
            # Interseção reta-círculo.
            return Circle.intersection(self, other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para interseção com objetos de tipo '{1}'."
                    .format(self.__class__.__name__, type(other))
            )

    @staticmethod
    def intersection(circle: "Circle", line: "Line", coef: bool = True, fwrd: bool = True) -> Point:
        raise NotImplementedError

    @staticmethod
    def _true_intersection(circle: "Circle", line: "Line"):
        v = line.direction
        n = circle.normal
        prpl = circle.center - line.origin

        if math.isclose(v * n, 0):
            if math.isclose(prpl * n, 0):
                a = v * v
                b = - 2 * a
                c = prpl * prpl - circle.radius ** 2

                delta = b ** 2 - 4 * a * c

                if math.isclose(a, 0):
                    if c <= 0:
                        return line
                    else:
                        return None
                elif delta < 0:
                    return None
                else:
                    return Vector.B(line((- b - math.sqrt(delta)) / (2 * a)), line((- b + math.sqrt(delta)) / (2 * a)))
            else:
                return None
        else:
            t = (prpl * n) / (v * n)

            if (t ** 2) * (v * v) - 2 * t * (v * v) + prpl * prpl - circle.radius ** 2 <= 0:
                return line(t)
            else:
                return None
