# Importar do pacote.
from .. import Intersectionable
from . import Plane
# Importar do projeto.
from python.raycaster.physics import *
# Importar bibliotecas.
import math
from typing import Union


class Circle(Intersectionable):
    def __init__(self, center: Point, normal: Vector, radius: float) -> None:
        self.center = center
        self.normal = normal
        self.radius = radius

    @classmethod
    def A(cls, center: Point, normal: Vector, radius: float) -> "Circle":
        return cls(center, normal, radius)

    @classmethod
    def B(cls, plane: Plane, radius: float) -> "Circle":
        return cls(plane.origin, plane.normal, radius)

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

    def intersection(self, line: Line, coef: bool = True, fwrd: bool = True) -> Union[None, Point, float]:
        v = line.direction
        n = self.normal
        prpl = self.center - line.origin

        # Verificar se a reta e o plano do círculo são paralelos.
        if math.isclose(v * n, 0):
            # A reta e o plano são paralelos.
            # Verificar se a reta está sobre o plano do círculo.
            if math.isclose(prpl * n, 0):
                # A reta está sobre o plano do círculo.
                a = v * v
                b = - 2 * a
                c = prpl * prpl - self.radius ** 2

                delta = b ** 2 - 4 * a * c

                # Verificar casos especiais.
                if math.isclose(a, 0):
                    # A reta na verdade é um ponto.
                    if c <= 0:
                        # O ponto está sobre o círculo.
                        t = 0
                        return t if coef else line.origin
                    else:
                        # O ponto não está sobre o círculo.
                        return None
                elif delta < 0:
                    # A reta e o círculo não se cruzam.
                    return None
                else:
                    # A reta e o círculo se cruzam. Retornar um segmento de reta.
                    t_min = (- b - math.sqrt(delta)) / (2 * a)
                    t_max = (- b + math.sqrt(delta)) / (2 * a)
                    t = max(t_min, min(0, t_max))
                    return None if (fwrd and t < 0) else (t if coef else line(t))
            else:
                # Não está sobre o plano do círculo. Não há interseção.
                return None
        else:
            # Não são paralelos. Há no máximo uma única interseção.
            t = (prpl * n) / (v * n)

            # Verificar se a interseção está no círculo.
            if (t ** 2) * (v * v) - 2 * t * (v * v) + prpl * prpl - self.radius ** 2 <= 0:
                # A interseção com o plano está no círculo.
                return line(t)
            else:
                # A interseção com o plano está fora do círculo.
                return None

    def _true_intersection(self, line: Line):
        v = line.direction
        n = self.normal
        prpl = self.center - line.origin

        # Verificar se a reta e o plano do círculo são paralelos.
        if math.isclose(v * n, 0):
            # A reta e o plano são paralelos.
            # Verificar se a reta está sobre o plano do círculo.
            if math.isclose(prpl * n, 0):
                # A reta está sobre o plano do círculo.
                a = v * v
                b = - 2 * a
                c = prpl * prpl - self.radius ** 2

                delta = b ** 2 - 4 * a * c

                # Verificar casos especiais.
                if math.isclose(a, 0):
                    # A reta na verdade é um ponto.
                    if c <= 0:
                        # O ponto está sobre o círculo.
                        return line
                    else:
                        # O ponto não está sobre o círculo.
                        return None
                elif delta < 0:
                    # A reta e o círculo não se cruzam.
                    return None
                elif math.isclose(delta, 0):
                    # A reta e o círculo se cruzam tangencialmente.
                    return line(- b / (2 * a))
                else:
                    # A reta atravessa o círculo. Retornar um segmento de reta.
                    return Line.B(line((- b - math.sqrt(delta)) / (2 * a)), line((- b + math.sqrt(delta)) / (2 * a)))
            else:
                # Não está sobre o plano do círculo. Não há interseção.
                return None
        else:
            # Não são paralelos. Há no máximo uma única interseção.
            t = (prpl * n) / (v * n)

            # Verificar se a interseção está no círculo.
            if (t ** 2) * (v * v) - 2 * t * (v * v) + prpl * prpl - self.radius ** 2 <= 0:
                # A interseção com o plano está no círculo.
                return line(t)
            else:
                # A interseção com o plano está fora do círculo.
                return None
