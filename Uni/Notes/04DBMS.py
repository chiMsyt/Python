# Creating a User's Table
# Goal: Create a table to store user information

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create Table
cursor.execute(''' CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

cursor.execute("INSERT INTO users (name,email) VALUES ('Marsella', 'msy@test.com')")

conn.commit()
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close