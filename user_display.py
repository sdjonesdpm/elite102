import core_functions
import show_accounts



#Compose CLI Menu loop 
def main_menu():
    #make sure table exists befor showing menu
    core_functions.create_table()

    while True:
        print("\nWelcome to the Banking App!")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Show Accounts")
        print("6. Exit")

        choice = input("Please select an option: ")
        if choice == '1':
            name = input("Enter account holder's name: ")
            if not name.strip():
                print("Name cannot be empty. Please try again.")
                continue
            elif len(name) > 100:
                print("Name is too long. Please enter a name with 100 characters or fewer.")
                continue
            #address number names
            elif any(char.isdigit() for char in name):
                print("Name cannot contain numbers. Please enter a valid name.")
                continue
            try:
                initial_balance = float(input("Enter initial balance: "))
                if initial_balance < 0:
                    print("Initial balance cannot be negative. Please enter a positive number.")
                    continue
            except ValueError:
                print("Invalid input for initial balance. Please enter a valid number.")
                continue
            core_functions.create_account(name, initial_balance)
            print("Account created successfully!")
             #make account info available after each transaction
            show_accounts.show_accounts()

        elif choice == '2':
            #address negative inputs and invalid account IDs
            try:
                id = int(input("Enter account ID: "))
                if id <= 0:
                    print("Invalid account ID. Please enter a positive integer.")
                    continue
                amount = float(input("Enter deposit amount: "))
                if amount < 0:
                    print("Invalid deposit amount. Please enter a positive number.")
                    continue
                core_functions.deposit(id, amount)
                print("Deposit successful!")
            except ValueError as e:
                print(f"Error: {e}")
                #make account info available after each transaction
            show_accounts.show_accounts()

        elif choice == '3':
            try:
                id = int(input("Enter account ID: "))
                if id <= 0:
                    print("Invalid account ID. Please enter a positive integer.")
                    continue
            except ValueError:
                print("Invalid account ID. Please enter a valid integer.")
                continue
            amount = float(input("Enter withdrawal amount: "))
            if amount < 0:
                print("Invalid withdrawal amount. Please enter a positive number.")
                continue
            success = core_functions.withdraw(id, amount)
            if success:
                print("Withdrawal successful!")
            else: 
                print("Insufficient funds or account not found.")
            #make account info available after each transaction
            show_accounts.show_accounts()

        elif choice == '4':
            id = int(input("Enter account ID: "))
            balance = core_functions.check_balance(id)
            if balance is not None:
                print(f"Current balance: ${balance:.2f}")
                show_accounts.show_accounts()
            else:
                print("Account not found.")

        elif choice == '5':
            show_accounts.show_accounts()

        elif choice == '6':
            print("Thank you for using the Banking App. See you next time!")
            break
        else: 
            print("Invalid option. Please try again. ")
if __name__ == "__main__":
    main_menu()
# get_connection() handles close and commit
