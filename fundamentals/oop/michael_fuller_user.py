
# create user class, including __init__() and make deposit method
class User:
    def __init__(self, name) -> None:
        self.name = name
        self.accountBalance = 0
    
    def makeDeposit(self, amount):
        self.accountBalance += amount

# make withdrawal method
    def makeWithdrawal(self, amount):
        if amount <= self.accountBalance:
            self.accountBalance -= amount

# display user balance method
    def displayUserBalance(self):
        print(f'{self.name}, your remaining balance is ${self.accountBalance}')

    def transferMoney(self, otherUser, amount):
        self.accountBalance -= amount
        otherUser.accountBalance += amount

# create 3 instances of User class
mike = User("Michael")
steve = User("Steven")
joe = User("Joseph")

# first user makes 3 deposits, and one withdrawal, display balance
mike.makeDeposit(100)
mike.makeDeposit(200)
mike.makeDeposit(200)
mike.makeWithdrawal(250)
mike.displayUserBalance()

# second user makes 2 deposits, 2 withdrawals, display balance
steve.makeDeposit(100)
steve.makeDeposit(300)
steve.makeWithdrawal(100)
steve.makeWithdrawal(50)
steve.displayUserBalance()

# third user makes 1 deposit, 3 withdrawals, display balance
joe.makeDeposit(200)
joe.makeWithdrawal(50)
joe.makeWithdrawal(50)
joe.makeWithdrawal(100)
joe.displayUserBalance()

# transfer money from first to third, display both
mike.transferMoney(joe, 100)
mike.displayUserBalance()
joe.displayUserBalance()