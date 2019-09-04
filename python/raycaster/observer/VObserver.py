# Importar arquivos do pacote.
from .Panel import Panel
from .Scene import Scene
# Importar arquivos do projeto.
from python.raycaster.physics import Point, Vector, Line
# Importar bibliotecas.
from typing import Tuple, List


class VObserver:
    def __init__(self, panel: Panel) -> None:
        self.panel = panel

    @classmethod
    def A(cls, panel_center: Point, normal: Vector, res: Tuple[int, int], size: Tuple[float, float]) -> "VObserver":
        return cls(Panel(panel_center, normal, res, size))

    @classmethod
    def B(cls, panel: Panel) -> "VObserver":
        return cls(panel)

    @property
    def panel(self) -> Panel:
        return self._panel

    @panel.setter
    def panel(self, value) -> None:
        self._panel = value

    def shoot(self, index_x: int, index_y: int) -> Line:
        return Line(self.panel.point(index_x, index_y), self.panel.normal)

    def render(self, scenery: Scene, mode: str = 'RGB') -> List[List[Tuple[int, int, int]]]:
        pixels = []

        for y_index in range(self.panel.res[1]):
            pixels.append([])
            for x_index in range(self.panel.res[0]):
                line = self.shoot(x_index, y_index)
                min_coef = None

                for obj_name in scenery.objects:
                    coef = scenery.objects[obj_name]

                if min_coef is None:
                    # No collisions, render background.
                    pass

        return pixels
