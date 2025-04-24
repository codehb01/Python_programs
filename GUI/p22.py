# Program 22: Perform CRUD database operations using a menu driven program (User Management - Add, Show, Delete, Update and Search).

import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to database
conn = sqlite3.connect('users_crud.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
''')
conn.commit()

# Functions
def add_user():
    name = name_var.get()
    email = email_var.get()
    if name == "" or email == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        messagebox.showinfo("Success", "User added successfully")
        clear_entries()

def show_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    output_text.delete("1.0", tk.END)
    for row in rows:
        output_text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}\n")

def search_user():
    id_val = id_var.get()
    if id_val == "":
        messagebox.showerror("Error", "Enter user ID to search")
    else:
        cursor.execute("SELECT * FROM users WHERE id=?", (id_val,))
        row = cursor.fetchone()
        output_text.delete("1.0", tk.END)
        if row:
            output_text.insert(tk.END, f"Found - ID: {row[0]}, Name: {row[1]}, Email: {row[2]}\n")
        else:
            output_text.insert(tk.END, "User not found\n")

def update_user():
    id_val = id_var.get()
    name = name_var.get()
    email = email_var.get()
    if id_val == "" or name == "" or email == "":
        messagebox.showerror("Error", "All fields are required for update")
    else:
        cursor.execute("UPDATE users SET name=?, email=? WHERE id=?", (name, email, id_val))
        conn.commit()
        messagebox.showinfo("Updated", "User record updated")
        clear_entries()

def delete_user():
    id_val = id_var.get()
    if id_val == "":
        messagebox.showerror("Error", "Enter user ID to delete")
    else:
        cursor.execute("DELETE FROM users WHERE id=?", (id_val,))
        conn.commit()
        messagebox.showinfo("Deleted", "User record deleted")
        clear_entries()

def clear_entries():
    id_var.set("")
    name_var.set("")
    email_var.set("")

# GUI Window
root = tk.Tk()
root.title("User Management System (CRUD)")
root.geometry("500x500")

id_var = tk.StringVar()
name_var = tk.StringVar()
email_var = tk.StringVar()

tk.Label(root, text="User ID").pack()
tk.Entry(root, textvariable=id_var).pack()
tk.Label(root, text="Name").pack()
tk.Entry(root, textvariable=name_var).pack()
tk.Label(root, text="Email").pack()
tk.Entry(root, textvariable=email_var).pack()

tk.Button(root, text="Add User", command=add_user).pack(pady=3)
tk.Button(root, text="Show All Users", command=show_users).pack(pady=3)
tk.Button(root, text="Search User", command=search_user).pack(pady=3)
tk.Button(root, text="Update User", command=update_user).pack(pady=3)
tk.Button(root, text="Delete User", command=delete_user).pack(pady=3)

output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=10)

root.mainloop()
