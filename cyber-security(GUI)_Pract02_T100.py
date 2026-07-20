#GUI METHOD
from tkinter import *
from tkinter import messagebox

# ---------------------- FUNCTIONS ---------------------- #

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def encrypt():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        msg = int(entry_msg.get())

        if p <= 1 or q <= 1:
            messagebox.showerror("Error", "Enter valid prime numbers.")
            return

        n = p * q

        if msg >= n:
            messagebox.showerror("Error", "Message must be smaller than n.")
            return

        phi = (p - 1) * (q - 1)

        e = 2
        while e < phi:
            if gcd(e, phi) == 1:
                break
            e += 1

        d = mod_inverse(e, phi)

        cipher = pow(msg, e, n)

        lbl_public.config(text=f"({e}, {n})")
        lbl_private.config(text=f"({d}, {n})")
        lbl_cipher.config(text=str(cipher))

        btn_decrypt.config(command=lambda: decrypt(cipher, d, n))

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def decrypt(cipher, d, n):
    plain = pow(cipher, d, n)
    lbl_plain.config(text=str(plain))

def clear():
    entry_p.delete(0, END)
    entry_q.delete(0, END)
    entry_msg.delete(0, END)

    lbl_public.config(text="")
    lbl_private.config(text="")
    lbl_cipher.config(text="")
    lbl_plain.config(text="")

# ---------------------- WINDOW ---------------------- #

root = Tk()
root.title("RSA Encryption & Decryption")
root.geometry("900x650")
root.minsize(800, 600)      # Can maximize
root.configure(bg="#EAF4FC")

# ---------------------- MENU ---------------------- #

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Clear", command=clear)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# ---------------------- TITLE ---------------------- #

title = Label(
    root,
    text="RSA PUBLIC KEY ENCRYPTION & DECRYPTION",
    bg="#0D47A1",
    fg="white",
    font=("Arial", 22, "bold"),
    pady=15
)

title.pack(fill=X)

# ---------------------- MAIN FRAME ---------------------- #

main = Frame(root, bg="#EAF4FC")
main.pack(fill=BOTH, expand=True, padx=30, pady=30)

card = Frame(main, bg="white", bd=3, relief=RIDGE)
card.place(relx=0.5, rely=0.5, anchor="center")

# ---------------------- INPUTS ---------------------- #

Label(card, text="Prime Number (p)", bg="white",
      font=("Arial", 12, "bold")).grid(row=0, column=0, padx=20, pady=15, sticky="w")

entry_p = Entry(card, font=("Arial", 12), width=30)
entry_p.grid(row=0, column=1)

Label(card, text="Prime Number (q)", bg="white",
      font=("Arial", 12, "bold")).grid(row=1, column=0, padx=20, pady=15, sticky="w")

entry_q = Entry(card, font=("Arial", 12), width=30)
entry_q.grid(row=1, column=1)

Label(card, text="Message", bg="white",
      font=("Arial", 12, "bold")).grid(row=2, column=0, padx=20, pady=15, sticky="w")

entry_msg = Entry(card, font=("Arial", 12), width=30)
entry_msg.grid(row=2, column=1)

# ---------------------- BUTTONS ---------------------- #

btn_frame = Frame(card, bg="white")
btn_frame.grid(row=3, column=0, columnspan=2, pady=20)

Button(
    btn_frame,
    text="Encrypt",
    bg="#1976D2",
    fg="white",
    font=("Arial", 12, "bold"),
    width=12,
    command=encrypt
).grid(row=0, column=0, padx=10)

btn_decrypt = Button(
    btn_frame,
    text="Decrypt",
    bg="#2E7D32",
    fg="white",
    font=("Arial", 12, "bold"),
    width=12
)

btn_decrypt.grid(row=0, column=1, padx=10)

Button(
    btn_frame,
    text="Clear",
    bg="#F57C00",
    fg="white",
    font=("Arial", 12, "bold"),
    width=12,
    command=clear
).grid(row=0, column=2, padx=10)

# ---------------------- OUTPUT ---------------------- #

Label(card, text="Public Key", bg="white",
      fg="#1565C0", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=20)

lbl_public = Label(card, bg="white", font=("Arial", 12))
lbl_public.grid(row=4, column=1, sticky="w")

Label(card, text="Private Key", bg="white",
      fg="#1565C0", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=20)

lbl_private = Label(card, bg="white", font=("Arial", 12))
lbl_private.grid(row=5, column=1, sticky="w")

Label(card, text="Encrypted Message", bg="white",
      fg="#1565C0", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=20)

lbl_cipher = Label(card, bg="white", font=("Arial", 12))
lbl_cipher.grid(row=6, column=1, sticky="w")

Label(card, text="Decrypted Message", bg="white",
      fg="#1565C0", font=("Arial", 12, "bold")).grid(row=7, column=0, sticky="w", padx=20)

lbl_plain = Label(card, bg="white", fg="red",
                  font=("Arial", 12, "bold"))

lbl_plain.grid(row=7, column=1, sticky="w")

# ---------------------- FOOTER ---------------------- #

footer = Label(
    root,
    text="Developed using Python Tkinter | RSA Cryptography Practical",
    bg="#0D47A1",
    fg="white",
    font=("Arial", 10)
)

footer.pack(fill=X, side=BOTTOM)

root.mainloop()
