from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Definir la clave de cifrado y el vector de inicialización
key = get_random_bytes(16)
iv = get_random_bytes(16)

# Ruta de la imagen original
ruta_imagen_original = "ruta/a/la/imagen/original.png"

# Abrir la imagen original y convertirla en bytes
with open(ruta_imagen_original, "rb") as f:
    imagen_original_bytes = f.read()

# Cifrar la imagen original utilizando AES en modo OFB
cipher = AES.new(key, AES.MODE_OFB, iv)
imagen_cifrada_bytes = cipher.encrypt(
    pad(imagen_original_bytes, AES.block_size))

# Ruta donde se guardará la imagen cifrada
ruta_imagen_cifrada = "ruta/donde/se/guardara/la/imagen/cifrada.png"

# Guardar la imagen cifrada en el disco
with open(ruta_imagen_cifrada, "wb") as f:
    f.write(imagen_cifrada_bytes)

# Leer la imagen cifrada y descifrarla utilizando AES en modo OFB
with open(ruta_imagen_cifrada, "rb") as f:
    imagen_cifrada_bytes = f.read()

cipher = AES.new(key, AES.MODE_OFB, iv)
imagen_descifrada_bytes = unpad(
    cipher.decrypt(imagen_cifrada_bytes), AES.block_size)

# Ruta donde se guardará la imagen descifrada
ruta_imagen_descifrada = "ruta/donde/se/guardara/la/imagen/descifrada.png"

# Guardar la imagen descifrada en el disco
with open(ruta_imagen_descifrada, "wb") as f:
    f.write(imagen_descifrada_bytes)
