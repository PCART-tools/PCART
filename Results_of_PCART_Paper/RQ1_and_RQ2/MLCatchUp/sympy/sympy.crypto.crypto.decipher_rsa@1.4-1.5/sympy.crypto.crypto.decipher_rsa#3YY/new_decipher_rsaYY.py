from sympy.crypto.crypto import encipher_rsa, rsa_public_key, decipher_rsa, rsa_private_key
from sympy import nextprime
p = nextprime(1000)
q = nextprime(1000 + p)
e = 65537
n = p * q
public_key = rsa_public_key(p, q, e)
private_key = rsa_private_key(p, q, e)
message = 12345
encrypted_message = encipher_rsa(message, key=public_key)
decrypted_message = decipher_rsa(i=encrypted_message, key=private_key, factors=None)
