class BankAccount:
    bank_name = "Second Semi-National Bank"
    all_accounts = []
    # balance = 0
    # bank_balance = sum_balance

# @classmethod
# def populate_all_accounts(cls):


    @classmethod
    def display_all_account_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()

    def __init__(self, int_rate, balance=0, user_info='a person'): 
        self.int_rate = int_rate
        self.balance = balance
        self.info = user_info
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance > 0):
            self.balance -= amount
        else:
            print('Insufficient funds, fwend!')
        return self

    def display_account_info(self):
        print(f'You account balance is: {self.balance}')
        print(self.info)
        return self

    def yield_interest(self):
        self.int_rate = self.balance * 0.03
        if(self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()
    
    def makeDeposit(self, amount):
        self.account.balance += amount

# make withdrawal method
    def makeWithdrawal(self, amount):
        if amount <= self.account.balance:
            self.account.balance -= amount

# display user balance method
    def displayUserBalance(self):
        print(f'{self.name}, your remaining balance is ${self.account.balance}')

# transfer money method
    def transferMoney(self, otherUser, amount):
        self.account.balance -= amount
        otherUser.account.balance += amount