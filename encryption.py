from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
 
def encrypt_aes256(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv=get_random_bytes(16))
    ciphertext = cipher.encrypt(pad(plaintext.encode(), 16))
    return base64.b64encode(cipher.iv + ciphertext).decode()
 
def decrypt_aes256(key, ciphertext):
    ciphertext = base64.b64decode(ciphertext)
    iv, ciphertext = ciphertext[:16], ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), 16).decode()
    return plaintext
 
# Example usage:
secret_key = b'Autosap automation python team N'  # 32 bytes (256 bits)
message = "Welcome@1234"
 
encrypted_message = encrypt_aes256(secret_key, message)
decrypted_message = decrypt_aes256(secret_key, encrypted_message)
 
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")