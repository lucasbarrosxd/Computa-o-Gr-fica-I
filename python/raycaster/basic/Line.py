# Importar arquivos do mesmo pacote.
from . import *


class Line:
    def __init__(self, origin, direction):
        if not isinstance(origin, Point):
            raise TypeError("Argumento 'origin' deve ser do tipo 'Point'.")
        if not isinstance(direction, Vector):
            raise TypeError("Argumento 'direction' deve ser do tipo 'Vector'.")
        self._origin = origin
        self._direction = direction

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        if not isinstance(value, Point):
            raise TypeError("Argumento 'origin' deve ser do tipo 'Point'.")
        self._origin = value

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        if not isinstance(value, Vector):
            raise TypeError("Argumento 'direction' deve ser do tipo 'Vector'.")
        self._direction = value

    def __str__(self):
        return "O: {0} V: {1}".format(str(self._origin), str(self._direction))

    def __call__(self, other):
        # O argumento é um número.
        if isinstance(other, (int, float, complex)) and not isinstance(other, bool):
            # Calcular o ponto P tal que P = Origem + Direção * other
            return Point(
                self._origin.x + self._direction.dx * other,
                self._origin.y + self._direction.dy * other,
                self._origin.z + self._direction.dz * other
            )
        else:
            raise TypeError(
                "Classe '{0}' não possui suporte para chamada com argumento de tipo '{1}'."
                .format(self.__class__.__name__, type(other))
            )
