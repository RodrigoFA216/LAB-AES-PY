import sys
from Crypto.Cipher import AES
import numpy as np


"""
Funciones del cifrado AES
"""
# %% Función de cifrado AES-CTR
# key debe ser una llave de 16 bytes (128 bits)
# El texto plano deben ser bits en un array numpy (pt_array)
# Los bits cifrados resultantes se obtienen en un array con las mismas dimensiones que pt_array
# no_bits es el número de bits que componen pt_array


def AESctr_cipherT(key, pt_array, no_bits):
    # Array en texto plano
    M, N = pt_array.shape

    # Cifrado AES-CTR
    dnonce = b'\xb1O\x12WA0\xe8\xf4'

    pt_bits = "".join(pt_array.reshape(-1,).copy())
    pt_bytes = int(pt_bits, 2).to_bytes(
        int((M*N*no_bits)/8), byteorder=sys.byteorder)

    cipher = AES.new(key, AES.MODE_CTR, nonce=dnonce)
    ct_bytes = cipher.encrypt(pt_bytes)

    ct_bits = bin(int.from_bytes((ct_bytes), byteorder=sys.byteorder))[
        2:].zfill(M*N*no_bits)

    ctl = []

    for i in range(int(len(ct_bits)/no_bits)):
        ctl.append(ct_bits[i*no_bits: (i+1)*no_bits])

    ct_array = np.array(ctl).reshape(M, N)

    return ct_array


def AESctr_decipher(key, ctd_array, no_bits):
    # Array cifrado
    M, N = ctd_array.shape

    # Cifrado AES-CTR
    dnonce = b'\xb1O\x12WA0\xe8\xf4'

    ctd_bits = "".join(ctd_array.reshape(-1,).copy())
    ctd_bytes = int(ctd_bits, 2).to_bytes(
        int((M*N*no_bits)/8), byteorder=sys.byteorder)

    decipher = AES.new(key, AES.MODE_CTR, nonce=dnonce)
    ptd_bytes = decipher.decrypt(ctd_bytes)

    ptd_bits = bin(int.from_bytes((ptd_bytes), byteorder=sys.byteorder))[
        2:].zfill(M*N*no_bits)

    ptdl = []

    for i in range(int(len(ptd_bits)/no_bits)):
        ptdl.append(ptd_bits[i*no_bits: (i+1)*no_bits])

    ptd_array = np.array(ptdl).reshape(M, N)
    return ptd_array
