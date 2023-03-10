import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

# We must turn off the tracer and set it up to zero in 0 in order to remove
# animation delay
screen.tracer(0)


def restart_game():
    scoreboard.reset_scoreboard()
    snake.reset_body()


def unpause():
    global game_is_paused

    if game_is_paused:
        game_is_paused = False
        restart_game()


def pause():
    global game_is_paused
    game_is_paused = True


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(unpause, 'Return')

game_is_on = True
game_is_paused = False

while game_is_on:

    if not game_is_paused:
        screen.update()
        time.sleep(0.1)
        snake.move_body()

        # Detect collision with food
        if snake.head_segment.distance(food) < 15:
            scoreboard.increase_score()
            snake.extend_body()
            food.refresh()

        # Detect collision with wall
        if snake.head_segment.xcor() > 280 or snake.head_segment.xcor() < -280 \
                or snake.head_segment.ycor() > 300 or snake.head_segment.ycor() < -280:
            scoreboard.print_game_over()
            pause()

        # Detect collision with other segments
        for segment in snake.body_segments[1:]:
            if snake.head_segment.distance(segment) < 5:
                scoreboard.print_game_over()
                pause()
    else:
        screen.update()

screen.exitonclick()

