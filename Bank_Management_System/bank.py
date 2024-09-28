from account import *

class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.accounts = []
        self.total_balance = 0
        self.total_loan = 0
        self.loan_status = True
        self.isBankrupt = False

    def create_account(self,  name, email, address, account_type):
        newAccount = Account(name, email, address,account_type)
        self.accounts.append(newAccount)
        print(f"Account created successfully! Account Number: {newAccount.account_number}")


    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} deleted successfully.")
                return
        print("Account not found.")

    def show_all_accounts(self):
        if(self.accounts):
            for account in self.accounts:
                print(f"Account Number: {account.account_number}\tName: {account.name}\tBalance: {account.balance}")
        else:
            print("No account found")
    
    def show_total_loan(self):
        self.total_loan = sum(account.taken_loan for account in self.accounts)
        print(f"Total loan amount in the bank: {self.total_loan}")

    def off_loan(self):
        self.loan_status = False
        print("Loan feature turned off.")

    def on_loan(self):
        self.loan_status = True
        print("Loan feature turned on.")


    def get_account_by_number(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

