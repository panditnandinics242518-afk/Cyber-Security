import tkinter as tk
from tkinter import messagebox


# =========================================================
# DIFFIE-HELLMAN KEY EXCHANGE
# Nandini and Ram
# =========================================================


# ---------------------------------------------------------
# FUNCTION TO CHECK PRIME NUMBER
# ---------------------------------------------------------

def is_prime(n):

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:

        if n % i == 0:
            return False

        i += 2

    return True


# ---------------------------------------------------------
# FUNCTION TO CHECK PRIMITIVE ROOT / VALID GENERATOR
# ---------------------------------------------------------

def is_valid_generator(g, p):

    if g <= 1 or g >= p:
        return False

    # For this educational GUI, check that g produces
    # more than one distinct value modulo p.
    values = set()

    value = 1

    for _ in range(1, p):

        value = (value * g) % p
        values.add(value)

    return len(values) == p - 1


# ---------------------------------------------------------
# DIFFIE-HELLMAN CALCULATION
# ---------------------------------------------------------

def calculate_dh():

    try:

        # Get values from GUI
        p = int(p_entry.get())
        g = int(g_entry.get())

        nandini_private = int(
            nandini_private_entry.get()
        )

        ram_private = int(
            ram_private_entry.get()
        )

        # -------------------------------------------------
        # CHECK PRIME NUMBER
        # -------------------------------------------------

        if not is_prime(p):

            messagebox.showerror(
                "Invalid Prime Number",
                f"{p} is NOT a prime number.\n\n"
                "Please enter a prime number such as:\n"
                "23, 29, 31, 37, 41..."
            )

            p_entry.focus()

            return

        # -------------------------------------------------
        # CHECK GENERATOR
        # -------------------------------------------------

        if not is_valid_generator(g, p):

            messagebox.showerror(
                "Invalid Generator",
                f"{g} is not a valid primitive root "
                f"for p = {p}.\n\n"
                "For p = 23, try g = 5."
            )

            g_entry.focus()

            return

        # -------------------------------------------------
        # CHECK PRIVATE KEYS
        # -------------------------------------------------

        if nandini_private <= 0:

            messagebox.showerror(
                "Invalid Input",
                "Nandini's private key must be greater than 0."
            )

            return

        if ram_private <= 0:

            messagebox.showerror(
                "Invalid Input",
                "Ram's private key must be greater than 0."
            )

            return

        # -------------------------------------------------
        # CALCULATE PUBLIC KEYS
        # -------------------------------------------------

        nandini_public = pow(
            g,
            nandini_private,
            p
        )

        ram_public = pow(
            g,
            ram_private,
            p
        )

        # -------------------------------------------------
        # CALCULATE SHARED SECRET
        # -------------------------------------------------

        nandini_shared = pow(
            ram_public,
            nandini_private,
            p
        )

        ram_shared = pow(
            nandini_public,
            ram_private,
            p
        )

        # -------------------------------------------------
        # DISPLAY NANDINI'S PUBLIC KEY
        # -------------------------------------------------

        nandini_public_entry.delete(
            0,
            tk.END
        )

        nandini_public_entry.insert(
            0,
            str(nandini_public)
        )

        # -------------------------------------------------
        # DISPLAY NANDINI'S SHARED SECRET
        # -------------------------------------------------

        nandini_shared_entry.delete(
            0,
            tk.END
        )

        nandini_shared_entry.insert(
            0,
            str(nandini_shared)
        )

        # -------------------------------------------------
        # DISPLAY RAM'S PUBLIC KEY
        # -------------------------------------------------

        ram_public_entry.delete(
            0,
            tk.END
        )

        ram_public_entry.insert(
            0,
            str(ram_public)
        )

        # -------------------------------------------------
        # DISPLAY RAM'S SHARED SECRET
        # -------------------------------------------------

        ram_shared_entry.delete(
            0,
            tk.END
        )

        ram_shared_entry.insert(
            0,
            str(ram_shared)
        )

        # -------------------------------------------------
        # VERIFY SHARED SECRET
        # -------------------------------------------------

        if nandini_shared == ram_shared:

            result_label.config(
                text="✓ KEY EXCHANGE SUCCESSFUL",
                fg="#008000"
            )

            result_detail.config(
                text="Nandini and Ram have the same shared secret key.",
                fg="#008000"
            )

        else:

            result_label.config(
                text="✗ KEY EXCHANGE FAILED",
                fg="#cc0000"
            )

            result_detail.config(
                text="The shared secret keys do not match.",
                fg="#cc0000"
            )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter numbers only."
        )


# ---------------------------------------------------------
# CLEAR FUNCTION
# ---------------------------------------------------------

def clear_all():

    entries = [

        p_entry,
        g_entry,

        nandini_private_entry,
        nandini_public_entry,
        nandini_shared_entry,

        ram_private_entry,
        ram_public_entry,
        ram_shared_entry

    ]

    for entry in entries:

        entry.delete(
            0,
            tk.END
        )

    result_label.config(
        text=""
    )

    result_detail.config(
        text=""
    )


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title(
    "Diffie-Hellman Key Exchange - Nandini & Ram"
)

root.geometry(
    "720x760"
)

root.resizable(
    False,
    False
)

root.configure(
    bg="#f4f6f8"
)


# =========================================================
# TITLE
# =========================================================

title = tk.Label(
    root,
    text="DIFFIE-HELLMAN KEY EXCHANGE",
    font=("Arial", 22, "bold"),
    bg="#f4f6f8",
    fg="#1f3c88"
)

title.pack(
    pady=(20, 5)
)


subtitle = tk.Label(
    root,
    text="Secure Key Exchange between Nandini and Ram",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#555555"
)

subtitle.pack(
    pady=(0, 15)
)


# =========================================================
# PUBLIC VALUES
# =========================================================

public_frame = tk.LabelFrame(
    root,
    text="  PUBLIC VALUES  ",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#1f3c88",
    padx=20,
    pady=15
)

public_frame.pack(
    padx=30,
    pady=8,
    fill="x"
)


# Prime Number

tk.Label(
    public_frame,
    text="Prime Number (p):",
    font=("Arial", 11),
    bg="white"
).grid(
    row=0,
    column=0,
    sticky="w",
    pady=7
)

p_entry = tk.Entry(
    public_frame,
    width=35,
    font=("Arial", 11)
)

p_entry.grid(
    row=0,
    column=1,
    padx=20
)


# Generator

tk.Label(
    public_frame,
    text="Generator (g):",
    font=("Arial", 11),
    bg="white"
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=7
)

g_entry = tk.Entry(
    public_frame,
    width=35,
    font=("Arial", 11)
)

g_entry.grid(
    row=1,
    column=1,
    padx=20
)


# =========================================================
# NANDINI
# =========================================================

nandini_frame = tk.LabelFrame(
    root,
    text="  NANDINI  ",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#8e44ad",
    padx=20,
    pady=15
)

nandini_frame.pack(
    padx=30,
    pady=8,
    fill="x"
)


# Private Key

tk.Label(
    nandini_frame,
    text="Private Key:",
    font=("Arial", 11),
    bg="white"
).grid(
    row=0,
    column=0,
    sticky="w",
    pady=7
)

nandini_private_entry = tk.Entry(
    nandini_frame,
    width=35,
    font=("Arial", 11)
)

nandini_private_entry.grid(
    row=0,
    column=1,
    padx=20
)


# Public Key

tk.Label(
    nandini_frame,
    text="Public Key:",
    font=("Arial", 11),
    bg="white"
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=7
)

nandini_public_entry = tk.Entry(
    nandini_frame,
    width=35,
    font=("Arial", 11)
)

nandini_public_entry.grid(
    row=1,
    column=1,
    padx=20
)


# Shared Secret

tk.Label(
    nandini_frame,
    text="Shared Secret:",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(
    row=2,
    column=0,
    sticky="w",
    pady=7
)

nandini_shared_entry = tk.Entry(
    nandini_frame,
    width=35,
    font=("Arial", 11)
)

nandini_shared_entry.grid(
    row=2,
    column=1,
    padx=20
)


# =========================================================
# RAM
# =========================================================

ram_frame = tk.LabelFrame(
    root,
    text="  RAM  ",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#d35400",
    padx=20,
    pady=15
)

ram_frame.pack(
    padx=30,
    pady=8,
    fill="x"
)


# Private Key

tk.Label(
    ram_frame,
    text="Private Key:",
    font=("Arial", 11),
    bg="white"
).grid(
    row=0,
    column=0,
    sticky="w",
    pady=7
)

ram_private_entry = tk.Entry(
    ram_frame,
    width=35,
    font=("Arial", 11)
)

ram_private_entry.grid(
    row=0,
    column=1,
    padx=20
)


# Public Key

tk.Label(
    ram_frame,
    text="Public Key:",
    font=("Arial", 11),
    bg="white"
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=7
)

ram_public_entry = tk.Entry(
    ram_frame,
    width=35,
    font=("Arial", 11)
)

ram_public_entry.grid(
    row=1,
    column=1,
    padx=20
)


# Shared Secret

tk.Label(
    ram_frame,
    text="Shared Secret:",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(
    row=2,
    column=0,
    sticky="w",
    pady=7
)

ram_shared_entry = tk.Entry(
    ram_frame,
    width=35,
    font=("Arial", 11)
)

ram_shared_entry.grid(
    row=2,
    column=1,
    padx=20
)


# =========================================================
# BUTTONS
# =========================================================

button_frame = tk.Frame(
    root,
    bg="#f4f6f8"
)

button_frame.pack(
    pady=18
)


generate_button = tk.Button(
    button_frame,
    text="GENERATE SHARED KEY",
    command=calculate_dh,
    font=("Arial", 11, "bold"),
    bg="#1f3c88",
    fg="white",
    activebackground="#162d66",
    activeforeground="white",
    width=22,
    height=2,
    relief="flat",
    cursor="hand2"
)

generate_button.grid(
    row=0,
    column=0,
    padx=10
)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    command=clear_all,
    font=("Arial", 11, "bold"),
    bg="#555555",
    fg="white",
    activebackground="#333333",
    activeforeground="white",
    width=12,
    height=2,
    relief="flat",
    cursor="hand2"
)

clear_button.grid(
    row=0,
    column=1,
    padx=10
)


# =========================================================
# RESULT
# =========================================================

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 15, "bold"),
    bg="#f4f6f8"
)

result_label.pack(
    pady=(5, 2)
)


result_detail = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    bg="#f4f6f8"
)

result_detail.pack(
    pady=2
)


# =========================================================
# FOOTER
# =========================================================

footer = tk.Label(
    root,
    text="Diffie-Hellman Algorithm | Cryptography Practical",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="#777777"
)

footer.pack(
    side="bottom",
    pady=12
)


# =========================================================
# START PROGRAM
# =========================================================

root.mainloop()
