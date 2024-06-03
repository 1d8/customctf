from cryptography.fernet import Fernet
import base64

def decrypt_data(key, encrypted_data):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

if __name__ == "__main__":
    key = b'Insert decryption key here'
    encrypted_data = b'gAAAAABl8di2CXp8ioaPRqzXUTU5wkD6MsGaowCF0kZQ4_uXgJsuyrr66nrfrb2AQ3k3ReCH_XS6dLrzwMOVo6K07W8GyWQtr5jLahmTrR8_szQIscwCvv0='
    decrypted_data = decrypt_data(key, encrypted_data)
    print("Decrypted data:", decrypted_data)
