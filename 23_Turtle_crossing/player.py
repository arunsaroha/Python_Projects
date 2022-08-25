from turtle import Turtle
# from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.refresh()
        self.setheading(90)

    def up(self):
        if self.ycor() != FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)