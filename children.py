
from account import Account
class childrenAccount(Account):
    def __init__(self):
        super().__init__()
        self.interest_rate = 0.007

    def deposit(self, amount):
        self.balance += self.balance + amount
        self.balance += self.balance * self.interest_rate
        print("Deposit successful. Your new balce is: ", self.balance)

    def withdraw(self):
        print("sorry, withdrawals are not allowed from this account. please contact your manager for more details")

account = childrenAccount()
account.deposit(30000)
account.withdraw()
