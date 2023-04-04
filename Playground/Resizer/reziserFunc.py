import cv2
import os
import numpy as np
from scipy.ndimage import zoom

archivo = 'resizerFunc.py'
ruta_actual = os.path.abspath(__file__)
ruta_actual = ruta_actual[:-len(archivo)]
carpeta_img = ruta_actual+"\Img\ "
carpeta_cif = ruta_actual+"\ImgCif\ "
carpeta_save = ruta_actual+"\ImgYCbCr\ "
img_pull = carpeta_img[:-1]+'Fondo Sakura.jpg'
img_final = carpeta_save[:-1]+'Final-image-rgb.jpg'


def divide_components(path, name):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    height, width, channels = img.shape
    resize_height = height//2
    resize_width = width//2
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, cb, cr = cv2.split(img_yuv)

    # Reducir la componente Cb
    cb_redux = cv2.resize(cb, (resize_width, resize_height),
                          interpolation=cv2.INTER_CUBIC)
    # Aplicar antialiasing
    cb_redux_smooth = cv2.GaussianBlur(cb_redux, (3, 3), 0)

    # Reducir la componente Cr
    cr_redux = cv2.resize(cr, (resize_width, resize_height),
                          interpolation=cv2.INTER_CUBIC)
    # Aplicar antialiasing
    cr_redux_smooth = cv2.GaussianBlur(cr_redux, (3, 3), 0)

    # Guardar las imagenes resultantes
    cv2.imwrite(carpeta_save[:-1]+"-cb-min.bmp", cb_redux_smooth)
    cv2.imwrite(carpeta_save[:-1]+"-cr-min.bmp", cr_redux_smooth)
