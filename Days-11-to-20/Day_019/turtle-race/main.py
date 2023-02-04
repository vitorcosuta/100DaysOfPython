from turtle import Turtle, Screen
from tkinter import messagebox
import random


def is_valid_answer(input_str):
    for element in colors:
        if input_str == element:
            return True
    return False


screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
is_race_on = False

# Asking the user to make a bet
user_bet = screen.textinput(title='Make your bet: ', prompt='Which turtle will win the race? Enter a color.')

while not is_valid_answer(user_bet):
    user_bet = screen.textinput(title='Please inform a valid color: ', prompt='Which turtle will win the race? Enter a'
                                                                              ' color.')

for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    turtles.append(new_turtle)

x = -230
y = -130

for turtle in turtles:
    turtle.setposition(x, y)
    y += 50

if user_bet:
    is_race_on = True

winner_turtle = None

while is_race_on:

    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.position()[0] >= 230:
            winner_turtle = turtle
            is_race_on = False

# Calling tkinter to generate an alert box
if user_bet == winner_turtle.pencolor():
    messagebox.showinfo(title='RESULTS', message=f'The winner of the race was the {winner_turtle.pencolor()} turtle. '
                                                 f'Your bet was right!')
else:
    messagebox.showinfo(title='RESULTS', message=f'The winner of the race was the {winner_turtle.pencolor()} turtle. '
                                                 f'You lost the bet.')

screen.exitonclick()
