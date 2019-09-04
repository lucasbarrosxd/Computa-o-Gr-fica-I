# Importar arquivos do pacote.
from .Panel import Panel
from .Scene import Scenery
# Importar arquivos do projeto.
from python.raycaster.physics import Point, Line
# Importar bibliotecas.
from typing import Tuple, List
from PIL import Image, ImageDraw


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

    def shoot(self, index_x: int, index_y: int) -> Line:
        panel_point = self.panel.point(index_x, index_y)

        return Line(panel_point, panel_point - self.position)

    def render(self, scenery: Scenery) -> List[Tuple[int, int, int]]:
        pixels = []

        for x_index in range(self.panel.res[1]):
            for y_index in range(self.panel.res[0]):
                line = self.shoot(x_index, y_index)
                min_coef = None

                for obj_name in scenery.objects:
                    if scenery.objects[obj_name].intersection(line):
                        pixels.append((255, 255, 255))

        return pixels


"""
                if min_coef is None:
                    # No collisions, render background.
                    pass"""