# #1A
def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice: ")

message = input("Enter message: ")
shift = int(input("Enter shift key: "))

if choice == '1':
    print("Encrypted Message:", encrypt(message, shift))
elif choice == '2':
    print("Decrypted Message:", decrypt(message, shift))
else:
    print("Invalid Choice")


#1B
# def encrypt(text):
#     rail1 = ""
#     rail2 = ""

#     for i in range(len(text)):
#         if i % 2 == 0:
#             rail1 += text[i]
#         else:
#             rail2 += text[i]

#     return rail1 + rail2


# def decrypt(cipher):
#     mid = (len(cipher) + 1) // 2

#     rail1 = cipher[:mid]
#     rail2 = cipher[mid:]

#     result = ""
#     i = j = 0

#     for k in range(len(cipher)):
#         if k % 2 == 0:
#             result += rail1[i]
#             i += 1
#         else:
#             result += rail2[j]
#             j += 1

#     return result


# print("1. Encrypt")
# print("2. Decrypt")

# choice = input("Enter choice: ")

# text = input("Enter text: ")

# if choice == '1':
#     print("Encrypted:", encrypt(text))
# elif choice == '2':
#     print("Decrypted:", decrypt(text))
# else:
#     print("Invalid Choice")
