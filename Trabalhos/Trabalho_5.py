# Importar arquivos do projeto.
from python.raycaster.physics import *
from python.raycaster.observer import Scene, Observer
from python.raycaster.object.surface import Plane, Cone, Cylinder, Sphere
# Importar bibliotecas.
import turtle

# Colors
mode = 'RGB'
colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "light_blue": (0, 181, 204),
    "dark_blue": (50, 50, 200),
    "light_green": (46, 204, 113),
    "dark_green": (24, 102, 56),
    "red": (255, 0, 0),
    "orange": (255, 165, 0),
    "yellow": (247, 202, 24),
    "brown": (94, 77, 41),
    "magenta": (202, 31, 123)
}
# Config
resolution = (50, 50)
observer = Observer.A(Point(5, 5, 30), Point(5, 5, 27), resolution, size=(7, 7))
scene = Scene()
# Scene Objects
scene.add_obj(Plane(Point(0, 0, 0), Vector(0, 1, 0)), "ground", colors["light_green"])
scene.add_obj(Sphere(Point(5, 2.5, 5), 2.5), "ball", colors["dark_blue"])
scene.add_obj(Cylinder.B(Point(0, 0, 10), Point(0, 4, 10), 0.5), "tree_1_trunk", colors["brown"])
scene.add_obj(Cylinder.B(Point(10, 0, 10), Point(10, 4, 10), 0.5), "tree_2_trunk", colors["brown"])
scene.add_obj(Cone(Point(0, 4, 10), Point(0, 7, 10), 1.5), "tree_1_leaves", colors["dark_green"])
scene.add_obj(Cone(Point(10, 4, 10), Point(10, 7, 10), 1.5), "tree_2_leaves", colors["dark_green"])


def onclick(x_index, y_index):
    # Re-executar o raycast naquela coordenada e mostrar os resultados.
    print(x_index, y_index)


# Objetos básicos para desenho.
screen = turtle.Screen()
pen = turtle.Pen()
# Configurar tela.
screen.title("RayCaster")
screen.onclick(onclick, 1, False)
# Configurar a caneta.
pen.penup()
pen.clear()
# Executar o raycast e desenhar na tela.
for y_index in range(resolution[1]):
    pen.setpos(- resolution[0] / 2 + 1, resolution[1] / 2 - 1 - y_index)
    for x_index in range(resolution[0]):
        line = observer.shoot(x_index, y_index)
        min_coef = None
        min_obj = None

        for obj_name in scene.objects:
            # Check if visibility is enabled for that object.
            if scene.objects[obj_name][1]:
                result = scene.objects[obj_name][0].intersection(line)
                if result and (min_coef is None or result < min_coef):
                    min_coef = result
                    min_obj = obj_name

        if min_obj:
            # Desenhar objeto.
            color = [i / 255 for i in scene.objects[min_obj][2]]
            pen.dot(2, color)
        else:
            # Desenhar plano de fundo.
            color = [i / 255 for i in colors["light_blue"]]
            pen.dot(2, color)
        pen.forward(1)

# Escutar cliques e avisar à tela que pode executar.
screen.listen()
turtle.done()
# Fechar a tela.
screen.bye()
