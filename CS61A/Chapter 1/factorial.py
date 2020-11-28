
def factorial(x):
# helps to get the factorial of a number
    final_factorial = 1
    increasing_number = 1
    number_counter = 1

    while number_counter <= x:
        final_factorial = final_factorial * increasing_number
        increasing_number = increasing_number + 1
        number_counter = number_counter + 1

    return final_factorial


result = factorial(3)

print(result)
