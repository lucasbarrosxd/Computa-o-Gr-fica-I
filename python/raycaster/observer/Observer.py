# Importar arquivos do pacote.
from .Panel import Panel
from .Scene import Scene
# Importar arquivos do projeto.
from python.raycaster.physics import Point, Line
# Importar bibliotecas.
from typing import Tuple, List


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

    def render(self, scene: Scene) -> List[Tuple[int, int, int]]:
        pixels = []

        for x_index in range(self.panel.res[1]):
            for y_index in range(self.panel.res[0]):
                line = self.shoot(x_index, y_index)
                min_coef = None
                min_obj = None

                for obj_name in scene.objects:
                    # Check if visibility is enabled for that object.
                    if scene.objects[obj_name][1]:
                        result = scene.objects[obj_name][0].intersection(line)
                        if result and (min_coef is None or result < min_coef):
                            min_coef = result
                            min_obj = obj_name

                pixels.append(scene.objects[min_obj][2])

        return pixels
