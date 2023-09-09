class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance
    
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    def interestAmount(self):
        return (self.balance * self.interestRate)
     
demo1 = SavingsAccount("Karunya", 7000, 5)
demo1.deposit(500)
balance = demo1.getBalance()
print(balance) 
demo1.withdrawal(500)
balance = demo1.getBalance()
print(balance)  
interest = demo1.interestAmount()
print(interest)  