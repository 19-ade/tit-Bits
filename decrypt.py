from cryptography.fernet import Fernet

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())
def decrypt_caller(message,key) -> object:
    key=key
    f= Fernet(key)
    decrypted_message=f.decrypt(message)
    return decrypted_message

if __name__ == "__main__":
    #print(decrypt_caller(b'gAAAAABf8v1AdliJ3Lh-0z96fzOslnlaGMngdwKEo4dAB8qa1acrLscmCFpGDCfNzlWhX0i0INJYU4JQzLSHQ4q12zcCmorGQA==' ,b'IwlOnh0Ih8XgVl01LZOF1DjTp3H45yV5EOaloCPA4q4=').decode())
    f=str(decrypt_message(b'gAAAAABf-qFBQ1HyixWPcYpqmm4zBx22CVl1GzAFRsTd1cSr96e37JyGIxRPKDwxP2Fei3CB7quWHNKmZ0ezvU6cEipuc58xtcfuA6rXn25qvDmrN7-FL5g='))
