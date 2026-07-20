import math

# Function to find GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find Modular Inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# RSA Key Generation
p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

n = p * q
phi = (p - 1) * (q - 1)

# Choose e
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

# Calculate d
d = mod_inverse(e, phi)

print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Input message
message = int(input("\nEnter message (number less than n): "))

# Encryption
cipher = pow(message, e, n)
print("Encrypted Message:", cipher)

# Decryption
decrypted = pow(cipher, d, n)
print("Decrypted Message:", decrypted)



def prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

p = int(input("Enter p: "))
q = int(input("Enter q: "))

if prime(p) and prime(q):
    print("Both numbers are Prime")
else:
    print("Enter Prime Numbers Only")
