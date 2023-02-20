import hashlib
import os
import base64

md5_string = hashlib.md5(b'bob').hexdigest()

md5_bin_string = bin(int(md5_string, 16))
print("{}\n{}".format(md5_bin_string[2:66], md5_bin_string[66:]))

print("\n")

sha256_string = hashlib.sha256(b'alice').hexdigest()

salt = base64.b64encode(os.urandom(16))
salt_string = salt.decode("utf-8")

sha256_bin_string = bin(int(sha256_string, 16))

print("{}\n{}".format(salt_string, sha256_string))
