import sqlite3

# Connect to SQLite database (it will create a file 'users.db' if it doesn't exist)
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the users table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insert a new user
try:
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('testuser', 'password123'))
    conn.commit()
    print("User inserted successfully.")
except sqlite3.IntegrityError:
    print("Username already exists. Choose a different one.")

# Close the connection
conn.close()

