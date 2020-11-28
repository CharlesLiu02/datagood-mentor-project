def summation(x,term):
    total = 0
    k = 1
    while k <= x:
        total = total + term(k)
        k = k + 1
    return total

def factorial (x):
    # helps to get the factorial of a number
        final_factorial = 1
        increasing_number = 1

        while increasing_number <= x:
            final_factorial = final_factorial * increasing_number
            increasing_number = increasing_number + 1

        return final_factorial

def approximate_e(x):
    return 1.0/factorial(x)

approximate_e = summation(100,approximate_e)

print(approximate_e)
