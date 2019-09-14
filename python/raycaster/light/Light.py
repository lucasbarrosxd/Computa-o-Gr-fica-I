# Importar do projeto.
from python.raycaster.auxi import RGB
from python.raycaster.physics import Point
from python.raycaster.object import Material
from python.raycaster.scene import Observer


class Light:
    def __init__(self, amb_light: RGB, dif_light: RGB, spe_light: RGB) -> None:
        self.amb_light = amb_light
        self.dif_light = dif_light
        self.spe_light = spe_light

    @property
    def amb_light(self) -> RGB:
        return self._amb_light

    @amb_light.setter
    def amb_light(self, value: RGB) -> None:
        self._amb_light = value

    @property
    def dif_light(self) -> RGB:
        return self._dif_light

    @dif_light.setter
    def dif_light(self, value: RGB) -> None:
        self._dif_light = value

    @property
    def spe_light(self) -> RGB:
        return self._spe_light

    @spe_light.setter
    def spe_light(self, value: RGB) -> None:
        self._spe_light = value

    def illuminate(self, material: Material, location: Point, observer: Observer) -> RGB:
        raise NotImplementedError
