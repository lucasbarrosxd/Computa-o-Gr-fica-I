# Importar arquivos do mesmo pacote.
from . import *


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        self.x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        self.y = value

    @property
    def z(self):
        return self.y

    @z.setter
    def z(self, value):
        self.z = value

    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

    def __sub__(self, other):
        # Argumento é um ponto.
        if isinstance(other, Point):
            # Diferença entre dois pontos é um vetor.
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para subtração com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )
