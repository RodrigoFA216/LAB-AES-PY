import cv2
import os
import numpy as np
from scipy.ndimage import zoom
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

archivo = 'cypher.py'
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

# Convierte los canales Y, Cb, Cr a bytes
y_bytes = y.tobytes()
cb_bytes = cb.tobytes()
cr_bytes = cr.tobytes()

# Genera una clave aleatoria y un objeto Fernet para cifrar
clave = Fernet.generate_key()
f = Fernet(clave)

# Cifra los canales Y, Cb, Cr usando el algoritmo AES en modo OFB
backend = default_backend()
iv = os.urandom(16)
aes = Cipher(algorithms.AES(clave), modes.OFB(iv), backend=backend)
encryptor = aes.encryptor()
y_cif = encryptor.update(y_bytes) + encryptor.finalize()
cb_cif = encryptor.update(cb_bytes) + encryptor.finalize()
cr_cif = encryptor.update(cr_bytes) + encryptor.finalize()

# Descifra los canales Y, Cb, Cr usando el mismo algoritmo AES en modo OFB
decryptor = aes.decryptor()
y_descif = decryptor.update(y_cif) + decryptor.finalize()
cb_descif = decryptor.update(cb_cif) + decryptor.finalize()
cr_descif = decryptor.update(cr_cif) + decryptor.finalize()

# Convierte los canales Y, Cb, Cr de vuelta a matrices de imagen y las guarda
y_descif = np.frombuffer(y_descif, dtype=np.uint8).reshape((height, width))
cb_descif = np.frombuffer(cb_descif, dtype=np.uint8).reshape((height, width))
cr_descif = np.frombuffer(cr_descif, dtype=np.uint8).reshape((height, width))
img_yuv_descif = cv2.merge((y_descif, cb_descif, cr_descif))
img_descif = cv2.cvtColor(img_yuv_descif, cv2.COLOR_YCrCb2BGR)
cv2.imwrite(carpeta_cif+'Fondo Sakura_cifrado.jpg', img_cif)
cv2.imwrite(carpeta_cif+'Fondo Sakura_descifrado.jpg', img_descif)
