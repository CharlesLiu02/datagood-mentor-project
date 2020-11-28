def make_deposit(balence):
    assert balence > 0, "You must deposit a positive number of cash"
    def deposit(amount):
        nonlocal balence
        balence = balence + amount
        return balence
    return deposit

print(make_deposit(20)(20))
"""dep = make_deposit(20)
dep2 = make_deposit(20)
dep3 = dep2
print(dep(5))
print(dep2(5))
print(dep2(5))

"""

"""

def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
                return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

wd = make_withdraw(20)
print(wd(5))
"""
