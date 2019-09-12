# Importar bibliotecas.
import math
# # Tipagem.
from numbers import Real
from typing import Optional, Text, Union
# Importar do projeto.
from python.raycaster.physics import *
# Importar do pacote.
from .. import Surface


class Cone(Surface):
    def __init__(self, bottom: Point, top: Point, radius: Real) -> None:
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
    def height(self) -> Real:
        return self._height

    @height.setter
    def height(self, value: Real) -> None:
        self._height = value

    @property
    def radius(self) -> Real:
        return self._radius

    @radius.setter
    def radius(self, value: Real) -> None:
        self._radius = value

    def __str__(self) -> Text:
        return "B: {0} T: {1} n:{2} h: {3} r: {4}".format(self.bottom, self.top, self.normal, self.height, self.radius)

    def __matmul__(self, other: Line) -> Optional[Real]:
        # Verificar tipo do argumento.
        if isinstance(other, Line):
            # Argumento é uma reta.
            # Interseção reta-cone retorna um coeficiente ou nada.
            return Cone.intersection(self, other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para interseção com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def normal_projection(self, point: Point) -> Optional[Vector]:
        p1p = point - self.top

        if math.isclose(p1p.norm, 0):
            return None

        p0p1 = self.top - self.bottom
        return p1p ** (p1p ** p0p1)

    def intersection(self, line: Line, coef: bool = True, fwrd: bool = True) -> Optional[Union[Point, Real]]:
        v = line.direction
        u = self.top - self.bottom
        w = self.bottom - line.origin

        # Common calculations.
        vv = v * v
        uu = u * u
        uu2 = uu ** 2
        ww = w * w
        vu = v * u
        wu = w * u
        vw = v * w
        r2 = self.radius ** 2

        a = vv * uu2 - (vu ** 2) * (r2 + uu)
        b = 2 * (r2 * vu * (wu + uu) + vu * wu * uu - vw * uu2)
        c = ww * uu2 - r2 * ((wu + uu) ** 2) - (wu ** 2) * uu

        delta = b ** 2 - 4 * a * c

        if delta < 0:
            # Não há interseção. A reta e o cone não se encontram.
            return None
        else:
            if math.isclose(a, 0):
                # A reta e a geratriz do cone são paralelas. Não há equação de segundo grau.
                if math.isclose(b, 0):
                    if math.isclose(c, 0):
                        # Qualquer valor de t satisfaz a equação.
                        t_1 = wu / vu
                        t_2 = (wu + uu) / vu
                        if t_1 > t_2:
                            t = t_1 if t_2 < 0 else t_2
                        else:
                            t = t_2 if t_1 < 0 else t_1

                        return None if (fwrd and t < 0) else (t if coef else line(t))
                    else:
                        # Nenhum valor de t satisfaz a equação.
                        return None
                else:
                    t = - c / b
                    s = (t * (v * u) - (w * u)) / (u * u)
                    if 0 <= s <= 1:
                        return None if (fwrd and t < 0) else (t if coef else line(t))
                    else:
                        # Não há interseção.
                        return None
            else:
                if math.isclose(delta, 0):
                    # Há apenas uma interseção tangencial possível.
                    t = (- b) / (2 * a)
                    s = (t * (v * u) - (w * u)) / (u * u)

                    if 0 <= s <= 1:
                        # A interseção é válida.
                        return None if (fwrd and t < 0) else (t if coef else line(t))
                    else:
                        # A interseção não é válida.
                        return None
                else:
                    # Há duas interseções possíveis.
                    t_min = (- b - math.sqrt(delta)) / (2 * a)
                    t_max = (- b + math.sqrt(delta)) / (2 * a)

                    s_min = (t_min * (v * u) - (w * u)) / (u * u)
                    s_max = (t_max * (v * u) - (w * u)) / (u * u)

                    if 0 <= s_min <= 1:
                        if 0 <= s_max <= 1:
                            # As duas interseções são válidas.
                            t = t_max if t_min < 0 else t_min
                        else:
                            t = t_min
                    elif 0 <= s_max <= 1:
                        # Apenas a segunda interseção é válida.
                        t = t_max
                    else:
                        # Nenhuma das interseções é válida.
                        return None

                    return None if (fwrd and t < 0) else (t if coef else line(t))

    def _true_intersection(self, line: Line):
        raise NotImplementedError
