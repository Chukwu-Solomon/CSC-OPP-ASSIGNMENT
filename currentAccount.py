from account import Account

class CurrentAccount(Account):
    
    def __init__(self):
        super().__init__()


        
currentAccount = CurrentAccount()

opt = input('IF YOU WANT TO DEPOSIT INPUT a lower case"d", AND IF YOU WANT TO WITHDRAW INPUT a lower case "w": ')

if opt == 'w': 

        amw = float(input('Enter desired  withdrawal amount: '))
        currentAccount.withdraw(amw)
    
        print('AMOUNT MUST BE NUMERIC')
    
if opt == 'd':
    
        amd = float(input('Enter deposit amount: '))
           
    

        currentAccount.deposit(amd)
    
        