# Importar bibliotecas.
# # Tipagem.
from numbers import Integral, Real
from typing import Tuple


class Texture:
    def __init__(self,
                 amb_color: Tuple[Integral, Integral, Integral],
                 dif_color: Tuple[Integral, Integral, Integral],
                 spe_color: Tuple[Integral, Integral, Integral],
                 shine: Real) -> None:
        self.amb_color = amb_color
        self.dif_color = dif_color
        self.spe_color = spe_color
        self.shine = shine

    @property
    def amb_color(self) -> Tuple[Integral, Integral, Integral]:
        return self._amb_color

    @amb_color.setter
    def amb_color(self, value: Tuple[Integral, Integral, Integral]) -> None:
        if not 0 <= value[0] <= 255 and not 0 <= value[1] <= 255 and not 0 <= value[2] <= 255:
            raise ValueError

        self._amb_color = value

    @property
    def dif_color(self) -> Tuple[Integral, Integral, Integral]:
        return self._dif_color

    @dif_color.setter
    def dif_color(self, value: Tuple[Integral, Integral, Integral]) -> None:
        if not 0 <= value[0] <= 255 and not 0 <= value[1] <= 255 and not 0 <= value[2] <= 255:
            raise ValueError

        self._dif_color = value

    @property
    def spe_color(self) -> Tuple[Integral, Integral, Integral]:
        return self._spe_color

    @spe_color.setter
    def spe_color(self, value: Tuple[Integral, Integral, Integral]) -> None:
        if not 0 <= value[0] <= 255 and not 0 <= value[1] <= 255 and not 0 <= value[2] <= 255:
            raise ValueError

        self._spe_color = value

    @property
    def shine(self) -> Real:
        return self._shine

    @shine.setter
    def shine(self, value: Real) -> None:
        self._shine = value
