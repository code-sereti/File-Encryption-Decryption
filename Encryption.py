from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(output_file, 'wb') as file:
        file.write(ciphertext)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        ciphertext = file.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    with open(output_file, 'wb') as file:
        file.write(plaintext)

def generate_key():
    return os.urandom(32)  # 256 bits key for AES-256

def main():
    input_file = "input.txt"
    encrypted_file = "encrypted.txt"
    decrypted_file = "decrypted.txt"

    key = generate_key()

    # Encrypt
    encrypt_file(input_file, encrypted_file, key)
    print(f"File '{input_file}' encrypted to '{encrypted_file}'")

    # Decrypt
    decrypt_file(encrypted_file, decrypted_file, key)
    print(f"File '{encrypted_file}' decrypted to '{decrypted_file}'")

if __name__ == "__main__":
    main()
