def turn_right():
    for n in range(3):
        turn_left()
        
def turn_around():
    turn_right()
    move()

def jump():
    turn_left()
    move()
    turn_around()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()


     