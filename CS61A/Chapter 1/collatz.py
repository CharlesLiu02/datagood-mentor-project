"""def split(n):
    return  n%10 , n//10

def even(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return odd(n-1)

def odd(n):
    return even(n-1)

def coll(n):
    last , all_but_last = split(n)
    if n == 1:
        return
    else:
        return coll_func(n)

def coll_func(n):
    last , all_but_last = split(n)
    if even(last):
        n = n // 2
        print(n)
        coll(n)
    else:
        n = 3*n + 1
        print(n)
        coll(n)

coll = coll(3)

coll
"""

def coll(n):
    while True:
        print(n)
        if n % 2 == 0:
            n = n // 2
        elif n == 1:
            return
        else:
            n = 3*n + 1


coll = coll(3)

coll
