from operator import mul
def is_sorted(n):
    if n < 10:
        return True
    if n % 10 > ((n % 100) // 10):
        return False
    else:
        return is_sorted(n//10)

print(is_sorted(22222))







"""2. (Spring 2015 MT1 Q3C) Implement the combine function, which takes a non-
negative integer n, a two-argument function f, and a number result. It applies

f to the first digit of n and the result of combining the rest of the digits of n by re-
peatedly applying f (see the doctests). If n has no digits (because it is zero), combine

returns result."""
def combine(n, f, result):
    if n == 0:
        return result
    else:
        return combine(n // 10 , f , f(n % 10, result))
print(combine(32, mul, 2))


def mario_number(level):
    if level == 1 or level == 11:
        return 1
    elif level % 10 == 0:
        return 0
    else:
        return mario_number(level//100) + mario_number(level//10)

print(mario_number(1110101010111))
