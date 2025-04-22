# super()

class Account:
    def __init__(self, name, balance, amount):
        self.name = name
        self.balance = balance
        self.amount = amount
    def deposit(self):
        self.balance = self.balance + self.amount
        print(f"you deposited {self.amount} now you have {self.balance}")

    def withdraw(self):
        self.balance = self.balance - self.amount
        print(f"you withdrawed {self.amount} now you have {self.balance}")

class Savings(Account):
    def __init__(self, name, balance, amount, rate):
        super().__init__(name, balance, amount)
        self.rate = rate
    def interest_rate(self):
        print(f"this is the interest rate {self.rate}")
    def add_interest(self):
        self.rate = self.balance + self.rate
        print(f"this is your balance {self.balance} and this is the interest rate added to your balance {self.rate}")

class Checking(Account):
    def __init__(self, name, balance, amount, charge):
        super().__init__(name, balance, amount)
        self.charge = charge

    def charge_fee(self):
        self.balance = self.balance - self.charge
        print(f"this amount of money {self.charge} is substracted from your balance. your balance right now is {self.balance}")
acc = Account("sofia", 200000, 10)
savings = Savings("sofia", 200000, 10, 20)
checking = Checking("sofia", 200000, 10, 20)

acc.deposit()
acc.withdraw()

savings.interest_rate()
savings.add_interest()

checking.charge_fee()
#