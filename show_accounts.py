import sqlite3

def show_accounts():
    print("\n ---- Current Accounts ----")
    try:
        with sqlite3.connect('bankdb') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM accounts;")
            rows = cursor.fetchall()
            if not rows:
                print("No account found.")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")

