# Importar arquivos do mesmo pacote.
from . import Object
# Importar arquivos do projeto.
from python.raycaster.basic import *


class Cylinder(Object):
    def __init__(self, top, bottom, radius):
        self.top = top
        self.bottom = bottom
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
