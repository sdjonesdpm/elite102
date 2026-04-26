import sqlite3


with sqlite3.connect('./bankdb') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts;")
    rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()