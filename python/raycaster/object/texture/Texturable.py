from python.raycaster.physics import Point, Line
from typing import Union


class Texturable:
    def color(self, location: Union[Point, float], line: Line):
        raise NotImplementedError
