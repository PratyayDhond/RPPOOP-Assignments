
import os
class Account:
    accountCount = 0
    savingsAccountCount = 0
    currentAccountCount = 0

    def __init__(self,userInfo):
        self.userName = userInfo['userName']
        self.type = userInfo['type']
        self.balance = userInfo['balance']
        self.accountNumber = '14'

        count = 0
        if self.type == 'savings':
            self.accountNumber += '1'
            Account.savingsAccountCount += 1
            count = Account.savingsAccountCount
        else:
            self.accountNumber += '2'
            Account.currentAccountCount += 1
            count = Account.currentAccountCount

        if count < 9:
            self.accountNumber += '00' + str(count)
        elif count < 99:
            self.accountNumber += '0' + str(count)
        else:
            self.accountNumber += str(count)

        Account.accountCount = Account.savingsAccountCount + Account.currentAccountCount

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print('You don\'t have enough balance')
            return 0
        else:
            self.balance = self.balance - amount
            return amount

    def deposit(self, amount):
        self.balance += amount

    def getName(self):
        return self.userName

    def getAccountNo(self):
        return self.accountNumber

    def getAccountType(self):
        return self.type

    def displayDetails(self):
        print('Name         : ' + self.getName())
        print('Account No.  : ' + self.getAccountNo())
        print('Account Type : ' + self.getAccountType())
        print('Balance      : ' + str(self.getBalance()))

# End of class code
def accountType():
    print('Choose your account type\n 1. Savings Account \n 2. Current Account\n : ',end='')
    typeChoice = int(input())
    if typeChoice == 1:
        return 'savings'
    elif typeChoice == 2:
        return 'current'
    else:
        print('Incorrect choice, enter one of the two values\n')
        return accountType()

def getAccount():
    accountNumber = str(input('Enter Your Account Number: '))
    for acc in accounts:
        if acc.getAccountNo() == accountNumber:
            return acc
    else:
        return -1

accounts = []
choice = 0
while True:
    os.system('clear')
    print(' Press 1 to create new Account \n Press 2 to view Account Balance \n Press 3 to Deposit to account \n Press 4 to Withdraw from account \n Press 5 to get account details \n Press 6 to delete Account \n Press 7 to Exit \n : ',end='')
    choice = int(input())

    if choice == 1:
        accountDetails = {
            'userName': str(input('Enter Your Name: ')),
            'type': accountType(),
            'balance': float(input('Enter Initial deposit amount : '))
        }
        if accountDetails['balance'] < 0:
            accountDetails['balance'] = 0

        newAccount = Account(accountDetails)
        accounts.append(newAccount)
        os.system('clear')
        print('New Account Created Successfully with id: ' + str(newAccount.getAccountNo()))
        newAccount.displayDetails()
    elif choice == 2:
        acc = getAccount()
        if acc == -1:
            print('Account does not exist')
        else:
            print('Balance = ' + str(acc.getBalance()))
    elif choice == 3:
        acc = getAccount()
        if acc == -1:
            print('Incorrect Account Number')
        else:
            amount = float(input('Enter Amount to deposit : '))
            if amount <= 0 :
                print('Invalid amount')
            else:
                acc.deposit(amount)
                print('Updated Balance : ' + str(acc.getBalance()))
    elif choice == 4:
        acc = getAccount()
        if acc == -1:
            print('Account does not exist')
        else:
            amount = float(input('Enter Amount to withdraw : '))
            if amount < 0:
                print('Invalid Amount')
            elif amount > acc.getBalance():
                print('You don\'t have sufficient balance')
            else:
                acc.withdraw(amount)
                print('Updated Balance : ' + str(acc.getBalance()))
    elif choice == 5:
        acc = getAccount()
        if acc == -1:
            print('Incorrect Account Number')
        else:
            acc.displayDetails()
    elif choice == 6:
        acc = getAccount()
        if acc == -1:
            print('Incorrect Account Number')
        else:
            if acc.getBalance() > 0:
                print('Your Account still has Rs. ' + str(acc.getBalance()) + ' left. It will be withdraw now.')
            accounts.remove(acc)
            print('Account Deleted Successfully')
    elif choice == 7:
        print('Have a great Day!!')
        break;
    else:
        print('Error in Input.')
    input('Press Enter to continue: ')

