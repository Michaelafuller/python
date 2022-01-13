
# create user class, including __init__() and make deposit method
class User:
    def __init__(self, name) -> None:
        self.name = name
        self.accountBalance = 0
    
    def makeDeposit(self, amount):
        self.accountBalance += amount
        return self

# make withdrawal method
    def makeWithdrawal(self, amount):
        if amount <= self.accountBalance:
            self.accountBalance -= amount
        return self

# display user balance method
    def displayUserBalance(self):
        print(f'{self.name}, your remaining balance is ${self.accountBalance}')
        return self

# transfer money method
    def transferMoney(self, otherUser, amount):
        self.accountBalance -= amount
        otherUser.accountBalance += amount
        return self

# create 3 instances of User class
mike = User("Michael")
steve = User("Steven")
joe = User("Joseph")

# first user makes 3 deposits, and one withdrawal, display balance
mike.makeDeposit(100).makeDeposit(200).makeDeposit(200).makeWithdrawal(250).displayUserBalance()

# second user makes 2 deposits, 2 withdrawals, display balance
steve.makeDeposit(100).makeDeposit(300).makeWithdrawal(100).makeWithdrawal(50).displayUserBalance()

# third user makes 1 deposit, 3 withdrawals, display balance
joe.makeDeposit(200).makeWithdrawal(50).makeWithdrawal(50).makeWithdrawal(100).displayUserBalance()

# transfer money from first to third, display both
mike.transferMoney(joe, 100).displayUserBalance()
joe.displayUserBalance()