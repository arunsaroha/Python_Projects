# one way of importing classes --- one by one
# from turtle import Turtle, Screen
# another way of importing classes --- all at once
# use them according to your convenience
# from turtle import *
# another method --- aliasing modules like
import turtle as t
import random
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
# "SeaGreen"]
tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
# completely random color
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    d = (r, g, b)
    return d


# # draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# # draw a dashed line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# # draw different shapes all at once
# for i in range(3, 16):
#     for j in range(1, i+1):
#         tim.forward(50)
#         tim.left(360/i)


# # draw different shapes by a function
# def draw_shape(num_sides):
#     angle = 360/ num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.left(angle)
# for n in range(3,11):
#     draw_shape(n)


# # random walk
# directions = [0, 90, 180, 270]
# for i in range(200):
#     tim.color(random_color())
#     tim.width(5)
#     tim.forward(50)
#     tim.speed("fastest")
#     tim.setheading(random.choice(directions))


# # make a spirograph
# def draw_spirograph(size_of_gap):
#     tim.speed("fastest")
#     for i in range(int(360/size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
# draw_spirograph(20)

