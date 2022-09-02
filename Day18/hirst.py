# import colorgram
# colors = colorgram.extract('hirst.jfif', 50)
# color_list = list()
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))
import turtle
from turtle import Turtle, Screen
import random

Screen().colormode(255)
color_list = [(230, 225, 219), (216, 232, 220), (237, 220, 228), (221, 225, 236), (216, 152, 103), (227, 209, 101),
              (124, 165, 187), (131, 177, 148), (42, 109, 156), (162, 14, 26), (45, 125, 58), (178, 71, 41),
              (234, 81, 49), (236, 209, 4), (15, 60, 35), (190, 176, 20), (12, 97, 37), (150, 71, 84), (170, 19, 12),
              (229, 61, 74), (14, 41, 74), (190, 140, 149), (49, 21, 15), (80, 13, 20), (57, 168, 79), (234, 169, 161),
              (15, 57, 132), (168, 208, 175), (48, 153, 188), (237, 162, 172), (79, 124, 185), (159, 205, 215),
              (253, 6, 23), (172, 192, 216), (31, 75, 92), (255, 10, 3), (71, 72, 41)]
tim = Turtle()
tim.up()
tim.hideturtle()
tim.backward(200)
tim.left(90)
tim.forward(250)
tim.right(90)
tim.down()
tim.speed("fastest")
for i in range(10):
    for _ in range(10):
        rgb = random.choice(color_list)
        tim.color(rgb)
        tim.begin_fill()
        tim.dot(20, rgb)
        tim.end_fill()
        tim.up()
        tim.forward(50)
        tim.down()
    tim.up()
    if i % 2 == 0:
        tim.right(90)
        tim.forward(50)
        tim.right(90)
        tim.forward(50)
        tim.down()
    else:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(50)
        tim.down()
    # tim.right(90)
    # tim.forward(50)
    # tim.right(90)
    # tim.forward(500)
    # tim.right(180)
    # tim.down()


Screen().exitonclick()
