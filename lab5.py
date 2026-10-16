import hashlib, secrets

p = 2**127 - 1
g = 3
q = p - 1

x = secrets.randbelow(q)    # the secret
y = pow(g, x, p)            # public value

def prove(x):
    r = secrets.randbelow(q)
    t = pow(g, r, p)
    c = int.from_bytes(hashlib.sha256(f"{g}{y}{t}".encode()).digest(), "big") % q
    s = (r + c * x) % q
    return t, s

def verify(t, s):
    c = int.from_bytes(hashlib.sha256(f"{g}{y}{t}".encode()).digest(), "big") % q
    return pow(g, s, p) == (t * pow(y, c, p)) % p

t, s = prove(x)
print("honest proof accepted:", verify(t, s))
fake_x = secrets.randbelow(q)
t2, s2 = prove(fake_x)
print("proof with wrong secret accepted:", verify(t2, s2))
print("response s equals the secret x:", s == x)
