from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def y_bounce(self):
        self.y_move = self.y_move * -1

    def x_bounce(self):
        self.x_move = self.x_move * -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()