import turtle
from turtle import Screen, Turtle
import random

turtle.colormode(255)

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("LightPink2")
colors = ['IndianRed4', 'DeepSkyBlue', 'DeepPink', 'OliveDrab', 'thistle']
directions = [0, 90, 180, 270]


# Challenge 1: Draw a square
def draw_square():

    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)


# Challenge 2: Draw dashed lines
def draw_dashed_line(line_length):

    dash_length = line_length/10
    total_dashes = line_length // 10

    if line_length < 0:
        total_dashes = -line_length//10

    for i in range(total_dashes):
        if i % 2 == 0:
            my_turtle.down()
            my_turtle.forward(dash_length)
        else:
            my_turtle.up()
            my_turtle.forward(dash_length)


# Challenge 3: Draw any polygon
def draw_polygon(number_of_sides):

    angle = 360/number_of_sides

    for _ in range(number_of_sides):
        my_turtle.forward(100)
        my_turtle.left(angle)


# Challenge 4: Simulate a random walk with multiple random colors
def random_walk():

    my_turtle.pensize(10)
    my_turtle.speed(10)

    for _ in range(100):
        my_turtle.color(random_color())
        my_turtle.forward(30)
        my_turtle.setheading(random.choice(directions))


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_rgb = (red, green, blue)

    return random_rgb


# Challenge 5: Draw a spirograph
def draw_spirograph():

    my_turtle.pensize(3)
    my_turtle.speed(0)
    for _ in range(72):
        draw_circle()
        my_turtle.right(5)
        my_turtle.forward(2)


def draw_circle():
    my_turtle.color(random_color())
    my_turtle.circle(100)


draw_spirograph()
my_screen = Screen()
my_screen.exitonclick()
