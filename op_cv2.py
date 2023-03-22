import cv2
import os

# Abrir la imagen en formato RGB
img = cv2.imread('ruta/a/la/imagen.jpg', cv2.IMREAD_COLOR)

# Convertir la imagen de RGB a YCbCr
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Separar las componentes Y, Cb y Cr en diferentes variables
y, cb, cr = cv2.split(img_yuv)

# Guardar las imagenes de cada componente por separado usando OpenCV
cv2.imwrite('ruta/a/la/componente-Y.jpg', y)
cv2.imwrite('ruta/a/la/componente-Cb.jpg', cb)
cv2.imwrite('ruta/a/la/componente-Cr.jpg', cr)
