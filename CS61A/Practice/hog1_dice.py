import random
def dice():
    min = 1
    max = 6
    return(random.randint(min, max))




def roll_dice(num_rolls):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1


    number_counter = 0
    dice_tracker = 0
    while number_counter < num_rolls:
        if int(dice()) == 1:
            number_counter = num_rolls
            dice_tracker = 1
            return (dice_tracker)
        dice_tracker += int(dice())
        number_counter += 1
    return( dice_tracker)

print(roll_dice (3))
