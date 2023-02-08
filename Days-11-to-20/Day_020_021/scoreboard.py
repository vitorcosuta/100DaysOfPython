from turtle import Turtle

STARTING_POSITION = (0, 260)
FONT_CONFIGURATION = ('Courier', 18, 'bold')
FONT_ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.setposition(STARTING_POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}  High Score:{self.high_score}', move=False, align=FONT_ALIGNMENT,
                   font=FONT_CONFIGURATION)

    def reset_scoreboard(self):

        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.setposition(STARTING_POSITION)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def print_game_over(self):
        self.home()
        self.write(f'GAME OVER', move=False, align=FONT_ALIGNMENT, font=FONT_CONFIGURATION)
        self.setposition((self.position()[0], self.position()[1] - 20))
        self.write(f'Press Enter to play again', move=False, align=FONT_ALIGNMENT, font=('Courier', 10, 'normal'))
