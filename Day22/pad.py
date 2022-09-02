from turtle import Turtle

class Pad(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.up()
        self.shapesize(1, 4)
        self.goto(x_cor, 0)
        self.setheading(90)

    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        self.setheading(270)
        self.forward(20)