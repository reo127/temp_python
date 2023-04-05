"""
Feature added : 
1) encript password by sha512 using hashlib
"""
import tkinter as tk
import random
import hashlib



# Genarate Random password ---------------------------------------------->>
def generate_password():
    strength = password_strength.get()
    if strength == "strong":
        password = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+") for i in range(12))
    elif strength == "medium":
        password = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(8))
    else:
        password = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for i in range(6))

    # Hash password to SHA-512 ---------------------------------------------->>
    hash_password = hashlib.sha512(password.encode()).hexdigest()
    password_label.config(text=hash_password)


root = tk.Tk()
root.geometry("400x200")
root.title("Password Generator")

password_strength = tk.StringVar(value="strong")

strong_button = tk.Radiobutton(root, text="Strong", variable=password_strength, value="strong")
strong_button.pack()

medium_button = tk.Radiobutton(root, text="Medium", variable=password_strength, value="medium")
medium_button.pack()

weak_button = tk.Radiobutton(root, text="Weak", variable=password_strength, value="weak")
weak_button.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()



password_label = tk.Label(root)
password_label.pack()


root.mainloop()
