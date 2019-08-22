# Importar arquivos do mesmo pacote.
from . import Object
# Importar arquivos do projeto.
from python.raycaster.basic import *


class Cone(Object):
    def __init__(self, bottom, top, radius):
        self.bottom = bottom
        self.top = top
        self.radius = radius

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        if not isinstance(value, Point):
            raise TypeError("Argumento 'top' deve ser de tipo 'Point'.")

        self._top = value

    @property
    def bottom(self):
        return self._bottom

    @bottom.setter
    def bottom(self, value):
        if not isinstance(value, Point):
            raise TypeError("Argumento 'bottom' deve ser de tipo 'Point'.")

        self._bottom = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not (isinstance(value, (int, float, complex)) and not isinstance(value, bool)):
            raise TypeError("Argumento 'radius' deve ser de tipo numérico.")

        self._radius = value

    def __str__(self):
        return "P0: {0} P1: {1} r: {2}".format(self.bottom, self.top, self.radius)
