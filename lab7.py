import hashlib

def H(x: bytes) -> bytes:
    return hashlib.sha256(x).digest()

def build_levels(leaves):
    levels = [[H(l) for l in leaves]]
    while len(levels[-1]) > 1:
        level = levels[-1]
        levels.append([H(level[i] + level[i + 1]) for i in range(0, len(level), 2)])
    return levels

def prove(levels, index):
    path = []
    for level in levels[:-1]:
        sibling = index ^ 1                     # the neighbour in the pair
        side = "left" if sibling < index else "right"
        path.append((side, level[sibling]))
        index //= 2
    return path

def verify(root, leaf, path):
    h = H(leaf)
    for side, sibling in path:
        h = H(sibling + h) if side == "left" else H(h + sibling)
    return h == root

leaves = [b"ckpt1", b"ckpt2", b"ckpt3", b"ckpt4"]
levels = build_levels(leaves)
root = levels[-1][0]

path = prove(levels, 2)                         # prove ckpt3 is in the tree
print("1. ckpt3 proof verifies:", verify(root, b"ckpt3", path))
print("2. hashes in the proof:", len(path))
print("3. 'forged' with ckpt3's path:", verify(root, b"forged", path))
print("4. ckpt1 with ckpt3's path:", verify(root, b"ckpt1", path))

big = [f"ckpt{i}".encode() for i in range(1, 9)]  # 8 checkpoints
big_levels = build_levels(big)
print("5. hashes in the proof with 8 checkpoints:", len(prove(big_levels, 2)))
