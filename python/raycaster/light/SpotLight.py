# Importar bibliotecas.
import math
# # Tipagem.
from numbers import Real
# Importar do projeto.
from python.raycaster.auxi import RGB
from python.raycaster.object import Material
from python.raycaster.physics import Point, Vector
# Importar do pacote.
from python.raycaster.scene import Observer
from .Light import Light


class SpotLight(Light):
    def __init__(self, amb_light: RGB, dif_light: RGB, spe_light: RGB, origin: Point, direction: Vector, angle: Real) \
            -> None:
        super().__init__(amb_light=amb_light, dif_light=dif_light, spe_light=spe_light)
        self.origin = origin
        self.direction = direction
        self.angle = angle

    @property
    def origin(self) -> Point:
        return self._origin

    @origin.setter
    def origin(self, value: Point) -> None:
        self._origin = value

    @property
    def direction(self) -> Vector:
        return self._direction

    @direction.setter
    def direction(self, value: Vector) -> None:
        self._direction = value

    @property
    def angle(self) -> Real:
        return self._angle

    @angle.setter
    def angle(self, value: Real) -> None:
        self._angle = value

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
            cos_coef = 0
        else:
            spe_coef = max(0, view_vector * reflection_vector) ** material.texture.shine

            max_cosine = math.cos(math.radians(self.angle))
            cos_coef = max(0.0, ((- light_vector) * self.direction) / self.direction.norm - max_cosine) \
                / (1 - max_cosine)

        amb_result = material.texture.amb_color * self.amb_light
        dif_result = material.texture.dif_color * self.dif_light * dif_coef * cos_coef
        spe_result = material.texture.spe_color * self.spe_light * spe_coef * cos_coef

        return amb_result + dif_result + spe_result
