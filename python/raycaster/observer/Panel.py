# Importar arquivos do projeto.
from python.raycaster.physics import Point, Vector
# Importar bibliotecas.
import math
from typing import Tuple, Optional


class Panel:
    def __init__(self, center: Point, normal: Vector, res: Tuple[int, int], size: Tuple[float, float], orientation: Optional[Vector] = None):
        self.center = center
        self.normal = normal
        self.res = res
        self._size = size

        if orientation is None:
            if not math.isclose(normal.dx, 0) or not math.isclose(normal.dz, 0):
                self.orientation = Vector(0, -1, 0) ** normal
            else:
                self.orientation = Vector(1, 0, 0)
        else:
            self.orientation = orientation

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
    def orientation(self) -> Vector:
        return self._orientation_x

    @orientation.setter
    def orientation(self, value: Vector) -> None:
        if not math.isclose(self.normal * value, 0):
            raise ValueError

        self._orientation_y = Vector.cross_prod(self.normal, value).unit() * self.size[1] / 2
        self._orientation_x = Vector.cross_prod(self._orientation_y, self.normal).unit() * self.size[0] / 2

    @property
    def res(self) -> Tuple[int, int]:
        return self._res

    @res.setter
    def res(self, value: Tuple[int, int]) -> None:
        if value[0] < 0 or value[1] < 0:
            raise ValueError

        self._res = value

    @property
    def size(self) -> Tuple[float, float]:
        return self._size

    @size.setter
    def size(self, value: Tuple[float, float]) -> None:
        self._size = value
        self._orientation_x *= value[0] / 2
        self._orientation_y *= value[1] / 2

    def __str__(self) -> str:
        return "Pos:{0} N:{1} Ori:{2} Res:{3} Size:{4}".format(
            self.center, self.normal, self.orientation, self.res, self.size,
        )

    def point(self, index_x: float, index_y: float) -> Point:
        return self.center + \
               (index_x/self.res[0] - 0.5) * self._orientation_x + \
               (index_y/self.res[1] - 0.5) * self._orientation_y
