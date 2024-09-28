from bank import *
from account import *
from admin import *

bank = Bank("ABC Bank")
admin = Admin("admin", "1234")

def user_menu(account):
    while True:
        print(f"\nWelcome {account.name}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            amount = int(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '2':
            if bank.isBankrupt ==  True:
                print("Bankrup, You can not withdraw or transfer money")
            else:
                amount = int(input("Enter withdraw amount: "))
                account.withdraw(amount)
        elif choice == '3':
            print(account.check_balance())
        elif choice == '4':
            history = account.show_transaction_history()
            for record in history:
                print(record)
        elif choice == '5':
            amount = int(input("Enter loan amount: "))
            account.take_loan(amount, bank.loan_status)
        elif choice == '6':
            if bank.isBankrupt ==  True:
                print("Bankrup, You can not withdraw or transfer money")
            else:
                recipient_account_number = input("Enter recipient account number: ")
                recipient_account = bank.get_account_by_number(recipient_account_number)
                if recipient_account:
                    amount = int(input("Enter transfer amount: "))
                    account.transfer_money(recipient_account, amount)
                else:
                    print("Account does not exist.")
        elif choice == '7':
            print("Exiting......")
            break
        else:
            print("Invalid choice")

def login_user():
    identifier = input("Enter your account number(name+email, if name: aa, email: bb then account no: aabb): ")
    account = bank.get_account_by_number(identifier)
    if account:
        user_menu(account)
    else:
        print("Not found, You can try again or create an account")

def create_account():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    account_type = input("Enter account type (Savings/Current): ")

    bank.create_account(name, email, address, account_type)

def set_bankrupt():
    if bank.isBankrupt == True:
        bank.isBankrupt = False
        print("Status: Bank is Ok")
    else:
        bank.isBankrupt = True
        print("Status: Bankrupt")

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Show All Accounts")
        print("2. Delete Account")
        print("3. Show Total Bank Balance")
        print("4. Show Total Loan Amount")
        print("5. Turn Off Loan Feature")
        print("6. Turn On Loan Feature")
        print("7. Create account")
        print("8. Set bankrupt")
        print("9. Exit")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            bank.show_all_accounts()
        elif choice == '2':
            delAcc = input("Enter acoount no to delete: ")
            bank.delete_account(delAcc)
        elif choice == '3':
            total_balance = sum(account.balance for account in bank.accounts)
            print(f"Total balance: {total_balance}")
        elif choice == '4':
            bank.show_total_loan()
        elif choice == '5':
            bank.off_loan()
        elif choice == '6':
            bank.on_loan()
        elif choice == '7':
            create_account()
        elif choice == '8':
            set_bankrupt()
        elif choice == '9':
            print("Exiting......")
            break
        else:
            print("Invalid Ouput")


while True:
    print("\nWelcome to the Banking Management System")
    print("1. Login as User")
    print("2. Create New User Account")
    print("3. Admin Login")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")
    if choice == '1':
        login_user()
    elif choice == '2':
        create_account()
    elif choice == '3':
        id = input("Enter admin id: ")
        password = input("Enter password: ")
        
        if id == admin.id and password == admin.password:
            admin_menu()
        else:
            print("Invalid ID or Password")
    elif choice == '4':
        print("Exiting....")
        break
    else:
        print("Invalid input.")
