# Importar arquivos do mesmo pacote.
from . import Point, Vector, Line
# Importar bibliotecas.
import math


class Plane:
    def __init__(self, origin, normal):
        self.origin = origin
        self.normal = normal

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        if not isinstance(value, Point):
            raise TypeError("Parâmetro 'origin' deve ser do tipo 'Point'.")

        self._origin = value

    @property
    def normal(self):
        return self._normal

    @normal.setter
    def normal(self, value):
        if not isinstance(value, Vector):
            raise TypeError("Parâmetro 'normal' deve ser do tipo 'Vector'.")

        self._normal = value

    def __str__(self):
        return "O: {0} N: {1}".format(self._origin, self._normal)

    def intersection(self, line):
        if not isinstance(line, Line):
            raise TypeError("Argumento 'line' deve ser do tipo 'Line'.")

        # Checar se a reta é perpendicular à normal do plano.
        if math.isclose(self._normal * line.direction, 0):
            # É perpendicular
            if math.isclose((line.origin - self._origin) * self._normal, 0):
                # A reta está sobre o plano, a interseção é a própria reta.
                return line
            else:
                # A reta é paralela ao plano, não há interseção.
                return None
        else:
            # Não é perpendicular, a interseção é um ponto.
            t = ((self._origin - line.origin) * self._normal) / (line.direction * self._normal)
            return line(t)
