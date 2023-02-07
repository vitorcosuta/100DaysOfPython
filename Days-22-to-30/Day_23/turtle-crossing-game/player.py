from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def move_forwards(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.setposition(STARTING_POSITION)

    def reached_finish_line(self):

        if self.ycor() > 280:
            self.reset_position()
            return True
        return False
