import os
from PIL import Image

# Pasos
# Rutas de archivos y funciones
# >crear una variable con el nombre del archivo
# >Establecer la ruta de este archivo
# >A la ruta del archivo hay que quitarle en el nombre del archivo
# >Se importan los directorios de imágenes, Cifrado AES, y LSB
# >Seleccionar la imagen conformae a la carpeta IMG
# >Lee la imagen y la reescala a 480x640
# >Mostrar la imagen
# Conversión de RGB a YCBR
# >toma la info de color
# >transforma esa info a YCbCr
# >Muestra la imagen sin la información de Cb y Cr
# >Obiene la info de alto y ancho
# >Obtiene la info de color Cb
# >Obtiene la info de color Cr
# Procesamiento de la información de color
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
