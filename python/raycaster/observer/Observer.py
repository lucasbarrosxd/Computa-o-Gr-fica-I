# Importar arquivos do pacote.
from .Panel import Panel
# Importar arquivos do projeto.
from python.raycaster.physics import Point, Line
# Importar bibliotecas.
from typing import Tuple


class Observer:
    def __init__(self, position: Point, panel: Panel) -> None:
        self.position = position
        self.panel = panel

    @classmethod
    def A(cls, observer_position: Point, panel_center: Point, res: Tuple[int, int], size: Tuple[float, float]) -> "Observer":
        return cls(observer_position, Panel(panel_center, panel_center - observer_position, res, size))

    @classmethod
    def B(cls, position: Point, panel: Panel) -> "Observer":
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
    def panel(self, value) -> None:
        self._panel = value

    def line(self, index_x: int, index_y: int) -> Line:
        panel_point = self.panel.point(index_x, index_y)

        return Line(panel_point, panel_point - self.position)

    def lines(self):
        for index_x in range(self.panel.res[0]):
            for index_y in range(self.panel.res[1]):
                if index_x != self.panel.res[0] or index_y != self.panel.res[1]:
                    yield self.line(index_x, index_y)
                else:
                    return self.line(index_x, index_y)
