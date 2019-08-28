# Importar arquivos do projeto.
from python.raycaster.physics import *


class Circle:
    def __init__(self, origin: Point, normal: Vector, radius: float) -> None:
        self.origin = origin
        self.normal = normal
        self.radius = radius

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

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = value

    def __str__(self):
        return "O: {0} N: {1} r: {2}".format(self.origin, self.normal, self.radius)
