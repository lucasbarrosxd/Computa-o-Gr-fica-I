# Importar arquivos do projeto.
from python.raycaster.physics import *
# Importar bibliotecas.
import math


class Cone:
    def __init__(self, bottom: Point, top: Point, radius: float) -> None:
        self.bottom = bottom
        self.top = top
        self.radius = radius

    @property
    def bottom(self) -> Point:
        return self._bottom

    @bottom.setter
    def bottom(self, value: Point) -> None:
        self._bottom = value

    @property
    def top(self) -> Point:
        return self._bottom + self.height * self.normal / self.normal.norm

    @top.setter
    def top(self, value: Point) -> None:
        self._normal = value - self.bottom
        self._height = self.normal.norm

    @property
    def normal(self) -> Vector:
        return self._normal

    @normal.setter
    def normal(self, value: Vector) -> None:
        self._normal = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = value

    def __str__(self):
        return "B: {0} T: {1} n:{2} h: {3} r: {4}".format(self.bottom, self.top, self.normal, self.height, self.radius)

    def __matmul__(self, other):
        # Argumento é uma reta.
        if isinstance(other, Line):
            # Interseção reta-cone.
            return Cone.intersection(self, other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para interseção com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    @staticmethod
    def intersection(cone: "Cone", line: Line, coef: bool = True, fwrd: bool = True):
        v = line.direction
        u = cone.top - cone.bottom
        w = cone.bottom - line.origin

        a = (v * v) * ((u * u) ** 2) - ((v * u) ** 2) * ((cone.radius ** 2) + (u * u))
        b = 2 * ((cone.radius ** 2) * (v * u) * (w * u + u * u) + (v * u) * (w * u) * (u * u) - (w * v) * (
                    (u * u) ** 2))
        c = (w * w) * ((u * u) ** 2) - (cone.radius ** 2) * ((w * u + u * u) ** 2) - ((w * u) ** 2) * (u * u)

        delta = b ** 2 - 4 * a * c

        if delta < 0:
            # Não há interseção. A reta e o cone não se encontram.
            return False
        else:
            if math.isclose(a, 0):
                # A reta e a geratriz do cone são paralelas. Não há equação de segundo grau.
                if math.isclose(b, 0):
                    if math.isclose(c, 0):
                        # Qualquer valor de t satisfaz a equação.
                        return True
                    else:
                        # Nenhum valor de t satisfaz a equação.
                        return False
                else:
                    t = - c / b
                    s = (t * (v * u) - (w * u)) / (u * u)
                    if 0 <= s <= 1:
                        return True
                    else:
                        # Não há interseção.
                        return False
            else:
                if math.isclose(delta, 0):
                    # Há apenas uma interseção tangencial possível.
                    t = (- b) / (2 * a)
                    s = (t * (v * u) - (w * u)) / (u * u)

                    if 0 <= s <= 1:
                        # A interseção é válida.
                        return True
                    else:
                        # A interseção não é válida.
                        return False
                else:
                    # Há duas interseções possíveis.
                    t1 = (- b - math.sqrt(delta)) / (2 * a)
                    t2 = (- b + math.sqrt(delta)) / (2 * a)

                    s1 = (t1 * (v * u) - (w * u)) / (u * u)
                    s2 = (t2 * (v * u) - (w * u)) / (u * u)

                    if 0 <= s1 <= 1 and 0 <= s2 <= 1:
                        # As duas interseções são válidas.
                        return True
                    elif 0 <= s1 <= 1:
                        # Apenas a primeira interseção é válida.
                        return True
                    elif 0 <= s2 <= 1:
                        # Apenas a segunda interseção é válida.
                        return True
                    else:
                        # Nenhuma das interseções é válida.
                        return False

    @staticmethod
    def _true_intersection(plane: "Cone", line: Line):
        pass
