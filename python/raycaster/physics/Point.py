# Importar bibliotecas.
# # Tipagem.
from numbers import Real
from typing import Text
# Importar do pacote.
from .Vector import Vector


class Point:
    def __init__(self, x: Real, y: Real, z: Real) -> None:
        self.x = x
        self.y = y
        self.z = z

    @property
    def x(self) -> Real:
        return self._x

    @x.setter
    def x(self, value: Real) -> None:
        self._x = value

    @property
    def y(self) -> Real:
        return self._y

    @y.setter
    def y(self, value: Real) -> None:
        self._y = value

    @property
    def z(self) -> Real:
        return self._z

    @z.setter
    def z(self, value: Real) -> None:
        self._z = value

    def __str__(self) -> Text:
        return "({0}, {1}, {2})".format(self._x, self._y, self._z)

    def __eq__(self, other: "Point") -> bool:
        # Verificar tipo do argumento.
        if isinstance(other, Point):
            # Argumento é um ponto.
            # Comparação entre pontos.
            return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para comparação com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __add__(self, other: Vector) -> "Point":
        # Verificar tipo do argumento.
        if isinstance(other, Vector):
            # Argumento é um vetor.
            # Adição de um ponto e um deslocamento (vetor) é um ponto.
            return Point(self.x + other.dx, self.y + other.dy, self.z + other.dz)
        raise TypeError(
            "Classe '{0}' não possui suporte para adição com objetos de tipo '{1}'."
            .format(self.__class__.__name__, type(other))
        )

    __radd__ = __add__

    def __sub__(self, other: "Point") -> Vector:
        # Verificar tipo do argumento.
        if isinstance(other, Point):
            # Argumento é um ponto.
            # Diferença entre dois pontos é um vetor.
            return Vector.b(other, self)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para subtração com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __rshift__(self, other: "Point") -> Real:
        # Verificar tipo do argumento.
        if isinstance(other, Point):
            # Argumento é um ponto.
            # Distância entre dois pontos é um número real.
            return Point.distance(self, other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para rshift com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    @staticmethod
    def distance(p1: "Point", p2: "Point") -> Real:
        # Criar um vetor é menos eficiente mas mantém a consistência do código.
        return (p1 - p2).norm
