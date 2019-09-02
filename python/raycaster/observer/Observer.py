# Importar arquivos do pacote.
from .Panel import Panel
# Importar arquivos do projeto.
from python.raycaster.physics import Point


class Observer:
    def __init__(self, position: Point, panel: Panel) -> None:
        self.position = position
        self.panel = panel
