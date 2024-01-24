class Bank_Account:
    
    def __init__(self):
        self.balance=0
        self.pin=1234
    def deposit(self):
        a=int(input("Enter password : "))
        if a==self.pin:
            amount=float(input("Enter amount to be Deposited : "))
            self.balance += amount
            print("\n Amount Deposited:",amount)
            print("\n Net Available Balance=",self.balance)
        else:
            print("Incorrect Password")

        screen_0()
 
    def withdraw(self):
        a=int(input("Enter password : "))
        if a==self.pin:
            amount = float(input("Enter amount to be Withdrawn : "))
            if self.balance>=amount:
                self.balance-=amount
                print("\n You Withdrew:", amount)
                print("\n Net Available Balance=",self.balance)
            else:
                print("\n Insufficient balance  ")
                print("\n Net Available Balance=",self.balance)
        else:
            print("Incorrect Password")
        screen_0()
 
    def display(self):
        a=int(input("Enter password : "))
        if a==self.pin:
            print("\n Net Available Balance=",self.balance)
        else:
            print("Incorrect Password")
        screen_0()

    def change_pin(self):
        pin1=int(input("Enter the old pin : "))
        if pin1==self.pin:
            new_pin=int(input("Enter a new pin : "))
            self.pin=new_pin
            screen_0()
        else:
            print("Wrong Pin")
            print("Press 1 to go back to home screen")
            print("press 2 to try again")
            b=int(input("Enter you choice : "))
            if b==1:
                screen_0()
            if b==2:
                s.change_pin()
            
s = Bank_Account()
def mainscreen():
        x=int(input('Enter your choice : '))
        if x==1:
            s.deposit()
        if x==2:
            s.withdraw()
        if x==3:
            s.display()
        if x==4:
            s.change_pin()
        if x== 5:
            exit()
def screen_0():
        print('                                                                ADITYA BANK SYSTEM                                                                      \n\n')
        print('                                                                1.Deposit Money                                                                              ')
        print('                                                                2.Withdraw Money                                                                                 ')
        print('                                                                3.Display Balance                                                                                    ')
        print('                                                                4.Change Pin                                                                                    ')
        print('                                                                5.Exit                                                                                    ')
        mainscreen()
         
screen_0()