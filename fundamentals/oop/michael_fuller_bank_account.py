class BankAccount:
    bank_name = "Second Semi-National Bank"
    all_accounts = []
    balance = 0
    # bank_balance = sum_balance

# @classmethod
# def populate_all_accounts(cls):


# @classmethod
# def display_all_account_info(cls):
#     print(BankAccount)

    def __init__(self, int_rate, balance=0, user_info='a person'): 
        self.int_rate = int_rate
        self.balance = balance
        self.info = user_info

    # don't worry about user info here; we'll involve the User class soon
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f'You account balance is: {self.balance}')
        print(self.info)
        return self

    def yield_interest(self):
        self.int_rate = self.balance * 0.03
        if(self.balance > 0):
            self.balance += self.balance * 0.03
        return self

account1 = BankAccount('Account1')
account2 = BankAccount('Account2') 

account1.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
account2.deposit(300).deposit(100).withdraw(50).withdraw(100).withdraw(50).withdraw(75).yield_interest().display_account_info()