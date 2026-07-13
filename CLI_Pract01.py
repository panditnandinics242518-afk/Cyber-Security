# Classical Cryptography (CLI)

def caesar(text, key, mode):
    result = ""
    if mode == "d":
        key = -key
    for ch in text:
        if ch.isalpha():
            shift = 65 if ch.isupper() else 97
            result += chr((ord(ch)-shift+key)%26+shift)
        else:
            result += ch
    return result

def playfair(text):
    text = text.upper().replace("J","I")
    if len(text)%2:
        text += "X"
    return " ".join(text[i:i+2] for i in range(0,len(text),2))

def columnar(text,key):
    while len(text)%key:
        text+="X"
    result=""
    for i in range(key):
        result+=text[i::key]
    return result

def double_columnar(text):
    return columnar(columnar(text,4),3)

while True:
    print("\n===== Classical Cryptography =====")
    print("1. Monoalphabetic Cipher")
    print("2. Playfair Cipher")
    print("3. Columnar Transposition")
    print("4. Double Columnar Transposition")
    print("5. Exit")

    ch=int(input("Enter Choice: "))

    if ch==1:
        txt=input("Enter Text: ")
        key=int(input("Enter Key: "))
        mode=input("Encrypt(e) / Decrypt(d): ")
        print("Result :",caesar(txt,key,mode))

    elif ch==2:
        txt=input("Enter Text: ")
        print("Playfair Pairs:",playfair(txt))

    elif ch==3:
        txt=input("Enter Text: ")
        key=int(input("Enter Columns: "))
        print("Encrypted :",columnar(txt,key))

    elif ch==4:
        txt=input("Enter Text: ")
        print("Encrypted :",double_columnar(txt))

    elif ch==5:
        break
