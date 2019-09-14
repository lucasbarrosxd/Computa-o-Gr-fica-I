# Importar do projeto.
from python.raycaster.auxi import RGB
from python.raycaster.physics import Point, Vector
from python.raycaster.object import Material
from python.raycaster.scene import Observer
# Importar do pacote.
from . import Light


class FocalLight(Light):
    def __init__(self, amb_light: RGB, dif_light: RGB, spe_light: RGB, origin: Point) -> None:
        super().__init__(amb_light=amb_light, dif_light=dif_light, spe_light=spe_light)
        self.origin = origin

    @property
    def origin(self) -> Point:
        return self._origin

    @origin.setter
    def origin(self, value: Point) -> None:
        self._origin = value

    def illuminate(self, material: Material, location: Point, observer: Observer) -> RGB:
        light_vector = Vector.b(location, self.origin)
        light_vector.norm = 1
        normal_vector = material.surface.normal_projection(location)
        normal_vector.norm = 1
        view_vector = Vector.b(location, observer.position)
        view_vector.norm = 1
        reflection_vector = 2 * (light_vector * normal_vector) * normal_vector - light_vector
        reflection_vector.norm = 1

        dif_coef = normal_vector * light_vector
        if dif_coef <= 0:
            dif_coef = 0
            spe_coef = 0
        else:
            spe_coef = max(0, view_vector * reflection_vector) ** material.texture.shine

        amb_result = material.texture.amb_color * self.amb_light
        dif_result = material.texture.dif_color * self.dif_light * dif_coef
        spe_result = material.texture.spe_color * self.spe_light * spe_coef

        return amb_result + dif_result + spe_result
