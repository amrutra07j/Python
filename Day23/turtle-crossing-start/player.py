from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.speed("fastest")

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+10)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-10)

    def move_right(self):
        self.goto(self.xcor()+10, self.ycor())

    def move_left(self):
        self.goto(self.xcor()-10, self.ycor())

    def level_up_p(self):
        if self.ycor() >= 280:
            self.goto(STARTING_POSITION)
            return True

