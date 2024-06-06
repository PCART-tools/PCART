from sympy.crypto.crypto import rsa_public_key, rsa_private_key
from sympy import nextprime
p = nextprime(1000)
q = nextprime(1000 + p)
e = 65537
public_key = rsa_public_key(q, e, args=p)
