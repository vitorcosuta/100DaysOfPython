import turtle
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()

        # Multiplies the base width and the base length which are both 20 pixels by 0.5, halving them.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('firebrick2')
        self.speed(0)

        self.refresh()

    def refresh(self):
        random_position = (random.randint(-280, 280), random.randint(-280, 280))
        self.setposition(random_position)
