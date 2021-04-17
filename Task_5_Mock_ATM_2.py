from datetime import datetime
import sys, random, string

allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']


def register():
    name = input('What is your name?: ')
    password = input('What password would you like to use?: ')
    allowedUsers.append(name)
    allowedPassword.append(password)
    number = []
    for x in range(10):
        number.append(random.choice(string.digits))
    acc_number = ''.join(number)
    print('Your account number is ',acc_number)
    return ATM()

def transactions(name, time, date):
    print('Welcome %s. You log in at %s on %s' %(name, time, date))
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4 Cancel Transaction')
                            

    selectOption = int(input('Please select an option: '))
    if selectOption == 1:
        withdraw()

    elif selectOption == 2:
        deposit()
                                
    elif selectOption == 3:
        complaint()

    elif selectOption == 4:
        sys.exit("Transaction Cancelled")

    else:
        print('Invalid Option selected, please try again!')
                                


def withdraw():
    amount = int(input('How much would you like to withdraw: '))
    print('Take your Cash', amount)
    return transactions
    
def deposit():
    amount = int(input('How much would you like to deposit?: '))
    print('You have successfully deposited %d' %amount)
    return transactions

def complaint():
    complaint = input('What issue will you like to report?: ')
    print('Thank you contacting us, It would be treated as soon as possible!')
    return transactions

def Login():
    name = input('What is your Username? \n')

    now = datetime.now()
    date = now.strftime('%B %d, %Y')
    time = now.strftime('%H:%M')

    
    if name in allowedUsers:
        password = input('Your password? \n')
        userId = allowedUsers.index(name)
        
        if password == allowedPassword[userId]:
            transactions(name, time, date)
            
        else:
            print('Password Incorrect, please try again')    

    else:
        print('User not found')

def ATM():
    print("Welcome, Enter\n1. To register\n2. To login")
    choice = int(input("Here: "))
    if choice == 1:
        register()
    elif choice == 2:
        Login()
    else:
        print('That isn\'t a valid Option. Try again!')
        ATM()

while True:
    ATM()


