import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# creating turtle
tom = Player()
# turtle forward/up movement
screen.listen()
screen.onkey(tom.up, "Up")

# creating cars
car = CarManager()

# creating scoreboard
score = Scoreboard()

count = 6
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()
    count += 1
    if count % 6 == 0:
        car.add_car()

    # detect turtle reaching end point
    if tom.ycor() >= 280:
        score.score_update()
        tom.refresh()
        car.level_up()

    # detect collision with car
    for i in car.cars:
        if i.distance(tom) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()