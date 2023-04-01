import cv2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Definir la clave de cifrado y el vector de inicialización
key = get_random_bytes(16)
iv = get_random_bytes(16)

# Ruta de la imagen original
ruta_imagen_original = "ruta/a/la/imagen/original.png"

# Cargar la imagen original con OpenCV
imagen_original = cv2.imread(ruta_imagen_original)

# Convertir la imagen original en bytes
imagen_original_bytes = cv2.imencode('.png', imagen_original)[1].tobytes()

# Cifrar la imagen original utilizando AES en modo OFB
cipher = AES.new(key, AES.MODE_OFB, iv)
imagen_cifrada_bytes = cipher.encrypt(
    pad(imagen_original_bytes, AES.block_size))

# Convertir la imagen cifrada de bytes a objeto NumPy
imagen_cifrada = cv2.imdecode(
    np.frombuffer(imagen_cifrada_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)

# Ruta donde se guardará la imagen cifrada
ruta_imagen_cifrada = "ruta/donde/se/guardara/la/imagen/cifrada.png"

# Guardar la imagen cifrada en el disco
cv2.imwrite(ruta_imagen_cifrada, imagen_cifrada)

# Leer la imagen cifrada y descifrarla utilizando AES en modo OFB
imagen_cifrada = cv2.imread(ruta_imagen_cifrada)

# Convertir la imagen cifrada en bytes
imagen_cifrada_bytes = cv2.imencode('.png', imagen_cifrada)[1].tobytes()

cipher = AES.new(key, AES.MODE_OFB, iv)
imagen_descifrada_bytes = unpad(
    cipher.decrypt(imagen_cifrada_bytes), AES.block_size)

# Convertir la imagen descifrada de bytes a objeto NumPy
imagen_descifrada = cv2.imdecode(
    np.frombuffer(imagen_descifrada_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)

# Ruta donde se guardará la imagen descifrada
ruta_imagen_descifrada = "ruta/donde/se/guardara/la/imagen/descifrada.png"

# Guardar la imagen descifrada en el disco
cv2.imwrite(ruta_imagen_descifrada, imagen_descifrada)
