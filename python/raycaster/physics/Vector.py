# Importar do pacote.
from . import Point
# Importar bibliotecas.
import math


class Vector:
    def __init__(self, dx: float, dy: float, dz: float) -> None:
        self.dx = dx
        self.dy = dy
        self.dz = dz

    @classmethod
    def A(cls, dx: float, dy: float, dz: float) -> "Vector":
        return cls(dx, dy, dz)

    @classmethod
    def B(cls, p_from: Point, p_to: Point) -> "Vector":
        return cls(p_to.x - p_from.x, p_to.y - p_from.y, p_to.z - p_from.z)
    
    @property
    def dx(self) -> float:
        return self._dx

    @dx.setter
    def dx(self, value: float) -> None:
        self._dx = value

    @property
    def dy(self) -> float:
        return self._dy

    @dy.setter
    def dy(self, value: float) -> None:
        self._dy = value

    @property
    def dz(self) -> float:
        return self._dz

    @dz.setter
    def dz(self, value: float) -> None:
        self._dz = value

    @property
    def norm(self) -> float:
        return math.sqrt(self.dx ** 2 + self.dy ** 2 + self.dz ** 2)

    @norm.setter
    def norm(self, value: float) -> None:
        old_norm = self.norm

        if math.isclose(old_norm, 0):
            raise ArithmeticError("Não é possível alterar a norma de um vetor nulo.")

        self.dx = self.dx * value / old_norm
        self.dy = self.dy * value / old_norm
        self.dz = self.dz * value / old_norm

    def unit(self) -> "Vector":
        return self / self.norm

    def __str__(self) -> str:
        return "({0}, {1}, {2})".format(self.dx, self.dy, self.dz)

    def __eq__(self, other) -> bool:
        # Argumento é um vetor.
        if isinstance(other, Vector):
            return (self.dx == other.dx) and (self.dy == other.dy) and (self.dz == other.dz)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para comparação com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __add__(self, other):
        # Argumento é um vetor.
        if isinstance(other, Vector):
            # Adição de dois vetores.
            return Vector(self.dx + other.dx, self.dy + other.dy, self.dz + other.dz)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para adição com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __sub__(self, other):
        # Argumento é um vetor.
        if isinstance(other, Vector):
            # Subtração de dois vetores.
            return Vector(self.dx - other.dx, self.dy - other.dy, self.dz - other.dz)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para subtração com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __neg__(self):
        return Vector(- self.dx, - self.dy, - self.dz)

    def __mul__(self, other):
        # Argumento é um vetor.
        if isinstance(other, Vector):
            # Produto escalar de dois vetores.
            return Vector.scalar_prod(self, other)
        # Argumento é um número.
        elif isinstance(other, (int, float, complex)) and not isinstance(other, bool):
            # Produto de um escalar por um vetor.
            return Vector(self.dx * other, self.dy * other, self.dz * other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para multiplicação com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    __rmul__ = __mul__

    def __truediv__(self, other):
        # Argumento é um número.
        if isinstance(other, (int, float, complex)) and not isinstance(other, bool):
            # Divisão de um vetor por um escalar.
            return Vector(self.dx / other, self.dy / other, self.dz / other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para divisão com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    def __pow__(self, other):
        # Argumento é um vetor.
        if isinstance(other, Vector):
            # Produto vetorial de dois vetores.
            return Vector.cross_prod(self, other)
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para produto vetorial com objetos de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )

    @staticmethod
    def scalar_prod(vector1: "Vector", vector2: "Vector"):
        return vector1.dx * vector2.dx + vector1.dy * vector2.dy + vector1.dz * vector2.dz

    @staticmethod
    def cross_prod(vector1: "Vector", vector2: "Vector"):
        return Vector(
            vector1.dy * vector2.dz - vector1.dz * vector2.dy,
            vector1.dz * vector2.dx - vector1.dx * vector2.dz,
            vector1.dx * vector2.dy - vector1.dy * vector2.dx
        )
