# scikit-image (también conocida como skimage) 

Es una biblioteca de Python que contiene una colección de algoritmos para el procesamiento de imágenes y visión por computadora. Para abrir y guardar imágenes en skimage, se puede usar funciones de otras bibliotecas como matplotlib o imageio.

Para cambiar la información de color y reescalar imágenes, se pueden usar las funciones del subpaquete transform. Por ejemplo, para reescalar una imagen en escala de grises puedes usar la función rescale:

        from skimage import data, color
        from skimage.transform import rescale

        image = color.rgb2gray(data.astronaut())
        image_rescaled = rescale(image, 0.25, anti_aliasing=False)

Para trabajar con imágenes a color se debe especificar el parámetro multichannel=True al llamar a la función rescale.

        im_rescaled = rescale(im, 0.25, multichannel=True)

Esto dará una imagen reescalada con todos los canales de color esperados 3.


# Pasos del algoritmo

- Pasos
- Rutas de archivos y funciones
    - crear una variable con el nombre del archivo
    - Establecer la ruta de este archivo
    - A la ruta del archivo hay que quitarle en el nombre del archivo
    - Se importan los directorios de imágenes, Cifrado AES, y LSB
    - Seleccionar la imagen conformae a la carpeta IMG
    - Lee la imagen y la reescala a 480x640
    - Mostrar la imagen
- Conversión de RGB a YCBR
    - toma la info de color
    - transforma esa info a YCbCr
    - Muestra la imagen sin la información de Cb y Cr
    - Obiene la info de alto y ancho
    - Obtiene la info de color Cb
    - Obtiene la info de color Cr
- Procesamiento de la información de color