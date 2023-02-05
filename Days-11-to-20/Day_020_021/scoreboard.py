from turtle import Turtle

STARTING_POSITION = (0, 260)
FONT_CONFIGURATION = ('Courier', 18, 'bold')
FONT_ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.speed(0)
        self.setposition(STARTING_POSITION)

        self.write(f'Score: {self.score}', move=False, align=FONT_ALIGNMENT, font=FONT_CONFIGURATION)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', move=False, align=FONT_ALIGNMENT, font=FONT_CONFIGURATION)

    def print_game_over(self):
        self.home()
        self.write(f'GAME OVER', move=False, align=FONT_ALIGNMENT, font=FONT_CONFIGURATION)
