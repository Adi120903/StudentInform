import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Create a table for student information
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

print("Database and students table created successfully!")

conn.commit()
conn.close()
