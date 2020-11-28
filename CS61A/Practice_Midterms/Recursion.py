def can_win(n):
    """Returns True if the current player is guaranteed a win
    starting from the given state. It is impossible to win a game
    from an invalid game state.

    >>> can_win (-1) # invalid game state
    False
    >>> can_win (3) # take all three !
    True
    >>> can_win (4)
    False
    """
    def opponent_turn(n):
        if n <= 3:
            return False
        return all([can_win(n-3), can_win(n-2), can_win(n-1)])
    if n <= 3:
        return True
    else:
        return any([opponent_turn(n-1), opponent_turn(n-2), opponent_turn(n-3)])

def can_win1(number):
    if number <= 0:
        return False
    action = 1
    while action <= 3:
        new_state = number - action
        if not can_win1 ( new_state ):
            return True
        action += 1
    return False

def tester(func1,func2):
    counter = 1
    while counter < 50:
        if func1(counter) != func2(counter):
            print(counter)
        counter +=1
    print('works!')

tester(can_win1,can_win)
