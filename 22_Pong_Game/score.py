from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman",20,"italic")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 270)
        self.write(f"{self.l_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 270)
        self.write(f"{self.r_score}", move=False, align=ALIGNMENT, font=FONT)


    def r_update(self):
        self.clear()
        self.r_score += 1
        self.update_score()

    def l_update(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=("Times New Roman", 20, "italic"))
        self.goto(0, -30)
        if self.l_score > self.r_score:
            self.write(f"🤩LEFT PLAYER WINS🤩", move=False, align=ALIGNMENT, font=("Times New Roman", 20, "italic"))
        if self.l_score < self.r_score:
            self.write(f"🤩RIGHT PLAYER WINS🤩", move=False, align=ALIGNMENT, font=("Times New Roman", 20, "italic"))
        if self.l_score == self.r_score:
            self.write(f"🤩ITS A DRAW🤩", move=False, align=ALIGNMENT, font=("Times New Roman", 20, "italic"))
