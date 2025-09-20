from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(data):
    padding_len = 16 - len(data) % 16
    padding = bytes([padding_len] * padding_len)
    return data + padding

def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

def encrypt(plaintext, key_bytes):
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8')))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def decrypt(iv, ciphertext, key_bytes):
    iv_bytes = base64.b64decode(iv)
    ct_bytes = base64.b64decode(ciphertext)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    pt = unpad(cipher.decrypt(ct_bytes))
    return pt.decode('utf-8')
