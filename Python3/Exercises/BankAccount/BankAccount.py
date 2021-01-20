class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
    
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
        
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

acct = BankAccount("Darcy")
acct.owner #Darcy
acct.balance #0.0
acct.deposit(10)  #10.0
acct.withdraw(3)  #7.0
acct.balance  #7.0