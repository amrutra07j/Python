from turtle import Turtle
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
class Snake:
    def __init__(self):
        self.tims = []
        self.create_snake()
        self.head = self.tims[0]

    def create_snake(self):
        post = 0
        for i in range(3):
            tim = Turtle("square")
            tim.color("white")
            tim.up()
            tim.goto(post, 0)
            self.tims.append(tim)
            post -= 20

    def move_snake(self):
        for i in range(len(self.tims) - 1, 0, -1):
            self.tims[i].goto(self.tims[i - 1].xcor(), self.tims[i - 1].ycor())
        self.tims[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_tim(self):
        tim = Turtle("square")
        tim.color("white")
        tim.up()
        x = self.tims[-1].xcor()+20
        y = self.tims[-1].ycor()
        tim.goto(x, y)
        self.tims.append(tim)

