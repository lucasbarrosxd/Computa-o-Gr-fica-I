# Importar arquivos do projeto.
from python.raycaster.auxi import RGB
from python.raycaster.light import FocalLight, FarLight, SpotLight
from python.raycaster.object import Material, Texture
from python.raycaster.object.surface import Plane, Sphere
from python.raycaster.physics import *
from python.raycaster.scene import Scene, Observer
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
    "navy_blue": (0, 0, 128),
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
observer = Observer.a(Point(-8, 10, -8), Point(-6, 9, -6), resolution, size=(7, 7))
scene = Scene()
background_color = colors["navy_blue"]
scene.add_obj("ground", Material(
    Plane(Point(0, 0, 0), Vector(0, 1, 0)),
    Texture(amb_color=RGB(0, 0, 0), dif_color=RGB(25, 89, 25), spe_color=RGB(4, 12, 2), shine=0.25)))
scene.add_obj("ball", Material(
    Sphere(Point(10, 5, 10), 5),
    Texture(amb_color=RGB(13, 13, 13), dif_color=RGB(127, 127, 127), spe_color=RGB(178, 178, 178), shine=0.78)))
scene.add_light("light_1", FocalLight(
    origin=Point(5, 0, 0),
    amb_light=RGB(10, 10, 6), dif_light=RGB(100, 100, 30), spe_light=RGB(180, 180, 48)))
scene.add_light("light_2", FarLight(
    direction=Vector(0, -10, 1),
    amb_light=RGB(30, 30, 40), dif_light=RGB(60, 60, 100), spe_light=RGB(90, 90, 120)))
scene.add_light("light_3", SpotLight(
    origin=Point(9, 15, 9), direction=Vector(1, -10, 1), angle=30,
    amb_light=RGB(50, 25, 25), dif_light=RGB(255, 100, 100), spe_light=RGB(255, 120, 120)
))

# Executar o raycast e desenhar na tela.
for y_index in range(resolution[1]):
    for x_index in range(resolution[0]):
        line = observer.shoot(x_index, y_index)
        min_coef = None
        min_obj = None

        for obj_name in scene.objects:
            # Check if visibility is enabled for that object.
            if scene.objects[obj_name][1]:
                result = scene.objects[obj_name][0].surface.intersection(line)
                if result and (min_coef is None or result < min_coef):
                    min_coef = result
                    min_obj = obj_name

        if min_obj:
            color = RGB(0, 0, 0)
            for light_name in scene.lights:
                color += scene.lights[light_name][0].illuminate(scene.objects[min_obj][0], line(min_coef), observer)
        else:
            # Cor a ser desenhada = cor do plano de fundo.
            color = RGB(0, 0, 0)
            for light_name in scene.lights:
                color += RGB(0, 0, 128) * scene.lights[light_name][0].amb_light

        pen.point((x_index, y_index), color.tuple)

# Save image.
image_path = '../Debug/'
image_name = time.strftime("%Y-%m-%d %H-%M-%S") + '.png'
image.save(image_path + image_name)


# Setup.
def onclick(event):
    print("Clique: ({0}, {1})".format(event.x, event.y))
    line = observer.shoot(event.x, event.y)
    min_coef = None
    min_obj = None

    for obj_name in scene.objects:
        # Check if visibility is enabled for that object.
        if scene.objects[obj_name][1]:
            result = scene.objects[obj_name][0].surface.intersection(line)
            if result and (min_coef is None or result < min_coef):
                min_coef = result
                min_obj = obj_name

            p = line(result) if result is not None else None
            print("{0} ('{1}', {2}) @ {3} {4}".format(
                obj_name,
                scene.objects[obj_name][0].surface.__class__.__name__,
                "Visível" if scene.objects[obj_name][1] else "Invisível",
                "Ponto: ({0:0.2f}, {1:0.2f}, {2:0.2f})".format(p.x, p.y, p.z) if p is not None else None,
                "Coef: {0:0.5f}".format(result) if result is not None else "")
            )

    if min_obj:
        color = RGB(0, 0, 0)
        for light_name in scene.lights:
            color += scene.lights[light_name][0].illuminate(scene.objects[min_obj][0], line(min_coef), observer)
        print("Interseção: {0}, Cor: {1}".format(min_obj, color))
    else:
        # Cor a ser desenhada = cor do plano de fundo.
        color = RGB(0, 0, 0)
        for light_name in scene.lights:
            color += RGB(0, 0, 128) * scene.lights[light_name][0].amb_light
        print("Interseção: Plano de Fundo, Cor: {0}".format(color))


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
