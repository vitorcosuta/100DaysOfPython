from turtle import Turtle, Screen

t1 = Turtle()
t1.shape('arrow')
t1.color('black')


def move_backwards():
    t1.backward(10)


def move_forwards():
    t1.forward(10)


def turn_counter_clockwise():
    t1.left(10)


def turn_clockwise():
    t1.right(10)


my_screen = Screen()
my_screen.listen()

my_screen.onkeypress(move_forwards, 'w')
my_screen.onkeypress(move_backwards, 's')
my_screen.onkeypress(turn_clockwise, 'd')
my_screen.onkeypress(turn_counter_clockwise, 'a')
my_screen.onkey(my_screen.reset, 'c')

my_screen.exitonclick()
