# crypto/diffie_hellman.py
import secrets

# Use a large prime number and generator (safe defaults)
PRIME = int(
    "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E08"
    "8A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD"
    "3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625"
    "E7EC6F44C42E9A63A36210000000000090563", 16
)
GENERATOR = 2


def generate_private_key():
    """Generate a private key (random number)"""
    return secrets.randbelow(PRIME - 2) + 2


def generate_public_key(private_key):
    """Calculate the public key"""
    return pow(GENERATOR, private_key, PRIME)


def generate_shared_secret(their_public_key, my_private_key):
    """Generate the shared secret key"""
    return pow(their_public_key, my_private_key, PRIME)
