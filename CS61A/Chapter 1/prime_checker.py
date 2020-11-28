def trace(fn):
        def wrapped(x):
            print('-> ', fn, '(', x, ')')
            return fn(x)
        return wrapped

@trace
def prime_checker(n):
    assert n > 2, "The smallest prime number is 2"
    number_counter = 1
    while n % (n - number_counter) != 0:
        number_counter = number_counter + 1
        if n == number_counter:
            return True
        if n - number_counter == 1:
            return True
        if n % (n - number_counter) == 0:
            return False
    return True
print(prime_checker(99996333))
