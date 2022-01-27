class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else: 
            print("insufficiant funds: Charging a $5 fee")
            self.balance -= (amount + 5)
        return self

    def display_account_info(self):
        print(f"Account Interest Rate: $ {self.int_rate}")
        print(f"Account Balance: $ {self.balance}")
        print("*******************************************")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print("no interest added")
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
        return cls

# Create 2 accounts.
checking = BankAccount(0.01)
savings =  BankAccount(0.02)

# To the first account, make 3 deposits and 1 withdrawal, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)
checking.deposit(100).deposit(200).deposit(300).withdraw(100).yield_interest()

# To the second account, make 2 deposits and 4 withdrawals, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)
savings.deposit(1000).deposit(900).withdraw(500).withdraw(400).withdraw(300).withdraw(200).yield_interest()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.print_all_accounts()
