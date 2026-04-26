import sqlite3
import banking_app

#Construct Core functions - Create Account, Deposit, Withdraw, Check Balance
def create_account(name, initial_balance):
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, initial_balance))
    conn.commit()

def deposit(id, amount):
    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, id))
    conn.commit()

def withdraw(id, amount):
    cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, id))
    conn.commit()

def check_balance(id):
    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (id))
    balance = cursor.fetchone()
    return balance[0] if balance else None 