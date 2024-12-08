import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3


# Function to add student to the database
def add_student():
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()
    email = entry_email.get()

    if not (name and age and grade and email):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)", (name, age, grade, email))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
        display_students()
        clear_entries()
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()


# Function to clear input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    entry_email.delete(0, tk.END)


# Function to display student records
def display_students():
    for row in tree.get_children():
        tree.delete(row)

    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()


# Main Window
root = tk.Tk()
root.title("Student Information Form")

# Labels and Entry Fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Grade:").grid(row=2, column=0, padx=10, pady=5)
entry_grade = tk.Entry(root)
entry_grade.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=3, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Student", command=add_student).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Clear", command=clear_entries).grid(row=4, column=1, pady=10)

# Display Area
columns = ("ID", "Name", "Age", "Grade", "Email")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Grade", text="Grade")
tree.heading("Email", text="Email")

tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Load existing records
display_students()

# Start the main loop
root.mainloop()
