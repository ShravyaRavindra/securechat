# main.py
from crypto.aes_module import encrypt, decrypt

def main():
    key = "thisisaverysecre"  # 16 chars = 128-bit key for AES
    plaintext = "Hello, this is a test message for AES encryption."

    print("Original text:", plaintext)

    iv, ciphertext = encrypt(plaintext, key)
    print("Encrypted text:", ciphertext)
    print("IV:", iv)

    decrypted_text = decrypt(iv, ciphertext, key)
    print("Decrypted text:", decrypted_text)

    assert decrypted_text == plaintext, "AES Decryption failed!"

if __name__ == "__main__":
    main()
# main.py (or test_rsa.py)
from crypto.rsa_module import generate_keys, encrypt, decrypt, sign, verify

def main():
    # Generate RSA keys
    priv_key, pub_key = generate_keys()
    print("Private Key:", priv_key.decode()[:50], "...")
    print("Public Key:", pub_key.decode()[:50], "...")

    message = "This is a secret message."
    print("Original Message:", message)

    # Encrypt message with public key
    encrypted = encrypt(message, pub_key)
    print("Encrypted Message:", encrypted)

    # Decrypt message with private key
    decrypted = decrypt(encrypted, priv_key)
    print("Decrypted Message:", decrypted)
    assert decrypted == message, "RSA decryption failed!"

    # Sign the message
    signature = sign(message, priv_key)
    print("Signature:", signature)

    # Verify the signature
    is_valid = verify(message, signature, pub_key)
    print("Signature Valid:", is_valid)
    assert is_valid, "Signature verification failed!"

if __name__ == "__main__":
    main()

from crypto.diffie_hellman import generate_private_key, generate_public_key, generate_shared_secret

def test_diffie_hellman():
    # Simulate two parties generating keys and shared secret
    private_a = generate_private_key()
    public_a = generate_public_key(private_a)

    private_b = generate_private_key()
    public_b = generate_public_key(private_b)

    secret_a = generate_shared_secret(public_b, private_a)
    secret_b = generate_shared_secret(public_a, private_b)

    print(f"Party A Private: {private_a}")
    print(f"Party A Public: {public_a}")
    print(f"Party B Private: {private_b}")
    print(f"Party B Public: {public_b}")
    print(f"Shared Secret A: {secret_a}")
    print(f"Shared Secret B: {secret_b}")
    assert secret_a == secret_b, "Shared secrets do not match!"

if __name__ == "__main__":
    test_diffie_hellman()
