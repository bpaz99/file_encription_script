# All this does is conver a damn string into a key
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def getKey(pswd):
    password = pswd.encode()
    salt = b'kJ\xb9\xb1\x9e\x861\x16p\xab\x0b/\xf7p\xe2\xf5'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=10000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return(key)