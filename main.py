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
cursor.execute("SELECT * FROM accounts")
conn.commit()   # IMPORTANT: saves your changes!

# Query data
cursor.execute("SELECT * FROM accounts")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Always close when done
conn.close()

# Insert data - SHOW DATA
#cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("Alice", 1000.0))"""

def run_diagnostics():
   try:
        with sqlite3.connect('bankdb') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM accounts;")
            rows = cursor.fetchall()

            if not rows:
                print("No accounts found.")

            for row in rows: 
                print(row)

    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
