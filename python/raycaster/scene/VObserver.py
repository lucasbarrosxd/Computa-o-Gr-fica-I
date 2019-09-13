# Importar bibliotecas.
# # Tipagem.
from numbers import Integral, Real
from typing import Tuple
# Importar do projeto.
from python.raycaster.physics import Point, Vector, Line
# Importar do pacote.
from . import Panel


class VObserver:
    def __init__(self, panel: Panel) -> None:
        self.panel = panel

    @classmethod
    def a(cls,
          panel_center: Point,
          normal: Vector,
          res: Tuple[Integral, Integral],
          size: Tuple[Real, Real]) -> "VObserver":
        return cls(Panel(panel_center, normal, res, size))

    @classmethod
    def b(cls, panel: Panel) -> "VObserver":
        return cls(panel)

    @property
    def panel(self) -> Panel:
        return self._panel

    @panel.setter
    def panel(self, value: Panel) -> None:
        self._panel = value

    def shoot(self, index_x: Integral, index_y: Integral) -> Line:
        return Line(self.panel.point(index_x, index_y), self.panel.normal)
