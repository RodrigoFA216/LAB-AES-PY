import os
from PIL import Image


def readImageOs(pathImg):
    with open(pathImg, "rb") as img_or:
        img_or_data = img_or.read()
    return img_or_data
    # img = pil.Image.open(io.BytesIO(img_or_data))


def readImagePil(pathImg):
    img_or_pil = Image.open(pathImg)


path = "./Img/1.bmp"

dataOs = readImageOs(path)
dataPil = readImagePil(path)

if dataOs == dataPil:
    print("equal")
    print(type(dataOs))
    print(type(dataPil))
elif dataOs != dataPil:
    print("unequal")
    print(type(dataOs))
    print(type(dataPil))
