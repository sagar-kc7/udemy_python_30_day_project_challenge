# import colorgram
# colors = colorgram.extract('image.jpg', 8)

# rgb_col = []
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_col = (r, g, b)
#     rgb_col.append(new_col)
# print(rgb_col)

color_list = [(199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), (222, 223, 226)]


from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.speed(0)
colormode(255)
tim.hideturtle()
tim_y_pos = 0.0


def draw():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.pu()
        tim.forward(50)
        tim.pd()

for _ in range(10):
    draw()
    tim.pu()
    tim_y_pos = tim.ycor() + 40.0
    tim.sety(tim_y_pos)
    tim.setx(0.0)
    tim.pd()

screen = Screen()
screen.exitonclick()
