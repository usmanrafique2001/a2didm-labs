import hashlib, json, secrets

def commit(value: bytes):
    salt = secrets.token_bytes(16)
    return hashlib.sha256(salt + value).hexdigest(), salt

def verify(c, value: bytes, salt: bytes):
    return hashlib.sha256(salt + value).hexdigest() == c

def h(block):
    return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

def valid(chain):
    prev = "0" * 64
    for b in chain:
        if b["prev"] != prev:
            return False
        prev = h(b)
    return True

# Owner trains privately and commits to each checkpoint
weights = [b"weights-epoch-1", b"weights-epoch-2", b"weights-epoch-3"]
salts = []
chain = []
prev = "0" * 64
for i, w in enumerate(weights):
    c, salt = commit(w)
    salts.append(salt)          # kept secret by the owner
    block = {"index": i, "commitment": c, "prev": prev}
    chain.append(block)
    prev = h(block)

print("chain valid:", valid(chain))

# Later: owner proves what checkpoint 2 was
print("owner reveals epoch 2:", verify(chain[1]["commitment"], weights[1], salts[1]))

# A thief claims different weights were at checkpoint 2
print("thief claims other weights:", verify(chain[1]["commitment"], b"stolen-weights", salts[1]))

# The thief rewrites the commitment in block 1 to match their weights
fake_c, fake_salt = commit(b"stolen-weights")
chain[1]["commitment"] = fake_c
print("thief's fake commitment verifies:", verify(chain[1]["commitment"], b"stolen-weights", fake_salt))
print("chain valid after rewrite:", valid(chain))
