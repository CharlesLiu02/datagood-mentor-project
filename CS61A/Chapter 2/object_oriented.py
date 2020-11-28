class Account:
    interest = .01
    def __init__(self,account_holder):
        self.balance = 0
        self.holder = account_holder
        self.counter = 0
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        assert self.balance >= amount, "Insufficient Funds"
        self.balance = self.balance - amount
        return self.balance

class SavingsAccount(Account):
    """An account with a higher interest rate but a limited number of withdrawls, but there is a maximum number of times you can be charged this ammount"""
    ### Basically my BofA account in real life
    interest = 0.05 ### This isn't my interest rate F

    def withdraw(self, amount):
            return Account.withdraw(self, amount + self.withdraw_charge)
    def withdraw(self, amount):
        if self.counter >= 6 and self.counter < 12:
            self.counter +=1
            return Account.withdraw(self, amount + 10)
        else:
            self.counter +=1
            return Account.withdraw(self, amount)
    def deposit(self, amount):
        return Account.deposit(self,amount)


stephen_account = Account("Stephen")
yang_account = Account("Yang")
stephen_yang_account = SavingsAccount("Stephen")
stephen_account.deposit(100)
stephen_yang_account.deposit(100)

stephen_yang_account.withdraw(10)
stephen_yang_account.withdraw(10)
stephen_yang_account.withdraw(10)
stephen_yang_account.withdraw(10)
stephen_yang_account.withdraw(10)
stephen_yang_account.withdraw(10)
print(stephen_yang_account.withdraw(10))
print(stephen_yang_account.counter)
