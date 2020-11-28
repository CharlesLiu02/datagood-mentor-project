def hailstone(n):
    if n == 1:
        return print(1) or 1
    elif n % 2 == 0:
        return print(n) or 1 + hailstone(n//2)
    else:
        return print(n) or 1 + hailstone(3 * n + 1)
a = hailstone(10)
print(a)

def make_func_repeater(f, x):
    def repeat(y):
        if x == 0:
            return y
        else:
            return make_func_repeater(f,x-1)(f(y))
    return repeat
incr_1 = make_func_repeater(lambda x: x + 1, 10)
print(incr_1(4)) #same as f(f(x)))
