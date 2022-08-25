import turtle
import pandas
screen = turtle.Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")
name = states.state.to_list()
guesses = []
while len(guesses) < 50:
    ask_user = (screen.textinput(title=f"{len(guesses)}/50 States Correct",prompt="What's your guess?")).title()
    if ask_user == "Exit":
        missed = [st for st in name if st not in guesses]
        new_data = pandas.DataFrame(missed)
        new_data.to_csv("states_to_learn.csv")
        exit()

    if ask_user in name:
        guesses.append(ask_user)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.speed("fastest")
        x_co = states[states.state == ask_user].x
        y_co = states[states.state == ask_user].y
        t.goto(x=int(x_co), y=int(y_co))
        t.write(ask_user)

screen.exitonclick()