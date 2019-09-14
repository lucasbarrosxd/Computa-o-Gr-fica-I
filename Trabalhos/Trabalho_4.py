# Importar arquivos do projeto.
from python.raycaster.physics import *
from python.raycaster.scene import Scene, Observer
from python.raycaster.object.surface import Triangle, Plane, Cone, Cylinder, Sphere
# Importar bibliotecas.
from PIL import Image, ImageDraw
import time

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
res = (500, 500)
observer_1 = Observer.A(Point(0, 0, 0), Point(5, 0, 0), res, size=(10, 10))
observer_2 = Observer.A(Point(10, 20, 30), Point(9, 18, 26), res, size=(8, 8))
observer_t = Observer.A(Point(5, 5, 30), Point(5, 5, 27), res, size=(7, 7))
# Escolher o observador
observer = observer_2

im = Image.new(mode=mode, size=res, color=colors["light_blue"])
draw = ImageDraw.Draw(im)

# Objetos Teste
# Pontos dos cubos
p00 = Point(2.5, 0, 2.5)
p01 = Point(2.5, 0, 7.5)
p02 = Point(7.5, 0, 7.5)
p03 = Point(7.5, 0, 2.5)
p10 = Point(2.5, 5, 2.5)
p11 = Point(2.5, 5, 7.5)
p12 = Point(7.5, 5, 7.5)
p13 = Point(7.5, 5, 2.5)
p20 = Point(2.5, 10, 2.5)
p21 = Point(2.5, 10, 7.5)
p22 = Point(7.5, 10, 7.5)
p23 = Point(7.5, 10, 2.5)
p30 = Point(2.5, 15, 2.5)
p31 = Point(2.5, 15, 7.5)
p32 = Point(7.5, 15, 7.5)
p33 = Point(7.5, 15, 2.5)
# Triângulos do cubo.
t1 = Triangle(p00, p01, p02)
t2 = Triangle(p00, p03, p02)
t3 = Triangle(p01, p00, p10)
t4 = Triangle(p01, p11, p10)
t5 = Triangle(p03, p02, p12)
t6 = Triangle(p03, p13, p12)
t7 = Triangle(p10, p13, p23)
t8 = Triangle(p10, p20, p23)
t9 = Triangle(p12, p11, p21)
t10 = Triangle(p12, p22, p21)
t11 = Triangle(p21, p20, p30)
t12 = Triangle(p21, p31, p30)
t13 = Triangle(p23, p22, p32)
t14 = Triangle(p23, p33, p32)
t15 = Triangle(p01, p02, p12)
t16 = Triangle(p01, p11, p12)
t17 = Triangle(p03, p00, p10)
t18 = Triangle(p03, p13, p10)
t19 = Triangle(p10, p11, p21)
t20 = Triangle(p10, p20, p21)
t21 = Triangle(p12, p13, p23)
t22 = Triangle(p12, p22, p23)
t23 = Triangle(p21, p22, p32)
t24 = Triangle(p21, p31, p32)
t25 = Triangle(p23, p20, p30)
t26 = Triangle(p23, p33, p30)
t27 = Triangle(p30, p31, p32)
t28 = Triangle(p32, p33, p30)
sphere_1 = Sphere(Point(5, 2.5, 5), 2.5)
sphere_2 = Sphere(Point(5, 7.5, 5), 2.5)
sphere_3 = Sphere(Point(5, 12.5, 5), 2.5)
plane = Plane(Point(0, 0, 0), Vector(0, 1, 0))
triangle = Triangle(Point(8, 0, 0), Point(7.5, 2, 1), Point(7, 0, 2))
# Objetos Trabalho
cyli_1 = Cylinder.B(Point(0, 0, 10), Point(0, 4, 10), 0.5)
cyli_2 = Cylinder.B(Point(10, 0, 10), Point(10, 4, 10), 0.5)
cone_1 = Cone(Point(0, 4, 10), Point(0, 7, 10), 1.5)
cone_2 = Cone(Point(10, 4, 10), Point(10, 7, 10), 1.5)

# Cenário
scene = Scene()
scene.add_obj(plane, "ground", colors["light_green"])
scene.add_obj(sphere_1, "building_1", colors["red"])
scene.add_obj(sphere_2, "building_2", colors["white"])
scene.add_obj(sphere_3, "building_3", colors["black"])
scene.add_obj(cyli_1, "tree_trunk_1", colors["brown"])
scene.add_obj(cone_1, "tree_leaves_1", colors["dark_green"])
scene.add_obj(cyli_2, "tree_trunk_2", colors["brown"])
scene.add_obj(cone_2, "tree_leaves_2", colors["dark_green"])
scene.add_obj(t1, "building_1", colors["black"])
scene.add_obj(t2, "building_2", colors["red"])
scene.add_obj(t3, "building_3", colors["dark_green"])
scene.add_obj(t4, "building_4", colors["dark_blue"])
scene.add_obj(t5, "building_5", colors["white"])
scene.add_obj(t6, "building_6", colors["brown"])
scene.add_obj(t7, "building_7", colors["yellow"])
scene.add_obj(t8, "building_8", colors["orange"])
scene.add_obj(t9, "building_9", colors["magenta"])
scene.add_obj(t10, "building_10", colors["light_green"])
scene.add_obj(t11, "building_11", colors["yellow"])
scene.add_obj(t12, "building_12", colors["red"])
scene.add_obj(t13, "building_13", colors["white"])
scene.add_obj(t14, "building_14", colors["black"])
scene.add_obj(t15, "building_15", colors["dark_green"])
scene.add_obj(t16, "building_16", colors["orange"])
scene.add_obj(t17, "building_17", colors["magenta"])
scene.add_obj(t18, "building_18", colors["yellow"])
scene.add_obj(t19, "building_19", colors["light_green"])
scene.add_obj(t20, "building_20", colors["magenta"])
scene.add_obj(t21, "building_21", colors["dark_blue"])
scene.add_obj(t22, "building_22", colors["white"])
scene.add_obj(t23, "building_23", colors["red"])
scene.add_obj(t24, "building_24", colors["orange"])
scene.add_obj(t25, "building_25", colors["magenta"])
scene.add_obj(t26, "building_26", colors["black"])
scene.add_obj(t27, "building_27", colors["dark_green"])
scene.add_obj(t28, "building_28", colors["red"])

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
