import random
from turtle import Turtle, Screen
race_on = False
screen = Screen()
screen.setup(width=800, height=600)
guess = screen.textinput(title="Make a guess", prompt="Which turtle will win the race? Enter a color. ")
colors = ["red", "orange", "blue", "green", "violet", "pink", "purple", "black", "yellow"]
y_positions = [-175, -125, -75, -25, 25, 75, 125, 175]
all_turtles = []

for t in range(0, 8):
    tim = Turtle(shape="turtle")
    tim.color(colors[t])
    tim.penup()
    tim.goto(x=-375, y=-y_positions[t])
    all_turtles.append(tim)

if guess:
    race_on = True

while race_on:

    for i in all_turtles:
        if i.xcor() > 355:
            race_on = False
            win = i.pencolor()
            if win == guess:
                print(f"You won! The {win} turtle won the race!")
            else:
                print(f"You lost! The {win} turtle won the race!")

        distance = random.randint(0,10)
        i.forward(distance)

screen.exitonclick()