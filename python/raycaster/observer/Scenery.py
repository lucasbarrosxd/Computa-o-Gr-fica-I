# Importar arquivos do pacote.
from .Observer import Observer
# Importar arquivos do projeto.
from python.raycaster.physics import Line
# Importar bibliotecas.
from typing import Tuple


class Scenery:
    def __init__(self, observer: Observer) -> None:
        self.objects = {}
        self.observer = observer

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

    def shoot(self, index_x: int, index_y: int) -> bool:
        line = self.observer.line(index_x, index_y)
        for obj_name in self.objects:
            if self.objects[obj_name][1] and self.objects[obj_name][0] @ line:
                return True
