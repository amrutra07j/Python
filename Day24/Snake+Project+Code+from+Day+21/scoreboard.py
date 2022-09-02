from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high.txt", "r") as high:
            self.high_score = int(high.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def up_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high.txt", "w") as high:
                high.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
