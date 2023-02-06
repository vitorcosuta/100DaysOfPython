from turtle import Turtle

ALIGNMENT = 'center'
FONT_CONFIGURATION = ('Courier', 80, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.update_score()

    def update_score(self):
        self.setposition(-100, 200)
        self.write(self.player1_score, font=FONT_CONFIGURATION, align=ALIGNMENT)
        self.setposition(100, 200)
        self.write(self.player2_score, font=FONT_CONFIGURATION, align=ALIGNMENT)

    def score_point(self, player_number):
        self.clear()
        if player_number == 1:
            self.player1_score += 1
        elif player_number == 2:
            self.player2_score += 1
        self.update_score()
