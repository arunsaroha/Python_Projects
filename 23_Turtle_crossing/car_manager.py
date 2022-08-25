import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.add_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for c in self.cars:
            new_x = c.xcor() - self.car_speed
            new_y = c.ycor()
            c.goto(x=new_x, y=new_y)

    def add_car(self):
        new = Turtle(shape="square")
        new.penup()
        new.color(random.choice(COLORS))
        new.shapesize(stretch_wid=1, stretch_len=2)
        new.goto(x=320, y=random.randint(-250, 250))
        self.cars.append(new)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
