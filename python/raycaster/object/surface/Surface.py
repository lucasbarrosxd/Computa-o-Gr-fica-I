# Importar bibliotecas.
# # Tipagem.
from typing import Optional, Union
# Importar do projeto.
from python.raycaster.physics import Point, Vector, Line


class Surface:
    def normal_projection(self, point: Point) -> Optional[Vector]:
        # Normal em um dado ponto da superfície.
        raise NotImplementedError

    def intersection(self, line: Line, coef: bool = True, fwrd: bool = True) -> Optional[Union[Point, float]]:
        # Inteseção entre a superfície e uma reta.
        # coef = retornar coeficiente ao invés do ponto.
        # fwrd = retornar apenas interseções com coef >= 0.
        raise NotImplementedError
