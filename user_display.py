import sqlite3
import banking_app
import core_functions
import showAccounts


# Connect to a database file (creates it if it does not exist)
conn = sqlite3.connect('bankdb')
cursor = conn.cursor()

#Compose CLI Menu loop 
def main_menu():
    while True:
        print("\nWelcome to the Banking App!")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Please select an option: ")
        if choice == '1':
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))
            core_functions.create_account(name, initial_balance)
            print("Account created successfully!")
        elif choice == '2':
            id = int(input("Enter account ID: "))
            amount = float(input("Enter deposit amount: "))
            core_functions.deposit(id, amount)
            print("Deposit successful!")
        elif choice == '3':
            id = int(input("Enter account ID: "))
            amount = float(input("Enter withdrawal amount: "))
            core_functions.withdraw(id, amount)
            print("Withdrawal successful!")
            #make account info available after each transaction
            showAccounts.show_accounts()
        elif choice == '4':
            id = int(input("Enter account ID: "))
            balance = core_functions.check_balance(id)
            if balance is not None:
                print(f"Current balance: ${balance:.2f}")
                showAccounts.show_accounts()
            else:
                print("Account not found.")
        elif choice == '5':
            print("Thank you for using the Banking App. See you next time!")
            break
        else: 
            print("Invalid option. Please try again. ")
if __name__ == "__main__":
    main_menu()
# Always close when done
conn.close()    

