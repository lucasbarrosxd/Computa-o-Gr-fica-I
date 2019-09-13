# Importar bibliotecas.
# # Tipagem.
from typing import Dict, List, Text, Union
# Importar do projeto.
from python.raycaster.light import Light
from python.raycaster.object import Material


class Scene:
    def __init__(self) -> None:
        self.objects: Dict[Text, List[Union[Material, bool]]] = dict()
        self.lights: Dict[Text, List[Union[Light, bool]]] = dict()

    def add_obj(self, obj_name: Text, renderable_object: Material) -> None:
        self.objects[obj_name] = [renderable_object, True]

    def hide_obj(self, obj_name: Text) -> None:
        if obj_name in self.objects:
            self.objects[obj_name][1] = False
        else:
            raise KeyError

    def show_obj(self, obj_name: Text) -> None:
        if obj_name in self.objects:
            self.objects[obj_name][1] = True
        else:
            raise KeyError

    def remove_obj(self, obj_name: Text) -> None:
        if obj_name in self.objects:
            del self.objects[obj_name]
        else:
            raise KeyError

    def add_light(self, light_name: Text, light: Light) -> None:
        self.lights[light_name] = [light, True]

    def hide_light(self, light_name: Text) -> None:
        if light_name in self.lights:
            self.objects[light_name][1] = False
        else:
            raise KeyError

    def show_light(self, light_name: Text) -> None:
        if light_name in self.lights:
            self.objects[light_name][1] = True
        else:
            raise KeyError

    def remove_light(self, light_name: Text) -> None:
        if light_name in self.lights:
            del self.objects[light_name]
        else:
            raise KeyError
