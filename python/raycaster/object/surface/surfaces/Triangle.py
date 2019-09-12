# Importar bibliotecas.
import math
# # Tipagem.
from numbers import Real
from typing import Optional, Text, Union
# Importar do projeto.
from python.raycaster.physics import Point, Vector, Line
# Importar do pacote.
from .. import Surface


class Triangle(Surface):
    def __init__(self, point_1: Point, point_2: Point, point_3: Point) -> None:
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    @property
    def point_1(self) -> Point:
        return self._point_1

    @point_1.setter
    def point_1(self, value: Point) -> None:
        self._point_1 = value

    @property
    def point_2(self) -> Point:
        return self._point_2

    @point_2.setter
    def point_2(self, value: Point) -> None:
        self._point_2 = value

    @property
    def point_3(self) -> Point:
        return self._point_3

    @point_3.setter
    def point_3(self, value: Point) -> None:
        self._point_3 = value

    def __str__(self) -> Text:
        return "{0} {1} {2}".format(self.point_1, self.point_2, self.point_3)

    def __matmul__(self, other: Line) -> Optional[Real]:
        # Verificar tipo do argumento.
        if isinstance(other, Line):
            # Argumento é uma reta.
            # Interseção reta-triângulo retorna um coeficiente ou nada.
            return Triangle.intersection(self, other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para interseção com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def normal_projection(self, point: Point) -> Optional[Vector]:
        return Vector.b(self.point_1, self.point_2) ** Vector.b(self.point_1, self.point_3)

    def intersection(self, line: Line, coef: bool = True, fwrd: bool = True) -> Optional[Union[Point, Real]]:
        p1p2 = self.point_2 - self.point_1
        p1p3 = self.point_3 - self.point_1

        n = p1p2 ** p1p3

        # Cálculos repetidos.
        v_scalar_n = line.direction * n
        prpl_scalar_n = (self.point_1 - line.origin) * n

        # Verificar se o plano e a reta são paralelos.
        if not math.isclose(v_scalar_n, 0):
            # Não são paralelos. Há no máximo uma única interseção.
            t = prpl_scalar_n / v_scalar_n
            if fwrd and t < 0:
                # A interseção ocorre atrás da reta.
                return None
        else:
            # São paralelos.
            if math.isclose(prpl_scalar_n, 0):
                # A reta está sobre o plano. A interseção é a própria reta. #FIX
                t = 0
            else:
                # A reta é paralela ao plano, mas não está sobre ele. Não há interseção.
                return None

        if t is None or (fwrd and t < 0):
            return None
        else:
            # Validar triângulo.
            p = line(t)

            p2p3 = self.point_3 - self.point_2
            p1p = p - self.point_1
            p2p = p - self.point_2
            p3p = p - self.point_3

            if (p1p2 ** p1p) * n >= 0 and (p2p3 ** p2p) * n >= 0 and ((- p1p3) ** p3p) * n >= 0:
                # Interseção está no triângulo.
                return t if coef else p
            else:
                # Interseção não está no triângulo.
                return None

    def _true_intersection(self, line: Line):
        raise NotImplementedError
