def factorial(n):
    assert n >= 0, "Only positive numbers can run through this function"
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return factorial(n-1) * n

factorial = factorial(0)

print(factorial)
