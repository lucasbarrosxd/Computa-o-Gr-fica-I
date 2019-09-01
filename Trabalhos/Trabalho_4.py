from PIL import *
from PIL import Image, ImageDraw

def newImage(mode, size, color=0):

    im = Image.new(mode, size, color)
    return im

mode = 'RGBA'
size = (600, 600)
color = (0, 0, 0)

im = newImage(mode=mode, size=size, color=color)

draw =ImageDraw.Draw(im)
white = (255, 255, 255)
for i in range(0,600):
    draw.point((i, i), white)
    draw.point((600-i, i), white)

image_path = '/home/bit/Documentos/2019.2/Computa-o-Gr-fica-I'
image_name = 'imagemInicial.png'
im.save(image_path + image_name)

im.show()
