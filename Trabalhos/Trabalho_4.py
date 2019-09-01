from PIL import *
from PIL import Image, ImageDraw

def newImage(mode, size, color=0):

    im = Image.new(mode, size, color)
    return im

mode = 'RGBA'
size = (640, 480)
color = (73, 109, 137)

im = newImage(mode=mode, size=size, color=color)


image_path = '/home/bit/Documentos/2019.2/Computa-o-Gr-fica-I'
image_name = 'imagemInicial.png'
im.save(image_path + image_name )

im.show()
