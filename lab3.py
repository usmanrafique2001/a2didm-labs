import hashlib, json

def h(block):
    return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

chain = []
prev = "0" * 64
for i, msg in enumerate(["commit ckpt 1", "commit ckpt 2", "commit ckpt 3"]):
    block = {"index": i, "data": msg, "prev": prev}
    chain.append(block)
    prev = h(block)

def valid(chain):
    prev = "0" * 64
    for b in chain:
        if b["prev"] != prev:
            return False
        prev = h(b)
    return True

print("intact chain valid:", valid(chain))
chain[1]["data"] = "forged ckpt 2"
print("after tampering block 1:", valid(chain))
