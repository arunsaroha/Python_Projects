from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman",14,"italic")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.new_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"SCORE = {self.new_score} HIGH SCORE: {self.high_score}", move=False, align="center",
                   font=("Times New Roman", 12, "italic"))

    def reset_score(self):
        if self.new_score > self.high_score:
            self.high_score = self.new_score
            with open("data.txt", mode="w") as data:
                data.write(str(self.new_score))
        self.new_score = 0
        self.score_update()

    def inc_score(self):
        self.new_score += 1
        self.score_update()
