#1A
# import tkinter as tk
# from tkinter import ttk, messagebox


# def caesar_encrypt(text, shift):
#     result = ""

#     for char in text:
#         if char.isalpha():
#             start = ord('A') if char.isupper() else ord('a')
#             result += chr((ord(char) - start + shift) % 26 + start)
#         else:
#             result += char

#     return result


# def caesar_decrypt(text, shift):
#     return caesar_encrypt(text, -shift)


# def encrypt():
#     try:
#         shift = int(key_entry.get())
#         message = text_entry.get()

#         if message == "":
#             messagebox.showwarning("Warning", "Please enter a message.")
#             return

#         result.set(caesar_encrypt(message, shift))

#     except:
#         messagebox.showerror("Error", "Shift key must be an integer.")


# def decrypt():
#     try:
#         shift = int(key_entry.get())
#         message = text_entry.get()

#         if message == "":
#             messagebox.showwarning("Warning", "Please enter a message.")
#             return

#         result.set(caesar_decrypt(message, shift))

#     except:
#         messagebox.showerror("Error", "Shift key must be an integer.")


# root = tk.Tk()
# root.title("Caesar Cipher Encryption System")
# root.geometry("550x350")
# root.resizable(False, False)

# title = tk.Label(
#     root,
#     text="Caesar Cipher (Substitution Technique)",
#     font=("Arial", 18, "bold"),
#     fg="navy"
# )
# title.pack(pady=15)

# frame = ttk.Frame(root, padding=20)
# frame.pack(fill="both", expand=True)

# ttk.Label(frame, text="Enter Message:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=8)

# text_entry = ttk.Entry(frame, width=45)
# text_entry.grid(row=0, column=1)

# ttk.Label(frame, text="Shift Key:", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=8)

# key_entry = ttk.Entry(frame, width=10)
# key_entry.grid(row=1, column=1, sticky="w")

# button_frame = ttk.Frame(frame)
# button_frame.grid(row=2, column=1, pady=20)

# ttk.Button(button_frame, text="Encrypt", command=encrypt).grid(row=0, column=0, padx=10)

# ttk.Button(button_frame, text="Decrypt", command=decrypt).grid(row=0, column=1, padx=10)

# ttk.Label(frame, text="Result:", font=("Arial", 11, "bold")).grid(row=3, column=0, sticky="nw")

# result = tk.StringVar()

# result_box = ttk.Entry(frame, textvariable=result, width=45, state="readonly")
# result_box.grid(row=3, column=1)

# root.mainloop()

#1B
import tkinter as tk
from tkinter import ttk, messagebox


def encrypt_rail():
    text = text_entry.get()

    if text == "":
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    rail1 = ""
    rail2 = ""

    for i in range(len(text)):
        if i % 2 == 0:
            rail1 += text[i]
        else:
            rail2 += text[i]

    result.set(rail1 + rail2)


def decrypt_rail():
    cipher = text_entry.get()

    if cipher == "":
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    mid = (len(cipher) + 1) // 2

    rail1 = cipher[:mid]
    rail2 = cipher[mid:]

    plain = ""
    i = j = 0

    for k in range(len(cipher)):
        if k % 2 == 0:
            plain += rail1[i]
            i += 1
        else:
            plain += rail2[j]
            j += 1

    result.set(plain)


root = tk.Tk()
root.title("Rail Fence Cipher Encryption System")
root.geometry("550x350")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Rail Fence Cipher (Transposition Technique)",
    font=("Arial", 18, "bold"),
    fg="darkgreen"
)
title.pack(pady=15)

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Enter Message:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=8)

text_entry = ttk.Entry(frame, width=45)
text_entry.grid(row=0, column=1)

button_frame = ttk.Frame(frame)
button_frame.grid(row=1, column=1, pady=20)

ttk.Button(button_frame, text="Encrypt", command=encrypt_rail).grid(row=0, column=0, padx=10)

ttk.Button(button_frame, text="Decrypt", command=decrypt_rail).grid(row=0, column=1, padx=10)

ttk.Label(frame, text="Result:", font=("Arial", 11, "bold")).grid(row=2, column=0, sticky="nw")

result = tk.StringVar()

result_box = ttk.Entry(frame, textvariable=result, width=45, state="readonly")
result_box.grid(row=2, column=1)

root.mainloop()