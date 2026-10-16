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

def build(commitments):
    chain, prev = [], "0" * 64
    for i, c in enumerate(commitments):
        block = {"index": i, "commitment": c, "prev": prev}
        chain.append(block)
        prev = h(block)
    return chain

# Owner commits to three checkpoints
weights = [b"weights-epoch-1", b"weights-epoch-2", b"weights-epoch-3"]
pairs = [commit(w) for w in weights]
commitments = [c for c, s in pairs]
salts = [s for c, s in pairs]
public_chain = build(commitments)          # everyone holds a copy of this
published_tip = h(public_chain[-1])        # hash of the last block, widely known

# 1. Owner reveals epoch 3 with the right salt
print("1. right salt:", verify(commitments[2], weights[2], salts[2]))

# 2. Owner reveals epoch 3 but mixes up the salt (uses epoch 1's)
print("2. wrong salt:", verify(commitments[2], weights[2], salts[0]))

# 3. Thief swaps block 1 and rebuilds EVERY later link
commitments_thief = commitments.copy()
fake_c, fake_salt = commit(b"stolen-weights")
commitments_thief[1] = fake_c
thief_chain = build(commitments_thief)
print("3. thief's rebuilt chain valid:", valid(thief_chain))

# 4. Does the thief's last block match the hash everyone already knows?
print("4. thief matches published tip:", h(thief_chain[-1]) == published_tip)

# 5. Is the public copy still valid?
print("5. public chain valid:", valid(public_chain))
