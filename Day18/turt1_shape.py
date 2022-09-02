from turtle import Turtle, Screen
import random

tim = Turtle()
my_screen = Screen()
tim.shape("turtle")
tim.color("red")
run = 10
i = 2
my_screen.colormode(255)
for i in range(3, 11):
    deg = 360/i
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    tim.color((r, g, b))
    for j in range(i):
        tim.forward(100)
        tim.right(deg)
my_screen.exitonclick()