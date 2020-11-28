
def identity(k):
    return k

def cubes(k):
    return pow (k,3)

def summation(x, term):
    assert x > 0, "number has to be positive"
    starting_number = 0
    number_counter = 1
    while number_counter <= x:
        starting_number = starting_number + term(number_counter)
        number_counter = number_counter + 1
    return starting_number

summation = summation(3,cubes)

print (summation)

"""
def sum_cubes(x):
    assert x > 0, "number has to be positive"
    starting_number = 0
    adding_number = 1
    number_counter = 0
    while number_counter < x:
        starting_number = pow(starting_number,3) + pow(adding_number,3)
        adding_number = adding_number + 1
        number_counter = number_counter + 1
    return starting_number
sum_cubes = sum_cubes(2)
print(sum_cubes)

def sum_naturals(x):
    assert x > 0, "number has to be positive"
    starting_number = 0
    adding_number = 1
    number_counter = 0
    while number_counter < x:
        starting_number = starting_number + adding_number
        adding_number = adding_number + 1
        number_counter = number_counter + 1
    return starting_number

sum_naturals = sum_naturals(10)

print(sum_naturals)
"""
