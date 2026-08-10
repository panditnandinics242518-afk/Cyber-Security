# Diffie-Hellman Key Exchange - CLI

print("=" * 55)
print("        DIFFIE-HELLMAN KEY EXCHANGE - CLI")
print("=" * 55)

# Publicly known values

p = int(input("\nEnter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))

# Private keys

nandini_private = int(input("\nEnter Nandini's private key: "))
ram_private = int(input("Enter Ram's private key: "))

# Calculate public keys

N = pow(g, nandini_private, p)
R = pow(g, ram_private, p)

# Calculate shared secret keys

nandini_shared_key = pow(R, nandini_private, p)
ram_shared_key = pow(N, ram_private, p)

print("\n---------- KEY EXCHANGE ----------")

print("\nPublic values:")
print("Prime (p):", p)
print("Generator (g):", g)

print("\nNandini:")
print("Private Key:", nandini_private)
print("Public Key :", N)

print("\nRam:")
print("Private Key:", ram_private)
print("Public Key :", R)

print("\n---------- SHARED SECRET ----------")

print("Nandini's Shared Key:", nandini_shared_key)
print("Ram's Shared Key    :", ram_shared_key)

if nandini_shared_key == ram_shared_key:
    print("\n✓ KEY EXCHANGE SUCCESSFUL")
    print("Nandini and Ram have the same shared secret key.")
else:
    print("\n✗ KEY EXCHANGE FAILED")
