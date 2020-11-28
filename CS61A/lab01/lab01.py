def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    falling = 1
    _ = n
    number_counter = 1
    while number_counter <= k:
        falling = falling * _
        _ -= 1
        number_counter += 1
    return falling



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1


    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    multi = 0
    remainder = 0

    while y > 0:
        if y % 10 == 0:
            y = y // 10
        if y:
            remainder = y % 10
            multi = multi + remainder
            y = y // 10
        if y < 10:
            return multi + y
    return

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    eight_counter = 0
    while n > 0:
        if n % 10 == 8:
            n = n // 10
            eight_counter += 1
        else:
            n = n // 10
    if eight_counter == 2:
        return True
    else:
        return False
