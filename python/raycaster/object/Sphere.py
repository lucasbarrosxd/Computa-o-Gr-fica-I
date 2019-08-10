# Importar arquivos do mesmo pacote.
from . import Object
# Importar arquivos do projeto.
from python.raycaster.basic import *
# Imporar bibliotecas.
import math


class Sphere(Object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, value):
        if not isinstance(value, Point):
            raise TypeError("Argumento 'center' deve ser de tipo 'Point'.")

        self._center = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not (isinstance(value, (int, float, complex)) and not isinstance(value, bool)):
            raise TypeError("Argumento 'radius' deve ser de tipo numérico.")

        self._radius = value

    def __str__(self):
        return "O: {0} r: {1}".format(self.center, self.radius)

    def intersection(self, line):
        if not isinstance(line, Line):
            raise TypeError("Argumento 'line' deve ser de tipo 'Line'.")

        a = line.direction * line.direction
        b = 2 * (line.origin - self.center)
        c = ((line.origin - self.center) * (line.origin - self.center)) - self.radius ** 2
        delta = b ** 2 - 4 * a * c

        # Verificar tipo de interseção
        if delta < 0:
            # Não há interseção.
            return None
        elif math.isclose(delta, 0):
            # Interseção tangencial.
            t = ((-1) * b) / (2 * a)
            return line(t)
        else:
            # Duas interseções.
            t1 = ((-1) * b + delta ** 0.5) / (2 * a)
            t2 = ((-1) * b - delta ** 0.5) / (2 * a)
            return line(t1), line(t2)
