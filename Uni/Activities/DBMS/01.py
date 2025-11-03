# Build a Reusable SQLite Helper

import sqlite3

def connect_db(db_name = 'mydatabase.db'):
  """ Connect to SQLite database and return connection + cursor"""
  conn = sqlite3.connect(db_name)
  cursor = conn.cursor()
  return conn, cursor

def close_db(conn):
  """ Commit changes and close the connection """
  conn.commit()
  conn.close()
  
# Create a Table (with constraints)
def reset_table():
    conn, cursor = connect_db('test.db')
    cursor.execute("DROP TABLE IF EXISTS users;")
    close_db(conn)
    print("Table reset successfully")

def create_table():
  conn, cursor = connect_db('test.db')
  cursor.execute(
    ''' CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL
    );
''')
  close_db(conn)
  print("Table created successfully")
  
def insert_user(name, email):
  conn, cursor = connect_db('test.db')
  cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
  close_db(conn)
  print(f"Added user: {name}")
  
def get_all_users():
    conn, cursor = connect_db('test.db')
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    close_db(conn)
    return results

def get_user_by_id(user_id):
    conn, cursor = connect_db('test.db')
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    close_db(conn)
    return result

def update_user_email(user_id, new_email):
    conn, cursor = connect_db('test.db')
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    close_db(conn)
    print("Email updated successfully")

def delete_user(user_id):
    conn, cursor = connect_db('test.db')
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    close_db(conn)
    print("User deleted successfully")

if __name__ == "__main__":
    reset_table()
    create_table()
    insert_user("Marsella", "msy@test.com")
    insert_user("Tim", "tim@test.com")
    print(get_all_users())
    update_user_email(1, "marsella.new@test.com")
    print(get_user_by_id(1))
    delete_user(2)
    print(get_all_users())
