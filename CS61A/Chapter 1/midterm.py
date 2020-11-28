def same_digits(a,b):
    while a and b:
            if a%10 == b%10:
                end = a%10
                if end == (a%10)%10 or end:
                    a = a//10
                if end == (b%10)%10 or end:
                    b = b//10
            else:
                return False
    return True

print(same_digits(1,1))

def no_repeats(a):
    return search(lambda b: same_digits(b,a),1)

def search (f,x):
    while not f(x):
        x += 1
    return x

print(no_repeats(2222))
