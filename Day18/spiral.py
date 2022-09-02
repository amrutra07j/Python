from turtle import Turtle, Screen
import random
tim = Turtle()
Screen().colormode(255)
rad = 100
x, y = 0, 0
tim.speed("fastest")
tim.pensize(1)
head = 0
for _ in range(36):
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    tim.color((r, g, b))
    tim.circle(rad)
    head += 10
    tim.setheading(head)
Screen().exitonclick()
