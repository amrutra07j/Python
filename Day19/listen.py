from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counter_clock():
    tim.left(10)

def move_clock():
    tim.right(10)

def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="A", fun=move_counter_clock)
screen.onkey(key="D", fun=move_clock)
screen.onkey(key="C", fun=clear)
screen.exitonclick()