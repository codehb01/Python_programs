# Program 21 : Design a working interface for the login and registration process with proper form validations and database connection using tkinter and SQLite

import tkinter as tk
from tkinter import messagebox
import bcrypt
import sqlite3

# Database setup
conn = sqlite3.connect("users.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	email TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL
)
""")
conn.commit()

# Password hashing functions
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode(), hashed_password)

# Register function
def register():
    username = user_name.get()
    email = email_id.get()
    password = pass_word.get()

    if not username or not email or not password:
        messagebox.showerror("Error", "All fields are compulsory")
        return

    if "@" not in email or "." not in email:
        messagebox.showerror("Error", "Enter a valid email")
        return

    if len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters")
        return

    try:
        hashed_pass = hash_password(password)
        cur.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                    (username, email, hashed_pass))
        conn.commit()
        messagebox.showinfo("Success", "Registration Successful! You can log in now")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username or Email already exists")

# Login function
def login():
    username = user_name.get()
    password = pass_word.get()

    if not username or not password:
        messagebox.showerror("Error", "All fields are required")
        return

    cur.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = cur.fetchone()

    if user and check_password(user[0], password):
        messagebox.showinfo("Success", "Login Successful! Welcome " + username)
    else:
        messagebox.showerror("Error", "Invalid Username or Password!")

# GUI Layout
root = tk.Tk()
root.title("Login Form")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Username:").pack(anchor="w", padx=10, pady=5)
user_name = tk.Entry(root)
user_name.pack(fill="x", padx=10)

tk.Label(root, text="Email:").pack(anchor="w", padx=10, pady=5)
email_id = tk.Entry(root)
email_id.pack(fill="x", padx=10)

tk.Label(root, text="Password:").pack(anchor="w", padx=10, pady=5)
pass_word = tk.Entry(root, show="*")
pass_word.pack(fill="x", padx=10)

tk.Button(root, text="Register", command=register).pack(pady=10)
tk.Button(root, text="Login", command=login).pack(pady=5)

root.mainloop()
