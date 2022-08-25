from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# setting up screen
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("MY PONG GAME")
screen.tracer(0)

# paddles
r_paddle = Paddle(470, 0)
l_paddle = Paddle(-480, 0)

# paddles movement
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# ball
ball = Ball()

# score
score = Score()


game_is_on = True
while game_is_on:
    time.sleep(ball.sleep)
    screen.update()
    ball.move()
    # detect bounce with walls
    if ball.ycor() > 260 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 440:
        ball.bounce_x()

    # detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -450:
        ball.bounce_x()

    # detect a right paddle miss
    if ball.xcor() > 470:
        score.l_update()
        ball.reset_ball()
        ball.bounce_x()

    # detect a left paddle miss
    if ball.xcor() < -480:
        score.r_update()
        ball.reset_ball()
        ball.bounce_x()

    if score.r_score > 4 or score.l_score > 4:
        game_is_on = False
        score.game_over()



screen.exitonclick()