def square_root (a):
    x = 1
    while x * x != a:
        x = square_root_update(x,a)
    return x

def square_root_update(x,a):
    return (x + a/x)/2

square_root = square_root(100)

print (square_root)



def improve(update,close,guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approximation(x,y,tolerance = 1e-10):
    return abs(x-y) < tolerance

def square_root(a):
    def update(x):
        return square_root_update(x,a)
    def close(x):
        return approximation(x*x,a)
    return improve(update,close)

square_root = square_root(100)


print (float(square_root))


def cube_root (a):
    x = 1
    while  x * x * x != a:
        x = cube_root_update(x,a)
    return x

def cube_root_update(x,a):
    return ((2 * x + a/(pow(x,2)))/3)

cube_root = cube_root (1000)

print (cube_root)
