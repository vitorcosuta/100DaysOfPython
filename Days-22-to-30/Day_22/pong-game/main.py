from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLES_POSITION = {'player1': (-350, 0), 'player2': (350, 0)}

screen = Screen()
screen.title('Pong Game')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

player1_paddle = Paddle(PADDLES_POSITION['player1'])
player2_paddle = Paddle(PADDLES_POSITION['player2'])
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player1_paddle.up, 'Up')
screen.onkeypress(player1_paddle.down, 'Down')
screen.onkeypress(player2_paddle.up, 'w')
screen.onkeypress(player2_paddle.down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with player 1 paddle
    if ball.distance(player1_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detecting collision with player 2 paddle
    if ball.distance(player2_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detecting if player 1 misses the ball
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.score_point(2)

    # Detecting if player 2 misses the ball
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.score_point(1)

screen.exitonclick()
