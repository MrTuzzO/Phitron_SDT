class Account:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address =  address
        self.account_type = account_type
        self.balance = 0
        self.account_number = name+email
        self.tnx_history =  []
        self.loan_count = 0
        self.taken_loan = 0

    def deposit(self, amount):
        self.balance += amount
        self.tnx_history.append(f"Deposit: {amount}\t Balance: {self.balance}")
        print(f"Deposit Sucessfull. Your Balance is : {self.balance}\n")

    def withdraw(self, amount):
        if(amount > self.balance):
            print("Withdrawal amount exceeded\n")
        else:
            self.balance-=amount
            self.tnx_history.append(f"Withdraw: {amount}\t Balance: {self.balance}")
            print(f"Withdraw Sucessfull. Your Balance is : {self.balance}\n")
    
    def check_balance(self):
        return f"Available balance: {self.balance}"
    
    def show_transaction_history(self):
        return self.tnx_history

    def take_loan(self, amount, loan_feature_enabled):
        if loan_feature_enabled:
            if(self.loan_count <2):
                self.balance += amount
                self.loan_count += 1
                self.taken_loan+=amount
                self.tnx_history.append(f"Took Loan: {amount}\t Balance: {self.balance}")
                print(f"You got loan: {amount} Your: Balance: {self.balance}")
            else:
                print("You have already taken the maximum number of loans allowed.")
        else:
            print("Loan feature is disabled.")

    def transfer_money(self, recipient_account,amount ):
        if(amount > self.balance):
            print("Insufficient balance for transfer.")
        elif recipient_account:
            self.balance -= amount
            recipient_account.balance += amount
            self.tnx_history.append(f"Transferred: {amount}\t Balance: {self.balance}")
            recipient_account.tnx_history.append(f"Received {amount}\tBalance: {recipient_account.balance}")
        else:
            print("Account does not exist.")



        

