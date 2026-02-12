import tkinter as tk
from tkinter import messagebox
import random, string
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Length must be a number!")
        return
    chars = ""
    if upper_var.get(): chars += string.ascii_uppercase
    if lower_var.get(): chars += string.ascii_lowercase
    if digits_var.get(): chars += string.digits
    if symbols_var.get(): chars += string.punctuation
    if not chars:
        messagebox.showerror("Error", "Select at least one type!")
        return
    password = "".join(random.choice(chars) for _ in range(length))
    password_output.config(state="normal")
    password_output.delete(0, tk.END)
    password_output.insert(0, password)
    password_output.config(state="readonly")
    check_strength(password, length)
def check_strength(password, length):
    strength = sum([
        length >= 8,
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password)
    ])
    if strength <= 2:
        strength_label.config(text="Weak ❌", fg="red")
    elif strength in [3,6]:
        strength_label.config(text="Medium ⚠️", fg="orange")
    else:
        strength_label.config(text="Strong ✅", fg="green")
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x380"); root.resizable(False, False)
tk.Label(root, text="🔐 Password Generator", font=("Arial",24,"bold")).pack(pady=10)
frame = tk.Frame(root); frame.pack(pady=10)
tk.Label(frame, text="Length:").grid(row=0, column=0, sticky="w")
length_entry = tk.Entry(frame, width=7); length_entry.insert(0,"18")
length_entry.grid(row=0, column=1)

upper_var, lower_var, digits_var, symbols_var = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()
tk.Checkbutton(frame, text="Include Uppercase", variable=upper_var, font=("Arial", 14)).grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame, text="Include Lowercase", variable=lower_var, font=("Arial", 14)).grid(row=2, column=0, sticky="w")
tk.Checkbutton(frame, text="Include Numbers", variable=digits_var, font=("Arial", 14)).grid(row=3, column=0, sticky="w")
tk.Checkbutton(frame, text="Include Symbols", variable=symbols_var, font=("Arial", 14)).grid(row=4, column=0, sticky="w")

tk.Button(root, text="Generate", command=generate_password, bg="#1500FF", fg="white").pack(pady=10)
password_output = tk.Entry(root, width=30, font=("Arial",16), justify="center", state="readonly"); password_output.pack(pady=5)
strength_label = tk.Label(root, text="", font=("Arial",16,"bold")); strength_label.pack(pady=10)
root.mainloop()
