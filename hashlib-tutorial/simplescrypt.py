import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

salt = os.urandom(16)

kdf = Scrypt(salt=salt, length=32,
             n=2**14, r=8, p=1,
             backend=default_backend())

key = kdf.derive(b"amazing password")

kdf = Scrypt(salt=salt, length=32,
             n=2**14, r=8, p=1,
             backend=default_backend())

kdf.verify(b"amazing password", key)
print("Success! (Exception if mismatch)")
