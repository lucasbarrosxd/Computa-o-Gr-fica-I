# Importar arquivos do pacote.
from .Observer import Observer


class Scenery:
    def __init__(self, observer: Observer) -> None:
        self.objects = {}
        self.observer = observer

    def add_obj(self, object, obj_name):
        self.objects[obj_name] = [object, True]

    def hide_obj(self, obj_name):
        instance_list = self.objects.get(obj_name, None)
        if instance_list is not None:
            self.objects[obj_name] = [instance_list[0], False]

    def remove_obj(self, obj_name):
        if self.objects.get(obj_name, None) is not None:
            del self.objects[obj_name]
