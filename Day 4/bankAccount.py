class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount
        print("Rs.",amount,"Deposited")

    def withdraw(self,amount):
        if(self.__balance>amount):
            self.__balance-=amount
            print("Rs.",amount,"Withdrawn")
        else:
            print("Insufficient balance")

    def get_balance(self):
        print("Balance : ",self.__balance)

acc=BankAccount()
acc.deposit(5000)
acc.withdraw(2000)
acc.get_balance()