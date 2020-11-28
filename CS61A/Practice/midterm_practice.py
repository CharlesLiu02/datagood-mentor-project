def q(n):
    def f(x, y, z):
        def g(i):
            if i == x:
                print ("Found")
            else:
                 print ("Not Found")
            return f(y,z,i)
        return g
    return f(None,None, n)

q(1)(1)(1)(1)



def get_k_run_starter(n, k):
###
#""">>> get_k_run_starter(123412341234, 1)
#1
#>>> get_k_run_starter(1234234534564567, 0)
#4
#>>> get_k_run_starter(1234234534564567, 1)
#3
#>>> get_k_run_starter(1234234534564567, 2)
#2
    i = 0
    final = None
    while k > i - 1:
        while n % 10 > (n // 10) % 10:
            n = n // 10
        final = n % 10
        i += 1
        n = n // 10

    return final
print(get_k_run_starter(1234234534564567, 1))

def div_by_primes_under(n):
    checker = lambda k: False
    i = 2
    while i <= n:
        if not checker(i):
            checker = (lambda f: lambda x: x % i or f(x)) (checker)
        i += 1
    return checker



def chain_function():
    def g(x, y):
        def h(n):
            if n == y + 1 or y == 0:
                return g(x,n)
            else:
                return print(n + 1, x + 1) or g(x + 1, n)
        return h
    return g(0,0)

print(chain_function()(3)(4)(4)(5))


def stacklist():

# get = stacklist()(3, stacklist()(2), stacklist()(2)) (1)
# get(1)
    g = lambda i: "Error: out of bounds!"
    def f(value, g=g, y=0 ): # y is editable
        f = g
        def g(i):
            if i == y: #editable line
                return value #editable line
            return f(i)  #editable line
        return g, y + 1 #editable line
    return f, g
