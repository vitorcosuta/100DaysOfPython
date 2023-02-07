import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forwards, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.advance_cars()

    for car in car_manager.cars:

        # Deleting the instance of each car that overpasses the screen and creating a new car instance
        if car.xcor() > 300:
            index = car_manager.cars.index(car)
            car_manager.delete_car_instance(index)
            car_manager.add_new_car()

        # Checking if the player crashed into a car
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.print_game_over()

    if player.reached_finish_line():
        car_manager.increase_speed()
        scoreboard.score_point()

screen.exitonclick()
