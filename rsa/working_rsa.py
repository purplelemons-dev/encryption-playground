
from random import getrandbits as grb
from math import sqrt,ceil,log2
from base64 import b64encode, b64decode

def first_calc():
    return (65537, 3312467842, 2222020747)

def is_prime(num:int)->bool:
    if not num%2: return False
    for i in range(3,ceil(sqrt(num)),2):
        if not num%i: return False
    return True

# i stole inverse() from rsa module (pip install rsa)
def inverse(exponent:int, modulo:int) -> int:
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = exponent  # Remember original a/b to remove
    ob = modulo  # negative values from return results
    while modulo != 0:
        q = exponent // modulo
        (exponent, modulo) = (modulo, exponent % modulo)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo original b
    if ly < 0:
        ly += oa  # If neg wrap modulo original a
    
    divider = exponent
    inv = lx
    if divider != 1:
        raise ValueError(f"{exponent} and {modulo} are not relative prime")
    return inv

def next_prime(base:int):
    base+=1 if not base%2 else 0
    while not is_prime(base):
        base+=2
    return base

def gen_prime(size=512):
    return next_prime(grb(size))

def rsa_keygen(size=1024,e=65537)->tuple[int,int,int]:
    """Returns `e`, `d`, `n`"""
    p,q=gen_prime(size//2),gen_prime(size//2)
    n=p*q
    tot=(p-1)*(q-1)
    #n=gen_prime(size//2)*gen_prime(size//2)
    ## d = e^-1(mod n)
    ## d*e = 1 (mod n)
    print(f"{p,q=}")
    print(f"{(e*n)%tot=}")
    d = inverse(e,tot)
    return e,d,n

def quick_pow_mod(base: int, exponent: int, modulus: int) -> int:
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def private_op(message:int, key:int, modulo:int)->int:
    return quick_pow_mod(message,key,modulo)

def public_op(message:int, key:int, modulo:int)->int:
    return quick_pow_mod(message,key,modulo)

if __name__=="__main__":
    e,d,n = (65537, 66998116182545, 93230066680511)

    message = 123456789
    print(f"{message=}")
    print(f"{e=}\n{d=}\n{n=}")
    print(f"{public_op(message,e,n)=}")
    print(f"{private_op(public_op(message,e,n),d,n)=}")

