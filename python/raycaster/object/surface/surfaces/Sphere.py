# Importar bibliotecas.
import math
# # Tipagem.
from numbers import Real
from typing import Optional, Text, Union
# Importar do projeto.
from python.raycaster.physics import *
# Importar do pacote.
from python.raycaster.object.surface import Surface


class Sphere(Surface):
    def __init__(self, center: Point, radius: Real) -> None:
        self.center = center
        self.radius = radius

    @property
    def center(self) -> Point:
        return self._center

    @center.setter
    def center(self, value: Point) -> None:
        self._center = value

    @property
    def radius(self) -> Real:
        return self._radius

    @radius.setter
    def radius(self, value: Real) -> None:
        self._radius = value

    def __str__(self) -> Text:
        return "O: {0} r: {1}".format(self.center, self.radius)

    def __matmul__(self, other: Line) -> Optional[Real]:
        # Verificar tipo do argumento.
        if isinstance(other, Line):
            # Argumento é uma reta.
            # Interseção reta-esfera retorna um coeficiente ou nada.
            return Sphere.intersection(self, other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para interseção com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def normal_projection(self, point: Point) -> Optional[Vector]:
        return Vector.b(self.center, point)

    def intersection(self, line: Line, coef: bool = True, fwrd: bool = True) -> Optional[Union[Point, Real]]:
        v = line.direction
        prpo = self.center - line.origin

        a = v * v
        b = - 2 * prpo * v
        c = prpo * prpo - self.radius ** 2

        delta = b ** 2 - 4 * a * c

        # Verificar se o vetor da reta é nulo.
        if math.isclose(a, 0):
            # O vetor da reta é nulo. A reta na verdade é um ponto.
            # Verificar se o ponto está sobre a superfície da esfera.
            if math.isclose(c, 0):
                # A interseção é a própria reta. Retornar a origem.
                return 0 if coef else line.origin
            else:
                # Não há interseção.
                return None
        # Verificar se há interseção.
        elif delta < 0:
            # Não há interseção.
            return None
        elif math.isclose(delta, 0):
            # A interseção é tangencial. Só há uma interseção.
            t = (- b) / (2 * a)
            return None if (fwrd and t < 0) else (t if coef else line(t))
        else:
            # Há duas interseções.
            t_min = ((-b) - math.sqrt(delta)) / (2 * a)
            t_max = ((-b) - math.sqrt(delta)) / (2 * a)
            t = t_max if t_min < 0 else t_min

            return None if (fwrd and t < 0) else (t if coef else line(t))

    def _true_intersection(self, line: Line):
        v = line.direction
        prpo = self.center - line.origin

        a = v * v
        b = - 2 * prpo * v
        c = prpo * prpo - self.radius ** 2

        delta = b ** 2 - 4 * a * c

        # Verificar se o vetor da reta é nulo.
        if math.isclose(a, 0):
            # O vetor da reta é nulo. A reta na verdade é um ponto.
            # Verificar se o ponto está sobre a superfície da esfera.
            if math.isclose(c, 0):
                # A interseção é a própria reta.
                return line
            else:
                # Não há interseção.
                return None
        # Verificar se há interseção.
        elif delta < 0:
            # Não há interseção.
            return None
        elif math.isclose(delta, 0):
            # A interseção é tangencial. Só há uma interseção.
            t = (- b) / (2 * a)
            return line(t)
        else:
            # Há duas interseções.
            t1 = ((-b) - math.sqrt(delta)) / (2 * a)
            t2 = ((-b) - math.sqrt(delta)) / (2 * a)

            return line(t1), line(t2)
