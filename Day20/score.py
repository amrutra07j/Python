from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(0, 270)
        self.write(arg=f"Your Score : {self.score}", align="center", font=('Courier', 15, 'normal'))

    def scorer(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Your Score : {self.score}", align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=('Courier', 15, 'normal'))
