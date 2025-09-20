# crypto/rsa_module.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_keys(key_size=2048):
    key = RSA.generate(key_size)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt(message, pub_key_bytes):
    public_key = RSA.import_key(pub_key_bytes)
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode('utf-8'))
    return ciphertext

def decrypt(ciphertext, priv_key_bytes):
    private_key = RSA.import_key(priv_key_bytes)
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('utf-8')

def sign(message, priv_key_bytes):
    private_key = RSA.import_key(priv_key_bytes)
    h = SHA256.new(message.encode('utf-8'))
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

def verify(message, signature, pub_key_bytes):
    public_key = RSA.import_key(pub_key_bytes)
    h = SHA256.new(message.encode('utf-8'))
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False
