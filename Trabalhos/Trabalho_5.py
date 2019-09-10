# Importar arquivos do projeto.
from python.raycaster.physics import *
from python.raycaster.observer import Scene, Observer
from python.raycaster.object.surface import Plane, Cone, Cylinder, Sphere
# Importar bibliotecas.
from PIL import Image, ImageDraw, ImageTk
import time
import tkinter as tk

# Cores
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

# Configurações
resolution = (500, 500)
image = Image.new(mode=mode, size=resolution)
pen = ImageDraw.Draw(image)

# Cenário
observer = Observer.A(Point(5, 5, 30), Point(5, 5, 27), resolution, size=(7, 7))
scene = Scene()
scene.add_obj(Plane(Point(0, 0, 0), Vector(0, 1, 0)), "ground", colors["light_green"])
scene.add_obj(Sphere(Point(5, 2.5, 5), 2.5), "ball", colors["dark_blue"])
scene.add_obj(Cylinder.B(Point(0, 0, 10), Point(0, 4, 10), 0.5), "tree_1_trunk", colors["brown"])
scene.add_obj(Cylinder.B(Point(10, 0, 10), Point(10, 4, 10), 0.5), "tree_2_trunk", colors["brown"])
scene.add_obj(Cone(Point(0, 4, 10), Point(0, 7, 10), 1.5), "tree_1_leaves", colors["dark_green"])
scene.add_obj(Cone(Point(10, 4, 10), Point(10, 7, 10), 1.5), "tree_2_leaves", colors["dark_green"])

# Executar o raycast e desenhar na tela.
for y_index in range(resolution[1]):
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
            # Cor a ser desenhada = cor do objeto.
            color = scene.objects[min_obj][2]
        else:
            # Cor a ser desenhada = cor do plano de fundo.
            color = colors["light_blue"]

        pen.point((x_index, y_index), color)

# Save image.
image_path = '../Debug/'
image_name = time.strftime("%Y-%m-%d %H-%M-%S") + '.png'
image.save(image_path + image_name)


# Setup.
def onclick(event):
    # Refazer raycast nas coordenadas do clique.
    line = observer.shoot(event.x, event.y)

    obj_hits = dict()

    for obj_name in scene.objects:
        # Check if visibility is enabled for that object.
        if scene.objects[obj_name][1]:
            obj_hits[obj_name] = scene.objects[obj_name][0].intersection(line)
            print("{0} - Tipo: {1} - Estado: {2} - Cor: {3} - Colisão: {4}".format(
                obj_name,
                scene.objects[obj_name][0].__class__.__name__,
                "Visível" if scene.objects[obj_name][1] else "Invisível",
                scene.objects[obj_name][2],
                "Não" if obj_hits[obj_name] is None else obj_hits[obj_name]
            ), sep="", end="\n")
    min_obj = None

    for obj_hit, obj_coef in obj_hits.items():
        if min_obj is not None:
            if obj_coef is not None and obj_hits[min_obj] > obj_coef:
                min_obj = obj_hit
        else:
            if obj_coef is not None:
                min_obj = obj_hit

    if min_obj is not None:
        # Cor a ser desenhada = cor do objeto.
        print("Resultado: {0}".format(min_obj))
    else:
        # Cor a ser desenhada = cor do plano de fundo.
        print("Resultado: Plano de Fundo")


root = tk.Tk()
root.title("RayCaster")
root.bind("<Button-1>", onclick)
canvas = tk.Canvas(master=root, width=resolution[0], height=resolution[1])
canvas.pack()
# Carregar imagem na janela.
photo_image = ImageTk.PhotoImage(image, master=root)
photo_id = canvas.create_image((0, 0), image=photo_image, anchor=tk.NW)
# Abrir janela.
root.mainloop()
