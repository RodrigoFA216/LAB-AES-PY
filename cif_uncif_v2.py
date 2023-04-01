from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image

# Definir la clave de cifrado y el vector de inicialización
key = get_random_bytes(16)
iv = get_random_bytes(16)

# Ruta de la imagen original
ruta_imagen_original = "ruta/a/la/imagen/original.png"

# Abrir la imagen original y convertirla en bytes
imagen_original = Image.open(ruta_imagen_original)
imagen_original_bytes = imagen_original.tobytes()

# Cifrar la imagen original utilizando AES en modo OFB
cipher = AES.new(key, AES.MODE_OFB, iv)
imagen_cifrada_bytes = cipher.encrypt(
    pad(imagen_original_bytes, AES.block_size))

# Convertir la imagen cifrada de bytes a objeto Image
ancho, alto = imagen_original.size
imagen_cifrada = Image.frombytes("RGB", (ancho, alto), imagen_cifrada_bytes)

# Ruta donde se guardará la imagen cifrada
ruta_imagen_cifrada = "ruta/donde/se/guardara/la/imagen/cifrada.png"

# Guardar la imagen cifrada en el disco
imagen_cifrada.save(ruta_imagen_cifrada)

# Leer la imagen cifrada y descifrarla utilizando AES en modo OFB
imagen_cifrada = Image.open(ruta_imagen_cifrada)
imagen_cifrada_bytes = imagen_cifrada.tobytes()

cipher = AES.new(key, AES.MODE_OFB, iv)
imagen_descifrada_bytes = unpad(
    cipher.decrypt(imagen_cifrada_bytes), AES.block_size)

# Convertir la imagen descifrada de bytes a objeto Image
imagen_descifrada = Image.frombytes(
    "RGB", (ancho, alto), imagen_descifrada_bytes)

# Ruta donde se guardará la imagen descifrada
ruta_imagen_descifrada = "ruta/donde/se/guardara/la/imagen/descifrada.png"

# Guardar la imagen descifrada en el disco
imagen_descifrada.save(ruta_imagen_descifrada)
