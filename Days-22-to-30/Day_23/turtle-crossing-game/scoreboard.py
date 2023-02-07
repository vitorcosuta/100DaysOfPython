from turtle import Turtle

FONT = ("Courier", 24, "normal")
STARTING_POSITION = (-280, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0

        self.update_score()

    def update_score(self):
        self.clear()
        self.setposition(STARTING_POSITION)
        self.write(f'Score: {self.score}', align='left', font=FONT)

    def score_point(self):
        self.score += 1
        self.update_score()

    def print_game_over(self):
        self.home()
        self.write(f'GAME OVER', align='center', font=FONT)
