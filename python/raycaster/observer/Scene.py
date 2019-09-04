# Importar bibliotecas.
from typing import Tuple, List


class Scene:
    def __init__(self) -> None:
        self.objects = {}
        self.lights = {}

    def add_obj(self, renderable_object, obj_name: str, color: Tuple[int, int, int]) -> None:
        self.objects[obj_name] = [renderable_object, True, color]

    def hide_obj(self, obj_name: str) -> None:
        if obj_name in self.objects:
            self.objects[obj_name][1] = False
        else:
            raise KeyError

    def show_obj(self, obj_name: str) -> None:
        if obj_name in self.objects:
            self.objects[obj_name][1] = True
        else:
            raise KeyError

    def remove_obj(self, obj_name: str) -> None:
        if obj_name in self.objects:
            del self.objects[obj_name]
        else:
            raise KeyError
