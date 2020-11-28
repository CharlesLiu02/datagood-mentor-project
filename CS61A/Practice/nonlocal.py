def make_sassy_function(f, msg):
    """Returns a version of f that only works every other function
    call.

    >>> f = lambda x: x**2
    >>> sassy_f = make_sassy_function(f, 'Um, excuse me?')
    >>> sassy_f(4)
    16
    >>> sassy_f(5)
    'Um, excuse me?'
    >>> sassy_f(6)
    36
    >>> g = lambda x, y: x*y
    >>> sassy_g = make_sassy_function(g, "Ain't nobody got time for that!")
    >>> sassy_g(1, 2)
    2
    >>> sassy_g(5, 4)
"Ain't nobody got time for that!"
    """
    number_counter = 0
    def counter(x):
        nonlocal number_counter
        number_counter += 1
    if number_counter % 2:
        counter(1)
        return msg
    elif number_counter % 2 == True:
        counter(1)
        return f
    else:
        return f

f = lambda x: x**2
sassy_f = make_sassy_function(f, 'Um, excuse me?')
print(sassy_f(4))
print(sassy_f(4))
def snooze(e, f):
    if e and f():
        print(e)
    if e or f():
        print(f)
    if not e:
        print('naughty')
