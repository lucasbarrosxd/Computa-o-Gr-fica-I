# Importar arquivos do projeto.
from python.raycaster.physics import *
from python.raycaster.observer import Scenery, Observer
from python.raycaster.object.r3d import Cone
# Importar bibliotecas.
from PIL import Image, ImageDraw


mode = 'RGB'
white = (255, 255, 255)
green = (46, 204, 113)
red = (255, 0, 0)
black = 0
res = (200, 100)

im = Image.new(mode=mode, size=res, color=black)

# Fazer o raycast.
observer = Observer.A(Point(0, 0, 0), Point(5, 0, 0), res, size=(10, 10))

scenery = Scenery()
cone = Cone(Point(10, 0, 0), Point(10, 5, 0), 2)
scenery.add_obj(cone, "cone", green)

lista = observer.render(scenery)

im.putdata(lista)

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