from crypto.diffie_hellman import generate_private_key, generate_public_key, generate_shared_secret
from crypto.rsa_module import generate_keys, encrypt as rsa_encrypt, decrypt as rsa_decrypt, sign, verify
from crypto.aes_module import encrypt as aes_encrypt, decrypt as aes_decrypt
import hashlib

class SecureCommunicator:
    def __init__(self):
        # Generate RSA keys for this party
        self.private_key, self.public_key = generate_keys()
        # Generate DH private and public keys
        self.dh_private_key = generate_private_key()
        self.dh_public_key = generate_public_key(self.dh_private_key)
        self.shared_key = None

    def create_shared_key(self, other_party_dh_public_key):
        shared_secret = generate_shared_secret(other_party_dh_public_key, self.dh_private_key)
        # Hash the shared secret to produce a fixed-length (16 bytes) AES key
        key_bytes = hashlib.sha256(str(shared_secret).encode('utf-8')).digest()[:16] # AES-128
        self.shared_key = key_bytes  # Use bytes, not string

    def encrypt_message(self, plaintext):
        if not self.shared_key:
            raise ValueError("Shared key not established")
        iv, ciphertext = aes_encrypt(plaintext, self.shared_key)
        return iv, ciphertext

    def decrypt_message(self, iv, ciphertext):
        if not self.shared_key:
            raise ValueError("Shared key not established")
        return aes_decrypt(iv, ciphertext, self.shared_key)

    def sign_message(self, message):
        return sign(message, self.private_key)

    def verify_signature(self, message, signature, sender_public_key):
        return verify(message, signature, sender_public_key)
