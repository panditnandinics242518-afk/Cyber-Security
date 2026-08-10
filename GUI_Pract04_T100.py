import tkinter as tk
from tkinter import messagebox
import hashlib
import random
import math


# ---------- RSA FUNCTIONS ----------

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

    if math.gcd(e, phi) != 1:
        e = 3

        while math.gcd(e, phi) != 1:
            e += 2

    d = pow(e, -1, phi)

    return (e, n), (d, n)


def hash_message(message):
    digest = hashlib.sha256(message.encode()).hexdigest()

    return int(digest, 16)


def sign_message(message, private_key):
    d, n = private_key

    hashed = hash_message(message)

    signature = pow(hashed, d, n)

    return signature


def verify_signature(message, signature, public_key):
    e, n = public_key

    hashed = hash_message(message)

    recovered_hash = pow(signature, e, n)

    return recovered_hash == hashed % n


# ---------- GUI FUNCTIONS ----------

public_key = None
private_key = None
signature = None


def generate_keys_gui():
    global public_key, private_key

    public_key, private_key = generate_keys()

    public_key_text.delete("1.0", tk.END)
    private_key_text.delete("1.0", tk.END)

    public_key_text.insert(
        tk.END,
        str(public_key)
    )

    private_key_text.insert(
        tk.END,
        str(private_key)
    )

    messagebox.showinfo(
        "Success",
        "RSA keys generated successfully!"
    )


def sign_gui():
    global signature

    if private_key is None:
        messagebox.showerror(
            "Error",
            "Generate RSA keys first!"
        )
        return

    message = message_entry.get("1.0", tk.END).strip()

    if not message:
        messagebox.showerror(
            "Error",
            "Enter a message first!"
        )
        return

    signature = sign_message(
        message,
        private_key
    )

    signature_text.delete("1.0", tk.END)

    signature_text.insert(
        tk.END,
        str(signature)
    )

    messagebox.showinfo(
        "Success",
        "Message digitally signed!"
    )


def verify_gui():
    if public_key is None:
        messagebox.showerror(
            "Error",
            "Generate RSA keys first!"
        )
        return

    if signature is None:
        messagebox.showerror(
            "Error",
            "Sign the message first!"
        )
        return

    message = message_entry.get("1.0", tk.END).strip()

    result = verify_signature(
        message,
        signature,
        public_key
    )

    if result:

        result_label.config(
            text="✓ VALID SIGNATURE\n"
                 "Integrity and authenticity verified."
        )

        messagebox.showinfo(
            "Verification",
            "VALID SIGNATURE\n\n"
            "The message has not been modified."
        )

    else:

        result_label.config(
            text="✗ INVALID SIGNATURE\n"
                 "Message integrity/authenticity failed."
        )

        messagebox.showerror(
            "Verification",
            "INVALID SIGNATURE\n\n"
            "The message may have been modified."
        )


def clear_gui():

    message_entry.delete(
        "1.0",
        tk.END
    )

    signature_text.delete(
        "1.0",
        tk.END
    )

    public_key_text.delete(
        "1.0",
        tk.END
    )

    private_key_text.delete(
        "1.0",
        tk.END
    )

    result_label.config(
        text=""
    )


# ---------- MAIN WINDOW ----------

root = tk.Tk()

root.title("RSA Digital Signature")
root.geometry("750x700")

title = tk.Label(
    root,
    text="RSA DIGITAL SIGNATURE",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)


# Message

tk.Label(
    root,
    text="Enter Message:",
    font=("Arial", 12, "bold")
).pack()

message_entry = tk.Text(
    root,
    height=5,
    width=80
)

message_entry.pack(
    pady=5
)


# Buttons

button_frame = tk.Frame(root)

button_frame.pack(
    pady=10
)

tk.Button(
    button_frame,
    text="Generate RSA Keys",
    command=generate_keys_gui,
    width=20
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Sign Message",
    command=sign_gui,
    width=20
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Verify Signature",
    command=verify_gui,
    width=20
).grid(row=0, column=2, padx=5)


# Public Key

tk.Label(
    root,
    text="Public Key (e, n):",
    font=("Arial", 11, "bold")
).pack()

public_key_text = tk.Text(
    root,
    height=2,
    width=80
)

public_key_text.pack(
    pady=5
)


# Private Key

tk.Label(
    root,
    text="Private Key (d, n):",
    font=("Arial", 11, "bold")
).pack()

private_key_text = tk.Text(
    root,
    height=2,
    width=80
)

private_key_text.pack(
    pady=5
)


# Signature

tk.Label(
    root,
    text="Digital Signature:",
    font=("Arial", 11, "bold")
).pack()

signature_text = tk.Text(
    root,
    height=3,
    width=80
)

signature_text.pack(
    pady=5
)


# Result

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)

result_label.pack(
    pady=15
)


# Clear Button

tk.Button(
    root,
    text="Clear",
    command=clear_gui,
    width=15
).pack()


root.mainloop()


