import sqlite3

# Connect to a database file (creates it if it does not exist)
conn = sqlite3.connect('bankdb')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        balance REAL
    )
''')

# Insert data - SHOW DATA
#cursor.execute("SELECT * FROM accounts")
conn.commit()   # IMPORTANT: saves your changes!

# Query data
cursor.execute("SELECT * FROM accounts")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Always close when done
conn.close()