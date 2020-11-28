def fib(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fib(n-1) + n
fib = fib(2)

print(fib)
