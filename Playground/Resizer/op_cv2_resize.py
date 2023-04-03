import cv2
import os
import numpy as np
from scipy.ndimage import zoom

archivo = 'op_cv2_resize.py'
ruta_actual = os.path.abspath(__file__)
ruta_actual = ruta_actual[:-len(archivo)]
carpeta_img = ruta_actual+"\Img\ "
carpeta_cif = ruta_actual+"\ImgCif\ "
carpeta_save = ruta_actual+"\ImgYCbCr\ "
img_pull = carpeta_img[:-1]+'Fondo Sakura.jpg'
img = cv2.imread(img_pull, cv2.IMREAD_COLOR)
imagen_real = img
height, width, channels = img.shape
img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)
b, g, r = cv2.split(img)
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
y, cb, cr = cv2.split(img_yuv)

# Redimensionar la componente Cb
cb_resized = cv2.resize(cb, (128, 128), interpolation=cv2.INTER_CUBIC)
# Aplicar antialiasing
cb_resized_smooth = cv2.GaussianBlur(cb_resized, (3, 3), 0)
# Guardar la imagen resultante
cv2.imwrite(carpeta_save[:-1]+"\componente-cb-min-solid.bmp", cb_resized)
cv2.imwrite(carpeta_save[:-1]+"\componente-cb-min-blur.bmp", cb_resized_smooth)

# Redimensionar la componente Cr Smooth
cb_redim = cv2.resize(cb_resized_smooth, (640, 480),
                      interpolation=cv2.INTER_LANCZOS4)
# Aplicar GaussianBlur
cb_resized_smooth = cv2.GaussianBlur(cb_redim, (3, 3), 0)
# Guardar la imagen resultante
cv2.imwrite(carpeta_save[:-1] +
            "\componente-cr-resized-smooth.bmp", cb_resized_smooth)
cv2.imwrite(carpeta_save[:-1]+"\componente-cr-resized-solid.bmp", cb_redim)

# Guardar Imágenes
cv2.imwrite(carpeta_save[:-1]+"\componente-y.bmp", y)
cv2.imwrite(carpeta_save[:-1]+"\componente-cb.bmp", cb)
cv2.imwrite(carpeta_save[:-1]+"\componente-cr.bmp", cr)

merged_smooth = cv2.merge([y, cb_resized_smooth, cr])  # Y Cb Cr
cv2.imwrite(carpeta_save[:-1]+"\Merged-smooth.bmp", merged_smooth)

merged_solid = cv2.merge([y, cb_redim, cr])  # Y Cb Cr
cv2.imwrite(carpeta_save[:-1]+"\Merged-smooth.bmp", merged_solid)

neded = cv2.merge([y, cb, cr])  # Y Cb Cr
cv2.imwrite(carpeta_save[:-1]+"\Merged-neded.bmp", neded)

img_rgb = cv2.cvtColor(neded, cv2.COLOR_YCrCb2BGR)
cv2.imwrite(carpeta_save[:-1]+"\Merged-neded-rgb.bmp", img_rgb)

img_rgb_smooth = cv2.cvtColor(merged_smooth, cv2.COLOR_YCrCb2BGR)
cv2.imwrite(carpeta_save[:-1]+"\Smooth-rgb.bmp", img_rgb_smooth)

img_rgb_solid = cv2.cvtColor(merged_solid, cv2.COLOR_YCrCb2BGR)
cv2.imwrite(carpeta_save[:-1]+"\Solid-rgb.bmp", img_rgb_solid)

img_final = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
cv2.imwrite(carpeta_save[:-1]+"\Final-image-rgb.bmp", img_rgb_solid)

# Calcular el PSNR entre la imagen original y la reescalada
img_original = img
img_resized = img_rgb_solid
error = cv2.absdiff(img_original, img_resized)
error = error.astype(np.float32)
mse = np.mean(error**2)
psnr = 10 * np.log10(255**2 / mse)
print("PSNR: {:.2f} dB".format(psnr))
