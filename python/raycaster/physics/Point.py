# Importar arquivos do mesmo pacote.
from .Vector import Vector


class Point:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        self._y = value

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, value: float) -> None:
        self._z = value

    def __str__(self):
        return "({0}, {1}, {2})".format(self._x, self._y, self._z)

    def __eq__(self, other):
        # Argumento é um ponto.
        if isinstance(other, Point):
            # Comparação entre coordenadas.
            return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para comparação com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __add__(self, other):
        # Argumento é um vetor.
        if isinstance(other, Vector):
            # Adição de um ponto e um deslocamento (vetor) é um ponto.
            return Point(self.x + other.dx, self.y + other.dy, self.z + other.dz)
        raise TypeError(
            "Classe '{0}' não possui suporte para adição com objetos de tipo '{1}'."
            .format(self.__class__.__name__, type(other))
        )

    __radd__ = __add__

    def __sub__(self, other):
        # Argumento é um ponto.
        if isinstance(other, Point):
            # Diferença entre dois pontos é um vetor.
            return Vector.B(other, self)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para subtração com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __rshift__(self, other):
        # Argumento é um ponto.
        if isinstance(other, Point):
            # Distância entre dois pontos.
            return Point.dist(self, other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para rshift com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    @staticmethod
    def dist(p1: "Point", p2: "Point") -> float:
        return (p1 - p2).norm
