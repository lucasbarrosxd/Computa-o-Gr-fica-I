# Importar bibliotecas.
# # Tipagem.
from numbers import Integral, Real
from typing import Tuple
# Importar do projeto.
from python.raycaster.physics import Point, Line
# Importar do pacote.
from .Panel import Panel


class Observer:
    def __init__(self, position: Point, panel: Panel) -> None:
        self.position = position
        self.panel = panel

    @classmethod
    def a(cls,
          observer_position: Point,
          panel_center: Point,
          res: Tuple[Integral, Integral],
          size: Tuple[Real, Real]) -> "Observer":
        return cls(observer_position, Panel(panel_center, panel_center - observer_position, res, size))

    @classmethod
    def b(cls, position: Point, panel: Panel) -> "Observer":
        return cls(position, panel)

    @property
    def position(self) -> Point:
        return self._position

    @position.setter
    def position(self, value: Point) -> None:
        self._position = value

    @property
    def panel(self) -> Panel:
        return self._panel

    @panel.setter
    def panel(self, value: Panel) -> None:
        self._panel = value

    def shoot(self, index_x: Integral, index_y: Integral) -> Line:
        panel_point = self.panel.point(index_x, index_y)

        return Line(panel_point, panel_point - self.position)
