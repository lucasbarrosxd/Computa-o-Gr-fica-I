# Importar arquivos do mesmo pacote.
from . import *

import math


class Plane:
    def __init__(self, origin, normal):
        if not isinstance(origin, Point):
            raise TypeError("Argumento 'origin' deve ser do tipo 'Point'.")
        if not isinstance(normal, Vector):
            raise TypeError("Argumento 'normal' deve ser do tipo 'Vector'.")

        self.origin = origin
        self.normal = normal

    @property
    def origin(self):
        return self.origin

    @origin.setter
    def origin(self, value):
        if not isinstance(value, Point):
            raise TypeError("Argumento 'origin' deve ser do tipo 'Point'.")
        self.origin = value

    @property
    def normal(self):
        return self.normal

    @normal.setter
    def normal(self, value):
        if not isinstance(value, Vector):
            raise TypeError("Argumento 'normal' deve ser do tipo 'Vector'.")
        self.normal = value

    def __str__(self):
        return "O: {0} N: {1}".format(self.origin, self.normal)

    def intersection(self, line):
        if not isinstance(line, Line):
            raise TypeError("Argumento 'line' deve ser do tipo 'Line'.")

        # Checar se a reta é perpendicular à normal do plano.
        if math.isclose(self.normal * line.direction, 0):
            # É perpendicular
            if math.isclose((line.origin - self.origin) * self.normal, 0):
                # A reta está sobre o plano, a interseção é a própria reta.
                return line
            else:
                # A reta é paralela ao plano, não há interseção.
                return None
        else:
            # Não é perpendicular, a interseção é um ponto.
            t = ((self.origin - line.origin) * self.normal) / (line.direction * self.normal)
            return line(t)
