import skimage.io
import skimage.color

# Cargamos la imagen
img = skimage.io.imread('imagen.bmp')

# Comprobamos si la imagen está en el espacio de color YCbCr
if img.ndim == 3 and img.shape[2] == 3 and img.dtype == 'uint8':
    img_y_cb_cr = skimage.color.rgb2ycbcr(img)
    print('La imagen está en el espacio de color YCbCr')
else:
    print('La imagen no está en el espacio de color YCbCr')

# Obtenemos los valores de los píxeles en el espacio de color YCbCr
pixels = img_y_cb_cr.reshape(-1, 3)

# Mostramos los valores de los píxeles en la terminal
for i in range(10):   # muestra solo los primeros 10 píxeles para simplificar la salida en la terminal
    print('Pixel', i+1, ':', pixels[i])
