import cv2
import os
import numpy as np
from scipy.ndimage import zoom

archivo = 'resizerV2.py'
ruta_actual = os.path.abspath(__file__)
ruta_actual = ruta_actual[:-len(archivo)]
carpeta_img = ruta_actual+"\Img\ "
carpeta_cif = ruta_actual+"\ImgCif\ "
carpeta_save = ruta_actual+"\ImgYCbCr\ "
img_pull = carpeta_img[:-1]+'Fondo Sakura.jpg'
img_final = carpeta_save[:-1]+'Final-image-rgb.jpg'
img = cv2.imread(img_pull, cv2.IMREAD_COLOR)
height, width, channels = img.shape
resize_height = height//2
resize_width = width//2
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
y, cb, cr = cv2.split(img_yuv)

# ------------------------------------------------------------------------------
# ---------------------------Reducir componentes--------------------------------
# ------------------------------------------------------------------------------
# Reducir la componente Cb
cb_redux = cv2.resize(cb, (resize_width, resize_height),
                      interpolation=cv2.INTER_CUBIC)
# Aplicar antialiasing
cb_redux_smooth = cv2.GaussianBlur(cb_redux, (3, 3), 0)

# Reducir la componente Cr
cr_redux = cv2.resize(cr, (resize_width, resize_height),
                      interpolation=cv2.INTER_CUBIC)
# Aplicar antialiasing
cr_redux_smooth = cv2.GaussianBlur(cr_redux, (3, 3), 0)

# Guardar las imagenes resultantes
cv2.imwrite(carpeta_save[:-1]+"\componente-cb-min-blur.bmp", cb_redux_smooth)
cv2.imwrite(carpeta_save[:-1]+"\componente-cr-min-blur.bmp", cr_redux_smooth)

# ------------------------------------------------------------------------------
# -------------------------Restaurar componentes--------------------------------
# ------------------------------------------------------------------------------

# Redimensionar las componentes de color
cb_redim = cv2.resize(cb_redux_smooth, (width, height),
                      interpolation=cv2.INTER_CUBIC)
cr_redim = cv2.resize(cr_redux_smooth, (width, height),
                      interpolation=cv2.INTER_CUBIC)
# Aplicar GaussianBlur
cb_redim_smooth = cv2.GaussianBlur(cb_redim, (3, 3), 0)
cr_redim_smooth = cv2.GaussianBlur(cr_redim, (3, 3), 0)


# ------------------------------------------------------------------------------
# --------------------------Union de componentes--------------------------------
# ------------------------------------------------------------------------------

# Unión de componentes Y Cb Cr Smooth
merged_smooth = cv2.merge([y, cb_redim, cr_redim])
cv2.imwrite(carpeta_save[:-1]+"\Merged-smooth.bmp", merged_smooth)
img_rgb_smooth = cv2.cvtColor(merged_smooth, cv2.COLOR_YCrCb2BGR)
cv2.imwrite(carpeta_save[:-1]+"\Final-image-rgb.jpg", img_rgb_smooth)

img_original = img
img_resized = img_rgb_smooth
error = cv2.absdiff(img_original, img_resized)
error = error.astype(np.float32)
mse = np.mean(error**2)
psnr = 10 * np.log10(255**2 / mse)
print("PSNR: {:.2f} dB".format(psnr))
