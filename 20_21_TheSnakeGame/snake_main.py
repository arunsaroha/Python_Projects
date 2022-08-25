import time
from turtle import Screen
from snake_move import Snake
from food import Food
from score import Score

# setting up screen
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

# using snake class
snake = Snake()
# using food class
food = Food()
# using score class
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.inc_score()

#     detect collision with wall
    if snake.head.xcor() > 490 or snake.head.ycor() > 290 or snake.head.xcor() < -490 or snake.head.ycor() < -290:
        score.reset_score()
        snake.snake_reset()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.snake_reset()


screen.exitonclick()