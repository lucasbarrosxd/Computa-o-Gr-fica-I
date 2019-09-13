# Importar bibliotecas.
# # Tipagem.
from numbers import Integral, Real
from typing import Tuple
# Importar do projeto.
from python.raycaster.auxi import RGB


class Texture:
    def __init__(self, amb_color: RGB, dif_color: RGB, spe_color: RGB, shine: Real) -> None:
        self.amb_color = amb_color
        self.dif_color = dif_color
        self.spe_color = spe_color
        self.shine = shine

    @property
    def amb_color(self) -> RGB:
        return self._amb_color

    @amb_color.setter
    def amb_color(self, value: RGB) -> None:
        self._amb_color = value

    @property
    def dif_color(self) -> RGB:
        return self._dif_color

    @dif_color.setter
    def dif_color(self, value: RGB) -> None:
        self._dif_color = value

    @property
    def spe_color(self) -> RGB:
        return self._spe_color

    @spe_color.setter
    def spe_color(self, value: RGB) -> None:
        self._spe_color = value

    @property
    def shine(self) -> Real:
        return self._shine

    @shine.setter
    def shine(self, value: Real) -> None:
        self._shine = value
