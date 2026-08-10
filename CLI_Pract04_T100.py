import hashlib
import random
import math


# ---------- RSA KEY GENERATION ----------

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def generate_prime():
    while True:
        n = random.randint(100, 300)
        if is_prime(n):
            return n


def generate_keys():
    p = generate_prime()
    q = generate_prime()

    while p == q:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537

    # Find another e if necessary
    if math.gcd(e, phi) != 1:
        e = 3
        while math.gcd(e, phi) != 1:
            e += 2

    d = pow(e, -1, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


# ---------- HASH MESSAGE ----------

def hash_message(message):
    digest = hashlib.sha256(message.encode()).hexdigest()

    # Convert hexadecimal hash to integer
    return int(digest, 16)


# ---------- SIGN MESSAGE ----------

def sign_message(message, private_key):
    d, n = private_key

    hashed = hash_message(message)

    # RSA signature
    signature = pow(hashed, d, n)

    return signature


# ---------- VERIFY SIGNATURE ----------

def verify_signature(message, signature, public_key):
    e, n = public_key

    hashed = hash_message(message)

    # Recover hash from signature
    recovered_hash = pow(signature, e, n)

    # Since RSA modulus is small in this educational implementation,
    # compare modulo n.
    return recovered_hash == hashed % n


# ---------- MAIN PROGRAM ----------

print("=" * 50)
print("       RSA DIGITAL SIGNATURE - CLI")
print("=" * 50)

public_key, private_key = generate_keys()

print("\nPublic Key :", public_key)
print("Private Key:", private_key)

message = input("\nEnter message to sign: ")

signature = sign_message(message, private_key)

print("\nOriginal Message:")
print(message)

print("\nDigital Signature:")
print(signature)

# Verification
result = verify_signature(message, signature, public_key)

print("\nVerification Result:")

if result:
    print("VALID SIGNATURE")
    print("Message integrity and authenticity verified.")
else:
    print("INVALID SIGNATURE")


# Test modified message
modified_message = input(
    "\nEnter modified message to test integrity "
    "(press Enter to skip): "
)

if modified_message:
    result = verify_signature(
        modified_message,
        signature,
        public_key
    )

    print("\nModified Message Verification:")

    if result:
        print("VALID")
    else:
        print("INVALID")
        print("Message has been modified or signature is not authentic.")
