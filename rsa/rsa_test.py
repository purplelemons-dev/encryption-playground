
# NOTES:
# . p and q are primes
# . n = p * q
# . phi = (p-1) * (q-1)
# . e, the public exponent, is a number such that
#       1 < e < (p-1)*(q-1) and e is coprime to (p-1)*(q-1) and p*q
# . public key is
#      <message>^e (mod n)
# . d, the private exponent, is a number such that
#       d*e = 1 (mod (p-1)*(q-1))

from math import sqrt
import base64

def isPrime(i:int):
    if not i%2: return False, 2, i
    n=3
    while n<sqrt(i):
        if not i%n:
            return False, n, i
        n+=2
    return True, None, i
#
#def keygen(bits=2048,expo=65537)->tuple[int,int]:
#    ...

username = b'MR_H3ADSH0T#0001'
print(f"username: {username} / {sum(i for i in username)}")
a = base64.b64encode(username)

print(f"base64: {a} / {sum(i for i in a)}")
