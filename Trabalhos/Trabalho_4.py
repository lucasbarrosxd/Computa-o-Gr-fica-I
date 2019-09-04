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
blue = (50, 50, 200)
green = (46, 204, 113)
red = (255, 0, 0)
brown = (247, 202, 24)

# Fazer o raycast.
res = (300, 300)
observer_1 = Observer.A(Point(0, 0, 0), Point(5, 0, 0), res, size=(10, 10))
observer_2 = Observer.A(Point(0, 2.5, 0), Point(5, 2.25, 0), res, size=(8, 8))

observer = observer_2

im = Image.new(mode=mode, size=res, color=black)
draw = ImageDraw.Draw(im)

scene = Scene()
cyli = Cylinder.B(Point(10, -5, 0), Point(10, 2, 0), 5)
cone = Cone(Point(10, 0, 0), Point(10, 5, 0), 2)
plane = Plane(Point(0, 0, 0), Vector(0, 1, 0))
sphere = Sphere(Point(10, 2, 0), 2)
triangle = Triangle(Point(8, 0, 0), Point(7.5, 2, 1), Point(7, 0, 2))
scene.add_obj(sphere, "ball", blue)
scene.add_obj(plane, "ground", green)
scene.add_obj(triangle, "triangle", red)

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
