from turtle import Turtle

MOVE_DISTANCE = 40


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed('fastest')
        self.setposition(position)

    def up(self):
        if self.ycor() < 210:
            new_y = self.ycor() + MOVE_DISTANCE
            self.setposition(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -210:
            new_y = self.ycor() - MOVE_DISTANCE
            self.setposition(self.xcor(), new_y)



