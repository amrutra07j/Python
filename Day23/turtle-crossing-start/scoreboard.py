from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.hideturtle()
        self.color("black")
        self.setheading(90)
        self.speed("fastest")
        self.level = 0

    def write_level(self):
        self.clear()
        self.level += 1
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align='center', font=('Courier', 30, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=('Courier', 30, 'normal'))
