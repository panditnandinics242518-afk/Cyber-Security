from tkinter import *

# ---------------- Functions ---------------- #

def caesar(text, key, mode):
    r = ""
    if mode == "Decrypt":
        key = -key

    for c in text:
        if c.isalpha():
            s = 65 if c.isupper() else 97
            r += chr((ord(c) - s + key) % 26 + s)
        else:
            r += c
    return r


def playfair(text):
    text = text.upper().replace("J", "I")
    if len(text) % 2:
        text += "X"
    return " ".join(text[i:i+2] for i in range(0, len(text), 2))


def columnar(text, key):
    while len(text) % key:
        text += "X"

    r = ""
    for i in range(key):
        r += text[i::key]
    return r


def double(text):
    return columnar(columnar(text, 4), 3)


def run():
    t = txt.get()
    k = key.get()

    try:
        if choice.get() == "Monoalphabetic":
            ans = caesar(t, int(k), mode.get())

        elif choice.get() == "Playfair":
            ans = playfair(t)

        elif choice.get() == "Columnar":
            ans = columnar(t, int(k))

        elif choice.get() == "Double Columnar":
            ans = double(t)

        output.config(text=ans)

    except:
        output.config(text="Invalid Key!")


# ---------------- GUI ---------------- #

root = Tk()
root.title("Classical Cryptography System")
root.geometry("650x500")
root.configure(bg="#EAF4FC")
root.resizable(False, False)

# Title
Label(
    root,
    text="CLASSICAL CRYPTOGRAPHY SYSTEM",
    font=("Helvetica", 18, "bold"),
    bg="#1565C0",
    fg="white",
    pady=12
).pack(fill=X)

# Main Frame
frame = Frame(root, bg="white", bd=2, relief=RIDGE)
frame.place(x=40, y=70, width=570, height=390)

# Technique
Label(
    frame,
    text="Select Technique",
    font=("Arial", 12, "bold"),
    bg="white"
).place(x=30, y=25)

choice = StringVar(value="Monoalphabetic")

OptionMenu(
    frame,
    choice,
    "Monoalphabetic",
    "Playfair",
    "Columnar",
    "Double Columnar"
).place(x=220, y=20, width=250)

# Text
Label(
    frame,
    text="Enter Message",
    font=("Arial", 12, "bold"),
    bg="white"
).place(x=30, y=80)

txt = Entry(frame, font=("Arial", 12), width=30)
txt.place(x=220, y=80)

# Key
Label(
    frame,
    text="Key",
    font=("Arial", 12, "bold"),
    bg="white"
).place(x=30, y=135)

key = Entry(frame, font=("Arial", 12), width=10)
key.insert(0, "3")
key.place(x=220, y=135)

# Mode
Label(
    frame,
    text="Mode",
    font=("Arial", 12, "bold"),
    bg="white"
).place(x=30, y=190)

mode = StringVar(value="Encrypt")

OptionMenu(
    frame,
    mode,
    "Encrypt",
    "Decrypt"
).place(x=220, y=185, width=150)

# Button
Button(
    frame,
    text="PROCESS",
    font=("Arial", 12, "bold"),
    bg="#1976D2",
    fg="white",
    activebackground="#0D47A1",
    activeforeground="white",
    command=run,
    cursor="hand2"
).place(x=210, y=245, width=160, height=40)

# Output Label
Label(
    frame,
    text="Result",
    font=("Arial", 12, "bold"),
    bg="white"
).place(x=30, y=315)

output = Label(
    frame,
    text="Output will appear here",
    font=("Arial", 12),
    bg="#F5F5F5",
    fg="#0D47A1",
    relief=SUNKEN,
    bd=2,
    wraplength=450,
    justify=LEFT,
    anchor="w",
    padx=10
)

output.place(x=30, y=345, width=500, height=35)

# Footer
Label(
    root,
    text="Python Cryptography Practical",
    font=("Arial", 10),
    bg="#EAF4FC",
    fg="gray"
).pack(side=BOTTOM, pady=5)

root.mainloop()
