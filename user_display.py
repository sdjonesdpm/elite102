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
            initial_balance = float(input("Enter initial balance: "))
            core_functions.create_account(name, initial_balance)
            print("Account created successfully!")
        elif choice == '2':
            id = int(input("Enter account ID: "))
            amount = float(input("Enter deposit amount: "))
            core_functions.deposit(id, amount)
            print("Deposit successful!")
                #make account info available after each transaction
            show_accounts.show_accounts()
        elif choice == '3':
            id = int(input("Enter account ID: "))
            amount = float(input("Enter withdrawal amount: "))
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
