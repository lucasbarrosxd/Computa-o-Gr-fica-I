# Importar arquivos do projeto.
from python.raycaster.physics import *


class Sphere:
    def __init__(self, center: Point, radius: float) -> None:
        self.center = center
        self.radius = radius

    @property
    def center(self) -> Point:
        return self._center

    @center.setter
    def center(self, value: Point) -> None:
        self._center = value

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = value

    def __str__(self):
        return "O: {0} r: {1}".format(self.center, self.radius)
