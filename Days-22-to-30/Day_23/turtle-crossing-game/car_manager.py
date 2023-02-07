from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
MAX_Y = 200
MIN_Y = -200
MAX_X = 260
MIN_X = -260


class CarManager:

    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

        self.init_cars()

    def delete_car_instance(self, index):
        self.cars[index].hideturtle()
        del self.cars[index]

    def advance_cars(self):

        for car in self.cars:
            new_x = car.xcor() + self.car_speed
            car.setposition(new_x, car.ycor())

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    # In Python, method overloading is not done by declaring two functions with the same name but different parameters.
    # We can do this by setting up all parameters to None and control the functionalities with if statements.
    # Here, we're resorting to method overloading in order to not need to pass a position parameter in the main file.
    def add_new_car(self, position=None):
        new_car = Turtle()
        new_car.shape('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))

        if position is None:
            new_car.setposition(-320, random.randint(MIN_Y, MAX_Y))
        else:
            new_car.setposition(position)

        self.cars.append(new_car)

    def init_cars(self):

        for _ in range(18):
            xcor = random.randint(MIN_X, MAX_X)
            ycor = random.randint(MIN_Y, MAX_Y)
            position = (xcor, ycor)
            self.add_new_car(position)
