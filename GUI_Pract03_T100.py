import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
import hmac

# ------------------------- Functions -------------------------

def generate_mac():
    message = txt_message.get("1.0", tk.END).strip()
    key = txt_key.get().strip()

    if message == "" or key == "":
        messagebox.showerror("Error", "Please enter both Message and Secret Key.")
        return

    mac = hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    txt_mac.config(state="normal")
    txt_mac.delete(0, tk.END)
    txt_mac.insert(0, mac)
    txt_mac.config(state="readonly")

    status.config(
        text="✔ MAC Generated Successfully",
        foreground="green"
    )


def verify_mac():
    message = txt_message.get("1.0", tk.END).strip()
    key = txt_key.get().strip()
    received_mac = txt_verify.get().strip()

    if message == "" or key == "" or received_mac == "":
        messagebox.showerror("Error", "Please fill all required fields.")
        return

    computed = hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    if hmac.compare_digest(computed, received_mac):
        status.config(
            text="✔ Verification Successful (Message Authentic)",
            foreground="green"
        )
        messagebox.showinfo("Result", "MAC Verified Successfully!")
    else:
        status.config(
            text="✘ Verification Failed (Message Modified)",
            foreground="red"
        )
        messagebox.showerror("Result", "MAC Verification Failed!")


def copy_mac():
    mac = txt_mac.get()
    if mac != "":
        root.clipboard_clear()
        root.clipboard_append(mac)
        messagebox.showinfo("Copied", "MAC copied to clipboard.")


def clear_all():
    txt_message.delete("1.0", tk.END)
    txt_key.delete(0, tk.END)

    txt_mac.config(state="normal")
    txt_mac.delete(0, tk.END)
    txt_mac.config(state="readonly")

    txt_verify.delete(0, tk.END)

    status.config(
        text="Ready",
        foreground="blue"
    )


# ------------------------- Window -------------------------

root = tk.Tk()
root.title("Message Authentication Code (MAC) Generator & Verifier")
# Full Screen Window
root.state("zoomed")          # Window

root.configure(bg="#EEF2F7")
root.resizable(True, True)

style = ttk.Style()
style.theme_use("clam")

title = tk.Label(
    root,
    text="Message Authentication Code (MAC)",
    font=("Segoe UI", 20, "bold"),
    bg="#1E3A5F",
    fg="white",
    pady=12
)
title.pack(fill="x")

frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.pack(padx=20, pady=20, fill="both", expand=True)

# ------------------------- Message -------------------------

tk.Label(
    frame,
    text="Message",
    bg="white",
    font=("Segoe UI", 11, "bold")
).place(x=25, y=20)

txt_message = tk.Text(
    frame,
    width=72,
    height=6,
    font=("Consolas", 11)
)
txt_message.place(x=25, y=50)

# ------------------------- Secret Key -------------------------

tk.Label(
    frame,
    text="Secret Key",
    bg="white",
    font=("Segoe UI", 11, "bold")
).place(x=25, y=180)

txt_key = ttk.Entry(
    frame,
    width=60,
    font=("Segoe UI", 11)
)
txt_key.place(x=25, y=210)

# ------------------------- Generate -------------------------

ttk.Button(
    frame,
    text="Generate MAC",
    command=generate_mac
).place(x=25, y=255)

# ------------------------- Generated MAC -------------------------

tk.Label(
    frame,
    text="Generated MAC",
    bg="white",
    font=("Segoe UI", 11, "bold")
).place(x=25, y=310)

txt_mac = ttk.Entry(
    frame,
    width=72,
    font=("Consolas", 10),
    state="readonly"
)
txt_mac.place(x=25, y=340)

# ------------------------- Verify -------------------------

tk.Label(
    frame,
    text="Enter MAC for Verification",
    bg="white",
    font=("Segoe UI", 11, "bold")
).place(x=25, y=390)

txt_verify = ttk.Entry(
    frame,
    width=72,
    font=("Consolas", 10)
)
txt_verify.place(x=25, y=420)

# ------------------------- Buttons -------------------------

ttk.Button(
    frame,
    text="Verify MAC",
    command=verify_mac
).place(x=25, y=465)

ttk.Button(
    frame,
    text="Copy MAC",
    command=copy_mac
).place(x=155, y=465)

ttk.Button(
    frame,
    text="Clear",
    command=clear_all
).place(x=265, y=465)
def exit_fullscreen(event=None):
    root.state("normal")

# Press ESC to exit full screen
root.bind("<Escape>", exit_fullscreen)

# ------------------------- Status -------------------------

status = tk.Label(
    root,
    text="Ready",
    font=("Segoe UI", 11, "bold"),
    fg="blue",
    bg="#EEF2F7"
)
status.pack(pady=8)

root.mainloop()
