
from account import Account



class bingham_savings_acc(Account):

    def __init__(self):
        super().__init__()
        self.interest_rate = 0.005
        

    def withdraw(self, amount):
        
        if amount > self.balance:
            print(h+' YOUR ACCOUNT BALANCE IS TOO LOW')

        
        elif amount <= 700000 :
             self.balance = self.balance - amount
             print('access granted for withdrawal')
             print(h+' your current balance is, '  + str(self.balance))
             

        else:
            print(h+' amount is beyond limits')
           

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.balance += self.balance*self.interest_rate
        print(h+' your current balance is, '  + str(self.balance))
        
print('ONLY INPUT NUMERIC VALUES FOR AMOUNT ')

h = input('Enter account user name: ')
k = bingham_savings_acc()
opt = input('IF YOU WANT TO DEPOSIT INPUT a lower case"d", AND IF YOU WANT TO WITHDRAW INPUT a lower case "w": ')

if opt == 'w': 
    try:
        amw = float(input('Enter desired  withdrawal amount: '))
        k.withdraw(amw)
    except:
        print(h +' AMOUNT MUST BE NUMERIC')
    
if opt == 'd':
    try:
        amd = float(input('Enter deposit amount: '))
        k.deposit(amd)
    except:
        print('AMOUNT MUST BE NUMERIC')
