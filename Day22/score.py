from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.up()
        self.l_score = 0
        self.r_score = 0

    def update_score(self):
        self.clear()
        self.goto(0, -350)
        self.down()
        self.goto(0, 350)
        self.up()
        self.goto(-50, 200)
        self.write(f"{self.l_score}", align='center', font=('Courier', 80, 'normal'))
        self.goto(50, 200)
        self.write(f"{self.r_score}", align='center', font=('Courier', 80, 'normal'))

    def left_score(self):
        self.l_score += 1

    def right_score(self):
        self.r_score += 1
