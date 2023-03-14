import os
from PIL import Image

ruta_actual = os.path.abspath(__file__)
archivo = 'main.py'
ruta_actual = ruta_actual[:-len(archivo)]

print(ruta_actual, type(ruta_actual))

# Abre la imagen en modo RGB
imagen = Image.open('./img/1.bmp').convert('RGB')

# Convierte la imagen a YCbCr
imagen_ycbcr = imagen.convert('YCbCr')

# Muestra la imagen convertida
imagen_ycbcr.show()

# Ruta de guardado
ruta_guardado = ruta_actual+'ImgCif'

imagen_ycbcr.save("ImgCif/1Cif.jpg")
