# Importar arquivos do projeto.
from python.raycaster.physics import *


class Triangle:
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

    def __str__(self) -> str:
        return "{0} {1} {2}".format(self.point_1, self.point_2, self.point_3)

    def __matmul__(self, other):
        # Argumento é uma reta.
        if isinstance(other, Line):
            # Interseção reta-triângulo.
            return Triangle.intersection(self, other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para interseção com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    @staticmethod
    def intersection(triangle: "Triangle", line: Line) -> Point:
        raise NotImplementedError

    @staticmethod
    def _true_intersection(triangle: "Triangle", line: Line):
        raise NotImplementedError
