
fib = 0
fib_one = 1

fib_count = 0

while fib_count < 7:
    fib = fib + fib_one
    fib_one = fib + fib_one
    fib_count += 1

fib_str_even = str(fib)
fib_str_odd = str(fib_one)

fib_count_str_even = str(fib_count*2)
fib_count_str_odd = str(fib_count*2+1)

print ('The ' + fib_count_str_even + 'th number is ' + fib_str_even)
print ('The ' + fib_count_str_odd + 'th number is ' + fib_str_odd)
