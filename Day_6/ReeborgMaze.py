def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() == False:
    if right_is_clear() == True:
        turn_right()
        move()
    elif right_is_clear() == False and front_is_clear() == True:
        move()
    else:
        turn_left()
