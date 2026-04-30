import sqlite3
from contextlib import contextmanager

DB_NAME = 'bankdb'

# 1. Establish connection and cursor at the module level
# or inside a setup function.
#Ensure the reuse of connections and cursors across functions to avoid overhead and potential issues with multiple connections.
@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        yield conn, cursor
    finally:
        conn.commit()  # Ensure changes are saved
        conn.close()   # Always close the connection when done

def create_table():
    # """Ensures the table exists before you try to use it."""
    with get_connection() as (conn, cursor):
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                balance REAL NOT NULL
            )
    ''')

def create_account(name, initial_balance):
    # Using 'with' or explicit commits keeps data safe
    with get_connection() as (conn, cursor):
        cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, initial_balance))

def deposit(account_id, amount):
    #adress negative inputs 
    with get_connection() as (conn, cursor):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, account_id))
        

def withdraw(account_id, amount):
    # Improvement: Add a check here later to prevent negative balances!
    with get_connection() as (conn, cursor):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        # Check current balance first
        cursor.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,))
        result = cursor.fetchone()
        if result and result[0] >= amount:
            cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, account_id))
            return True
        else:
            return False

def check_balance(account_id):
    # Fixed: Added the comma (account_id,) to make it a proper tuple
    with get_connection() as (conn, cursor):
        cursor.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,))
        result = cursor.fetchone()
    return result[0] if result else None