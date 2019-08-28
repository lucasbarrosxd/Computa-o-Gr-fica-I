# Importar arquivos do projeto.
from python.raycaster.physics import *


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
