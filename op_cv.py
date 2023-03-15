import cv2

# Cargamos la imagen
img = cv2.imread('imagen.bmp')

# Comprobamos si la imagen está en el espacio de color YCbCr
if cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb) is not None:
    print('La imagen está en el espacio de color YCbCr')
else:
    print('La imagen no está en el espacio de color YCbCr')

# Convertimos la imagen a modo YCbCr (independientemente del espacio de color original)
img_y_cb_cr = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Obtenemos los valores de los píxeles en el espacio de color YCbCr
pixels = img_y_cb_cr.flatten()

# Mostramos los valores de los píxeles en la terminal
for i in range(10):   # muestra solo los primeros 10 píxeles para simplificar la salida en la terminal
    print('Pixel', i+1, ':', pixels[i])
