from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()
my_screen.canvheight = 1000
print(my_screen.canvheight)
my_turtle.shape("turtle")
my_turtle.forward(200)
my_turtle.color("chartreuse")
my_screen.exitonclick()
