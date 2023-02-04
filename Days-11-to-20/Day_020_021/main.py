from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

# We must turn off the tracer and set it up to zero in 0 in order to remove
# animation delay
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.down, 'Down')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_body()


screen.exitonclick()
