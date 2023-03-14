from PIL import Image

# Cargo la imagen BMP original
# img = Image.open('Img/1.bmp')
img = Image.open('imagen_y_cb_cr.bmp')

# Convierto la imagen a modo YCbCr
img_y_cb_cr = img.convert('YCbCr')

# Comprobamos si la imagen está en el espacio de color YCbCr
if img.mode == 'YCbCr':
    print('La imagen está en el espacio de color YCbCr')
else:
    print('La imagen no está en el espacio de color YCbCr')

# Guardo la imagen en formato JPEG o PNG (ambos admiten la codificación YCbCr)
img_y_cb_cr.save('imagen_y_cb_cr.jpg')   # o 'imagen_y_cb_cr.png'

# Obtenemos los valores de los píxeles en el espacio de color YCbCr
pixels = img_y_cb_cr.getdata()

# Mostramos los valores de los píxeles en la terminal
for i in range(10):   # muestra solo los primeros 10 píxeles para simplificar la salida en la terminal
    print('Pixel', i+1, ':', pixels[i])

# Cargamos la nueva imagen en formato JPEG o PNG
img_y_cb_cr = Image.open('imagen_y_cb_cr.jpg')   # o 'imagen_y_cb_cr.png'

# Guardamos la nueva imagen en formato BMP
img_y_cb_cr.save('imagen_y_cb_cr.bmp')
