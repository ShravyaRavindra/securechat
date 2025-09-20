from core.message_handler import SecureCommunicator

def test_secure_communication():
    # Create communicators for two parties
    alice = SecureCommunicator()
    bob = SecureCommunicator()

    # Exchange DH public keys and create shared AES keys
    alice.create_shared_key(bob.dh_public_key)
    bob.create_shared_key(alice.dh_public_key)

    # Verify shared keys are the same
    assert alice.shared_key == bob.shared_key, "Shared AES keys do not match!"

    # Message to send
    message = "Hello Bob! This is a confidential message from Alice."

    # Alice encrypts message using shared AES key
    iv, encrypted_msg = alice.encrypt_message(message)

    # Bob decrypts the message
    decrypted_msg = bob.decrypt_message(iv, encrypted_msg)

    print("Decrypted Message at Bob's end:", decrypted_msg)

    # Alice signs the message
    signature = alice.sign_message(message)

    # Bob verifies signature using Alice's public key
    is_valid_signature = bob.verify_signature(message, signature, alice.public_key)
    print("Signature Valid:", is_valid_signature)

    assert decrypted_msg == message, "Decrypted message mismatch!"
    assert is_valid_signature, "Signature verification failed!"

if __name__ == "__main__":
    test_secure_communication()
