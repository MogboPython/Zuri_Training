from datetime import datetime

name = input('What is your Username? \n')
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']
usersBalance = [30000, 40000, 50000]

now = datetime.now()
date = now.strftime('%B %d, %Y')
time = now.strftime('%H:%M')


if name in allowedUsers:
    password = input('Your password? \n')
    userId = allowedUsers.index(name)
    
    if password == allowedPassword[userId]:
        print('Welcome %s. You log in at %s on %s' %(name, time, date))
        
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        

        selectOption = int(input('Please select an option: '))
        if selectOption == 1:
            amount = int(input('How much would you like to withdraw: '))
            print('Take your Cash')

        elif selectOption == 2:
            amount2 = int(input('How much would you like to deposit?: '))
            usersPreviousBalance = usersBalance[userId]
            currentBalance =  usersPreviousBalance + amount2
            print('Your current Balance is %d' %currentBalance)
            
        elif selectOption == 3:
            complaint = input('What issue will you like to report?: ')
            print('Thank you contacting us!')
        else:
            print('Invalid Option selected, please try again!')
            

    else:
        print('Password Incorrect, please try again')

else:
    print('User not found')



