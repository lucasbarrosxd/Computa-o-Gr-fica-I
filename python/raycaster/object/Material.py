# Importar do pacote.
from . import Surface, Texture


class Material:
    def __init__(self, surface: Surface, texture: Texture) -> None:
        self.surface = surface
        self.texture = texture

    @property
    def surface(self) -> Surface:
        return self._surface

    @surface.setter
    def surface(self, value: Surface) -> None:
        self._surface = value

    @property
    def texture(self) -> Texture:
        return self._texture

    @texture.setter
    def texture(self, value: Texture) -> None:
        self._texture = value
