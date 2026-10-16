import hashlib, secrets

def commit(value: bytes):
    salt = secrets.token_bytes(16)
    c = hashlib.sha256(salt + value).hexdigest()
    return c, salt

def verify(c, value: bytes, salt: bytes):
    return hashlib.sha256(salt + value).hexdigest() == c

c, salt = commit(b"weights-checkpoint-1")
print("commitment:", c)
print("honest reveal:", verify(c, b"weights-checkpoint-1", salt))
print("swapped value:", verify(c, b"weights-checkpoint-2", salt))
