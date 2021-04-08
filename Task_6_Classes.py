class Budget:
    
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment


#methods associated with the Budget class
#sector specifies which category they want to deposit/withdraw into and also the balance they want to check
#amount specifies the money to be added or withdrawn of transferred


    def deposit(self, sector, amount):
        if sector == 1:
            self.food = self.food + amount
            return('Your balance is now %d' %self.food)
        elif sector == 2:
            self.clothing = self.clothing + amount
            return ('Your balance is now %d' %self.clothing)
        elif sector == 3:
            self.entertainment = self.entertainment + amount
            return ('Your balance is now %d' %self.entertainment)
        else:
            return('This is not a valid section')

        
        

    def withdraw(self, sector, amount):
        if sector == 1:
            self.food = self.food - amount
            return('Your balance is now %d' %self.food)
        elif sector == 2:
            self.clothing = self.clothing - amount
            return ('Your balance is now %d' %self.clothing)
        elif sector == 3:
            self.entertainment = self.entertainment - amount
            return ('Your balance is now %d' %self.entertainment)
        else:
            return('This is not a valid section')

    def balance(self, sector):
        if sector == 1:
            return('Your balance is %d' %self.food)
        elif sector == 2:
            return ('Your balance is %d' %self.clothing)
        elif sector == 3:
            return ('Your balance is %d' %self.entertainment)
        else:
            return('This is not a valid section')

    def transfer(self, sender, reciever, amount): #strictly between categories
        if sender == 1:
            self.food = self.food - amount
            if reciever == 1:
                return('You can\'t recieve to the category you are sending from. Try Again!')
            elif reciever == 2:
                self.clothing = self.clothing + amount
                return ('Your balance for Food is %d and Clothing is %d' %(self.food, self.clothing))
            elif reciever == 3:
                self.entertainment = self.entertainment + amount
                return ('Your balance for Food is %d and Clothing is %d' %(self.food, self.entertainment))
            else:
                return('This is not a valid section')
            
        elif sender == 2:
            self.clothing = self.clothing - amount
            if reciever == 1:
                self.food = self.food + amount
                return('Your balance for Clothing is %d and Food is %d'%(self.clothing, self.food))
            elif reciever == 2:
                return ('You can\'t recieve to the category you are sending from. Try Again!' )
            elif reciever == 3:
                self.entertainment = self.entertainment + amount
                return ('Your balance for Clothing is %d and Entertainment is %d' %(self.clothing, self.entertainment))
            else:
                return('This is not a valid section')
            
        elif sender == 3:
            self.entertainment = self.entertainment - amount
            if reciever == 1:
                self.food = self.food + amount
                return('Your balance for Entertainment is %d and Food is %d'%(self.entertainment, self.food))
            elif reciever == 2:
                return ('Your balance for Entertainment is %d and Clothing is %d' %(self.entertainment, self.clothing))
            elif reciever == 3:
                return ('You can\'t recieve to the category you are sending from. Try Again!')
            else:
                return('This is not a valid section')
            

        else:
            return('This is not a valid section')
        


person1 = Budget(10000,50000,3000)

#money1 = person1.deposit(1,300)
money2 = person1.withdraw(2,5000)
money3 = person1.transfer(2,3, 5000)
money4 = person1.transfer(1, 3, 700)

print (money2, '\n', money3, '\n', money4)
