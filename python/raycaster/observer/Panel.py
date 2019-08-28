# Importar arquivos do projeto.
from python.raycaster.physics import Point, Vector


class Panel:
    def __init__(self, position: Point, normal: Vector, res_x: int, res_y: int, width: float, height: float, rotation: float):
        self.position = position
        self.normal = normal
        self.res_x = res_x
        self.res_y = res_y
        self.width = width
        self.height = height
        self.rotation = rotation

    @property
    def position(self) -> Point:
        return self._position

    @position.setter
    def position(self, value: Point) -> None:
        self._position = value

    @property
    def normal(self) -> Vector:
        return self._normal

    @normal.setter
    def normal(self, value: Vector) -> None:
        self._normal = value

    @property
    def res_x(self) -> int:
        return self._res_x

    @res_x.setter
    def res_x(self, value: int) -> None:
        self._res_x = value

    @property
    def res_y(self) -> int:
        return self._res_y

    @res_y.setter
    def res_y(self, value: int) -> None:
        self._res_y = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value: float) -> None:
        self._rotation = value

    def __str__(self):
        return "Pos:{0} N:{1} Res:{2}x{3} Size:{4}x{5} º:{6}".format(
            self.position, self.normal, self.res_x, self.res_y, self.width, self.height, self.rotation
        )
