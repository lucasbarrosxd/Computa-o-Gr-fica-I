from python.raycaster.physics import *
from python.raycaster.observer import Scenery, Observer
from python.raycaster.renderable.r3d import Cone
from PIL import Image, ImageDraw


def new_image(mode, size, color=0):
    return Image.new(mode, size, color)


mode = 'RGB'
white = (255, 255, 255)
green = (46, 204, 113)
black = 0
res = (1920, 1080)

im = new_image(mode=mode, size=res, color=black)
draw = ImageDraw.Draw(im)

# Fazer o raycast.
cone = Cone(Point(10, 0, 0), Point(10, 5, 0), 2)

scenery = Scenery(Observer.A(Point(0, 0, 0), Point(5, 0, 0), res, size=(10, 10)))
scenery.add_obj(cone, "cone", green)

for index_x in range(res[0]):
    for index_y in range(res[1]):
        if scenery.shoot(index_x, res[1] - index_y - 1):
            draw.point((index_x, index_y), green)

image_path = '../Debug/'
image_name = 'imagemInicial.png'
im.save(image_path + image_name)

im.show()

for y in range(0,1000):
    for z in range(0, 1000):
        point = (x,y,z)
        z-zTrans
    z=zInicial
    y=y-yTrans

rigthTrans = 