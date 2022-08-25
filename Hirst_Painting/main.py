# drawing the dots
import turtle as t
import random
# import colorgram
# # extracting some colors from the image using colorgram
# colors = colorgram.extract('hirst.jpg', 10)
# print(colors)
# rgb_colors = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

rgb_colors = [(216, 168, 79), (81, 110, 153), (117, 162, 208), (107, 174, 137), (191, 123, 161), (70, 127, 98),
              (128, 23, 63)]
tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
t.colormode(255)  # changing the color mode

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

for i in range(10):
    for j in range(10):
        tim.speed("fastest")
        tim.dot(20, random.choice(rgb_colors))
        tim.penup()
        tim.forward(50)
    tim.left(90)
    tim.penup()
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)


screen = t.Screen()
screen.exitonclick()  # this holds the popup screen until we click inside it.