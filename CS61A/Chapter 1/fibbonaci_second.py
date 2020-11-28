

def fib(n):
# find the nth fibbonaci number
    fib_count = 0
    fib, fib_one = 0 , 1
    while(fib_count  < n):
        fib, fib_one = fib_one, fib + fib_one
        fib_count += 1
    return fib

result = fib(35)

print (result)
