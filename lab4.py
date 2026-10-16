import hashlib

def H(x: bytes) -> bytes:
    return hashlib.sha256(x).digest()

def merkle_root(leaves):
    level = [H(l) for l in leaves]
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        level = [H(level[i] + level[i + 1]) for i in range(0, len(level), 2)]
    return level[0]

leaves = [b"ckpt1", b"ckpt2", b"ckpt3", b"ckpt4"]
root = merkle_root(leaves)
print("root:", root.hex())
leaves[2] = b"forged"
print("changed after one edit:", merkle_root(leaves) != root)
