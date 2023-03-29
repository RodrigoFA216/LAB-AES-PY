import cv2
import os
import numpy as np
from scipy.ndimage import zoom

archivo = 'op_cv2_clean.py'
ruta_actual = os.path.abspath(__file__)
ruta_actual = ruta_actual[:-len(archivo)]
carpeta_img = ruta_actual+"\Img\ "
carpeta_cif = ruta_actual+"\ImgCif\ "
carpeta_save = ruta_actual+"\ImgYCbCr\ "
img_pull = carpeta_img[:-1]+'2.bmp'
img = cv2.imread(img_pull, cv2.IMREAD_COLOR)
img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)
b, g, r = cv2.split(img)
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
y, cb, cr = cv2.split(img_yuv)

# Redimensionar la componente Cb
cb_resized = cv2.resize(cb, (128, 128), interpolation=cv2.INTER_CUBIC)
# Aplicar antialiasing
cb_resized_smooth = cv2.GaussianBlur(cb_resized, (3, 3), 0)
# Guardar la imagen resultante
cv2.imwrite(carpeta_save[:-1]+"\componente-cb-resized.bmp", cb_resized_smooth)
# Guardar Imágenes
cv2.imwrite(carpeta_save[:-1]+"\componente-y.bmp", y)
cv2.imwrite(carpeta_save[:-1]+"\componente-cb.bmp", cb)
cv2.imwrite(carpeta_save[:-1]+"\componente-cr.bmp", cr)
