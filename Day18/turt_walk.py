import random
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")
tim.pensize(10)
for i in range(100):
# while True:
    rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    get = random.choice([90, 180, 0, 270])
    tim.color(rgb)
    tim.left(get)
    tim.forward(20)
    a = tim.pos()
    print(a)
    if abs(a[0]) > 320 or abs(a[1]) > 320:
        tim.up()
        tim.setpos(0, 0)
        tim.down()
# tim.forward(320)
screen.exitonclick()

