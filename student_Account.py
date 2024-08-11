from account import Account

class StudentAccount(Account):
    def __init__(self):
        super().__init__()
        self.withdrawal_limit = 2000
        self.deposit_limit = 50000

    def deposit(self, amount):
        if amount > self.deposit_limit:
            return "Deposit limit exceeded. The maximum you can deposit at a time is {}.".format(self.deposit_limit)
        else:
            self.balance += amount
            return "Deposit successful. Your new balance is {}.".format(self.balance)

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            return "Withdrawal limit exceeded. The maximum you can withdraw at a time is {}.".format(self.withdrawal_limit)
        elif amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance = self.balance - amount
            return  "Withdrawal successful. Your new balance is {}.".format(self.balance)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Balance: {self.balance:.2f}"

account = StudentAccount()
account.deposit(50000)  
account.withdraw(200)
print(f"Current Balance: {account.get_balance():.2f}")
print(account)