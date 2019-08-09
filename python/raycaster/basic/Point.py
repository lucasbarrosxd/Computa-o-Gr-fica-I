# Importar arquivos do mesmo pacote.
from . import *


class Point:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._y

    @z.setter
    def z(self, value):
        self._z = value

    def __str__(self):
        return "({0}, {1}, {2})".format(self._x, self._y, self._z)

    def __sub__(self, other):
        # Argumento é um ponto.
        if isinstance(other, Point):
            # Diferença entre dois pontos é um vetor.
            return Vector(self._x - other.x, self._y - other.y, self._z - other.z)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para subtração com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )
