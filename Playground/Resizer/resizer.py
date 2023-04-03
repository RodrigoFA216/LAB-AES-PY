import cv2
import os
import numpy as np
from scipy.ndimage import zoom

archivo = 'resizer.py'
ruta_actual = os.path.abspath(__file__)
ruta_actual = ruta_actual[:-len(archivo)]
carpeta_img = ruta_actual+"\Img\ "
carpeta_cif = ruta_actual+"\ImgCif\ "
carpeta_save = ruta_actual+"\ImgYCbCr\ "
img_pull = carpeta_img[:-1]+'Fondo Sakura.jpg'
img = cv2.imread(img_pull, cv2.IMREAD_COLOR)
img_original = cv2.imread(img_pull, cv2.IMREAD_COLOR)
resize_height = 480
resize_width = 640
min_height = 256
min_width = 256
height, width, channels = img.shape
img = cv2.resize(img, (resize_width, resize_height),
                 interpolation=cv2.INTER_AREA)
b, g, r = cv2.split(img)
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
y, cb, cr = cv2.split(img_yuv)

# Redimensionar la componente Cb
cb_resized = cv2.resize(cb, (min_width, min_height),
                        interpolation=cv2.INTER_CUBIC)
# Aplicar antialiasing
cb_resized_smooth = cv2.GaussianBlur(cb_resized, (3, 3), 0)
# Redimensionar la componente Cb
cr_resized = cv2.resize(cr, (min_width, min_height),
                        interpolation=cv2.INTER_CUBIC)
# Aplicar antialiasing
cr_resized_smooth = cv2.GaussianBlur(cr_resized, (3, 3), 0)
# Guardar las imagenes resultantes
# cv2.imwrite(carpeta_save[:-1]+"\componente-cb-min-blur.bmp", cb_resized_smooth)


# Redimensionar las componentes de color
cb_redim = cv2.resize(cb_resized_smooth, (resize_width, resize_height),
                      interpolation=cv2.INTER_LANCZOS4)
cr_redim = cv2.resize(cr_resized_smooth, (resize_width, resize_height),
                      interpolation=cv2.INTER_LANCZOS4)
# Aplicar GaussianBlur
cb_resized_smooth = cv2.GaussianBlur(cb_redim, (3, 3), 0)
cr_resized_smooth = cv2.GaussianBlur(cr_redim, (3, 3), 0)

merged_solid = cv2.merge([y, cb_redim, cr_redim])  # Y Cb Cr
# cv2.imwrite(carpeta_save[:-1]+"\Merged-smooth.bmp", merged_solid)

img_rgb_solid = cv2.cvtColor(merged_solid, cv2.COLOR_YCrCb2BGR)
# cv2.imwrite(carpeta_save[:-1]+"\Solid-rgb.bmp", img_rgb_solid)

img_final = cv2.resize(img_rgb_solid, (width, height),
                       interpolation=cv2.INTER_AREA)
cv2.imwrite(carpeta_save[:-1]+"\Final-image-rgb.bmp", img_final)

# Calcular el PSNR entre la imagen original y la reescalada
img_original = img_original
img_resized = img_final
error = cv2.absdiff(img_original, img_resized)
error = error.astype(np.float32)
mse = np.mean(error**2)
psnr = 10 * np.log10(255**2 / mse)
print("PSNR: {:.2f} dB".format(psnr))
