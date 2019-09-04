# Importar arquivos do projeto.
from python.raycaster.physics import *
# Importar bibliotecas.
import math
from typing import Union


class Cylinder:
    def __init__(self, bottom: Point, normal: Vector, height: float, radius: float) -> None:
        self.bottom = bottom
        self.normal = normal
        self.height = height
        self.radius = radius

    @classmethod
    def A(cls, bottom: Point, normal: Vector, height: float, radius: float):
        return cls(bottom, normal, height, radius)

    @classmethod
    def B(cls, bottom: Point, top: Point, radius: float):
        return cls(bottom, top - bottom, (top - bottom).norm, radius)

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

    def intersection(self, line: Line, coef: bool = True, fwrd: bool = True) -> Union[None, Point, float]:
        v = line.direction
        u = self.normal
        w = self.bottom - line.origin

        # Common calculations.
        vv = v * v
        uu = u * u
        ww = w * w
        vu = v * u
        wu = w * u
        wv = w * v
        r2 = self.radius ** 2

        a = vv * uu - vu ** 2
        b = 2 * (vu * wu - wv * uu)
        c = (ww - r2) * uu - wu ** 2

        # Casos especiais.
        if math.isclose(a, 0):
            # O cilindro é uma esfera.
            if math.isclose(uu, 0):
                # A reta é um ponto.
                if math.isclose(vv, 0):
                    # O ponto está sobre a superfície da esfera.
                    if math.isclose(ww - r2, 0):
                        t = 0
                        return t if coef else line.origin
                    # O ponto não está sobre a superfície da esfera.
                    else:
                        return None
                else:
                    a = vv
                    b = - 2 * wv
                    c = ww - r2

                    delta = b ** 2 - 4 * a * c

                    # Sem interseção reta-esfera.
                    if delta < 0:
                        return None
                    # Há interseção reta-esfera.
                    else:
                        t_min = (- b - math.sqrt(delta)) / (2 * a)
                        t_max = (- b + math.sqrt(delta)) / (2 * a)
                        t = t_max if t_min < 0 else t_min

                        return None if (fwrd and t < 0) else (t if coef else line(t))
            elif math.isclose(c, 0):
                if math.isclose(vv, 0):
                    if 0 <= - wu / uu <= 1:
                        t = 0
                        return t if coef else line.origin
                    else:
                        return None
                else:
                    t_1 = wu / vu
                    t_2 = (wu + uu) / vu
                    if t_1 > t_2:
                        t = t_1 if t_2 < 0 else t_2
                    else:
                        t = t_2 if t_1 < 0 else t_1

                    return None if (fwrd and t < 0) else (t if coef else line(t))
            else:
                return None
        else:
            delta = b ** 2 - 4 * a * c

            if delta < 0:
                return None
            else:
                t_min = ((- b) - math.sqrt(delta)) / (2 * a)
                s_min = (t_min * vu - wu) / uu
                t_max = ((- b) + math.sqrt(delta)) / (2 * a)
                s_max = (t_max * vu - wu) / uu
                if 0 <= s_min <= 1:
                    if 0 <= s_max <= 1:
                        t = t_max if t_min < 0 else t_min
                    else:
                        t = s_min
                elif 0 <= s_max <= 1:
                    t = s_max
                else:
                    return None

                return None if (fwrd and t < 0) else (t if coef else line(t))
