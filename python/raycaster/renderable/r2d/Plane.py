# Importar arquivos do projeto.
from python.raycaster.physics import *
# Importar bibliotecas.
import math
from typing import Optional, Union


class Plane:
    def __init__(self, origin: Point, normal: Vector) -> None:
        self.origin = origin
        self.normal = normal

    @property
    def origin(self) -> Point:
        return self._origin

    @origin.setter
    def origin(self, value: Point) -> None:
        self._origin = value

    @property
    def normal(self) -> Vector:
        return self._normal

    @normal.setter
    def normal(self, value: Vector) -> None:
        self._normal = value

    def __str__(self):
        return "O: {0} N: {1}".format(self.origin, self.normal)

    def __matmul__(self, other):
        # Argumento é uma reta.
        if isinstance(other, Line):
            # Interseção reta-plano.
            return Plane.intersection(self, other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para interseção com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    @staticmethod
    def intersection(plane: "Plane", line: Line, coef: bool = True, fwrd: bool = True):
        v = line.direction
        n = plane.normal
        prpl = plane.origin - line.origin

        # Verificar se o plano e a reta são perpendiculares.
        if not math.isclose(v * n, 0):
            # Não são perpendiculares. Há uma única interseção.
            t = (prpl * n) / (v * n)

            return None if (t < 0 and fwrd) else (t if coef else line(t))
        else:
            # São perpendiculares.
            if math.isclose(prpl * n, 0):
                # A reta está sobre o plano. A interseção é a própria reta. Retornar a origem da reta.
                t = 0
                return None if (t < 0 and fwrd) else (t if coef else line(t))
            else:
                return None

    @staticmethod
    def _true_intersection(plane: "Plane", line: Line):
        v = line.direction
        n = plane.normal
        prpl = plane.origin - line.origin

        if not math.isclose(v * n, 0):
            return line((prpl * n) / (v * n))
        else:
            if math.isclose(prpl * n, 0):
                return line
            else:
                return None
