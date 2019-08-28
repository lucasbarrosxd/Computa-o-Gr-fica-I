# Importar arquivos do projeto.
from python.raycaster.physics import *
# Importar bibliotecas.
import math


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
        return "O: {0} N: {1}".format(self._origin, self._normal)
