import turtle
import colorgram
import random
from turtle import Turtle, Screen

START_POSITION = (-350, -350)


def draw_spotted_art():

    # Configuring appearance
    my_turtle.width(5)
    my_turtle.shape('arrow')
    my_turtle.speed(0)
    my_turtle.up()
    my_turtle.hideturtle()

    # Setting up starting position
    x = START_POSITION[0]
    y = START_POSITION[1]
    my_turtle.setposition(x, y)

    for _ in range(14):
        for _ in range(14):
            draw_filled_circle()
            my_turtle.up()
            my_turtle.forward(50)
        y += 50
        my_turtle.up()
        my_turtle.setposition(x, y)


def draw_filled_circle():

    my_turtle.color(random.choice(color_palette))
    my_turtle.begin_fill()
    my_turtle.circle(20)
    my_turtle.end_fill()
    # We could also have use the dot() method:
    # my_turtle.dot(20, random.choice(color_palette))


turtle.colormode(255)

extracted_colors = colorgram.extract('hirst-art.jpg', 25)
color_palette = []
my_turtle = Turtle()

for color in extracted_colors:
    rgb = color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    final_color = (r, g, b)
    color_palette.append(final_color)

draw_spotted_art()
my_screen = Screen()
my_screen.exitonclick()
