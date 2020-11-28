
def split(n):
    return n // 10 , n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        return sum_digits(n-1) + n


def luhn(n):
    if n < 10:
        return n
    else:
        all_but_last , last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last , last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn(all_but_last) + luhn_digit

print(luhn(32))
