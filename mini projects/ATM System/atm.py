class Atm:

    def __init__(self):
        self.balance=10000
        self.pin=1234

    def welcome(self):
        print("Welcome to the ATM")
        a=int(input("press 1 to enter card:\t"))
        if(a==1):
            usePin=int(input("enter pin:\t"))
            if(usePin==self.pin):
                f1.options()
            else:
                print("Pin is incorrect try again")
                f1.welcome()
        else:
            print("Please enter the card to continue")
            f1.welcome()
    def options(self):
        b=int(input("Press\n1) to check balance\n2) to withdraw\n3) to deposit\n4) to exit:\t"))
        if(b==1):
            f1.checkBalance()
        elif(b==2):
            f1.withdraw()
        elif(b==3):
            f1.deposit()
        else:
            f1.exit()
            
    def checkBalance(self):
        print("your balance is:\t",self.balance)
        ex=input("do you want to exit?\t")
        if(ex=="yes"):
            f1.exit()
        else:
            f1.options()

    def withdraw(self):
        wa=int(input("enter the amount to withdraw:\t"))
        if(wa>self.balance):
            print("insufficient balance")
        
        else:
            print("pls collect the ammount 0f",wa,"from the slot")
            self.balance=self.balance-wa
            wcb=input("do you wan to check balance:\t")
            if(wcb=="yes"):
                f1.checkBalance()
        ex=input("do you want to exit?\t")
        if(ex=="yes"):
            f1.exit()
        else:
            f1.options()

    def deposit(self):
        de=int(input("enter the amoubt you want to deposit:\t"))
        self.balance=self.balance+de
        print("your balance is:\t",self.balance)
        ex=input("do you want to exit?\t")
        if(ex=="yes"):
            f1.exit()
        else:
            f1.options()
        
    def exit(self):
        print("thanks visit again")
            
f1=Atm()
f1.welcome()