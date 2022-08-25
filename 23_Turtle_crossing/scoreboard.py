from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(x=-290, y=260)
        self.new_score = 0
        self.write(f"SCORE = {self.new_score}", move=False, font=FONT)

    def score_update(self):
        self.new_score += 1
        self.clear()
        self.write(f"SCORE = {self.new_score}", move=False, font=FONT)


    def game_over(self):
        self.goto(-100,0)
        self.write(f"GAME OVER", move=False, font=FONT)
        # self.write(f"FINAL SCORE = {self.new_score}", move=False, font=FONT)

