# Importar do projeto.
from python.raycaster.physics import Point, Line
# Importar bibliotecas.
from typing import Union


class Intersectionable:
    def intersection(self, line: Line, coef: bool = True, fwrd: bool = True)\
            -> Union[None, Point, float]:
        raise NotImplementedError
