import cv2
import os
import numpy as np


# Rutas de archivos y funciones
# >crear una variable con el nombre del archivo
archivo = 'op_cv2.py'
# >Establecer la ruta de este archivo
ruta_actual = os.path.abspath(__file__)
# >A la ruta del archivo hay que quitarle en el nombre del archivo
ruta_actual = ruta_actual[:-len(archivo)]
# >Se importan los directorios de imágenes, Cifrado AES, y LSB
# AES y LSB se importan en la cabecera
carpeta_img = ruta_actual+"\Img\ "
carpeta_cif = ruta_actual+"\ImgCif\ "
carpeta_save = ruta_actual+"\ImgYCbCr\ "
# >Seleccionar la imagen conformae a la carpeta IMG
img_pull = carpeta_img[:-1]+'2.bmp'
# >Lee la imagen y la reescala a 480x640
img = cv2.imread(img_pull, cv2.IMREAD_COLOR)
img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)
# >Mostrar la imagen
# este paso se puede omitir para la API
# cv2.imshow('Imagen reescalada', img)
# cv2.waitKey(0) # ojo, esto requiere que se agreguen las lineas "cv2.waitKey(0)" y "cv2.destroyAllWindows()" al final del script
# Guardo la informacion RGB
b, g, r = cv2.split(img)
r = cv2.merge([np.zeros_like(r), np.zeros_like(r), r])  # bgr
g = cv2.merge([np.zeros_like(g), g, np.zeros_like(g)])  # bgr
b = cv2.merge([b, np.zeros_like(b), np.zeros_like(b)])  # bgr
cv2.imwrite(carpeta_save[:-1]+"\componente-R.bmp", r)
cv2.imwrite(carpeta_save[:-1]+"\componente-G.bmp", g)
cv2.imwrite(carpeta_save[:-1]+"\componente-B.bmp", b)
# Conversión de RGB a YCBR
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
# >toma la info de color
# >transforma esa info a YCbCr
# separo las componentes Y, Cb y Cr en diferentes variables
y, cb, cr = cv2.split(img_yuv)
# >Muestra la imagen sin la información de Cb y Cr
cv2.imwrite(carpeta_save[:-1]+"\componente-y.bmp", y)
cv2.imwrite(carpeta_save[:-1]+"\componente-cb.bmp", cb)
cv2.imwrite(carpeta_save[:-1]+"\componente-cr.bmp", cr)

ycb = cv2.merge([y, cb, np.zeros_like(cb)])
ycr = cv2.merge([y, np.zeros_like(cr), cr])
cv2.imwrite(carpeta_save[:-1]+"\componente-ycb.bmp", ycb)
cv2.imwrite(carpeta_save[:-1]+"\componente-ycr.bmp", ycr)


# >Obiene la info de alto y ancho
# >Obtiene la info de color Cb
# >Obtiene la info de color Cr
# Procesamiento de la información de color


# Guardar las imagenes de cada componente por separado usando OpenCV
# cv2.imwrite('ruta/a/la/componente-Y.jpg', y)
# cv2.imwrite('ruta/a/la/componente-Cb.jpg', cb)
# cv2.imwrite('ruta/a/la/componente-Cr.jpg', cr)


# # Redimensionar la componente Cb
# cb_resized2 = zoom(cb, (128/cb.shape[0], 128/cb.shape[1]), order=3)
# cb_resized2 = np.uint8(cb_resized2)

# cv2.imwrite(carpeta_save[:-1]+"\componente-cb-resized-2.bmp", cb_resized2)