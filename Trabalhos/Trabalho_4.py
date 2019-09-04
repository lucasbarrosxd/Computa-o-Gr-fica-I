# Importar arquivos do projeto.
from python.raycaster.physics import *
from python.raycaster.observer import Scene, Observer
from python.raycaster.object.surface import Triangle, Plane, Cone, Cylinder, Sphere
# Importar bibliotecas.
from PIL import Image, ImageDraw
import time


mode = 'RGB'
white = (255, 255, 255)
black = (0, 0, 0)
light_blue = (0, 181, 204)
dark_blue = (50, 50, 200)
light_green = (46, 204, 113)
dark_green = (24, 102, 56)
red = (255, 0, 0)
brown = (247, 202, 24)

# Fazer o raycast.
res = (500, 500)
observer_1 = Observer.A(Point(0, 0, 0), Point(5, 0, 0), res, size=(10, 10))
observer_2 = Observer.A(Point(0, 2.5, 0), Point(5, 2.25, 0), res, size=(8, 8))
observer_t = Observer.A(Point(5, 5, 30), Point(5, 5, 27), res, size=(7, 7))

observer = observer_t

im = Image.new(mode=mode, size=res, color=light_blue)
draw = ImageDraw.Draw(im)

# Objetos Teste
sphere_1 = Sphere(Point(5, 2.5, 5), 2.5)
sphere_2 = Sphere(Point(5, 7.5, 5), 2.5)
sphere_3 = Sphere(Point(5, 12.5, 5), 2.5)
plane = Plane(Point(0, 0, 0), Vector(0, 1, 0))
triangle = Triangle(Point(8, 0, 0), Point(7.5, 2, 1), Point(7, 0, 2))
# Objetos Trabalho
cyli_1 = Cylinder.B(Point(2, 0, 8), Point(2, 7, 8), 1)
cyli_2 = Cylinder.B(Point(7, 0, 8), Point(7, 7, 8), 1)
cone_1 = Cone(Point(2, 7, 8), Point(2, 13, 8), 1.5)
cone_2 = Cone(Point(7, 7, 8), Point(7, 13, 8), 1.5)

# Cenário
scene = Scene()
#scene.add_obj(plane, "ground", light_green)
#scene.add_obj(sphere_1, "building_1", red)
#scene.add_obj(sphere_2, "building_2", white)
#scene.add_obj(sphere_3, "building_3", black)
scene.add_obj(cyli_1, "tree_trunk_1", brown)
#scene.add_obj(cone_1, "tree_leaves_1", dark_green)
scene.add_obj(cyli_2, "tree_trunk_2", brown)
#scene.add_obj(cone_2, "tree_leaves_2", dark_green)


for x_index in range(observer.panel.res[1]):
    for y_index in range(observer.panel.res[0]):
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
            draw.point((x_index, y_index), scene.objects[min_obj][2])

image_path = '../Debug/'
image_name = time.strftime("%H%M%S %d-%m-%Y") + '.png'
im.save(image_path + image_name)

im.show()
