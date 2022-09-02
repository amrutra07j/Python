import time
from turtle import Screen
from ball import Ball
from pad import Pad
from score import Score

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.listen()

pad_r = Pad(380)
pad_l = Pad(-380)
ball = Ball()
score = Score()
screen.onkey(pad_r.move_up, "Up")
screen.onkey(pad_r.move_down, "Down")
screen.onkey(pad_l.move_up, "w")
screen.onkey(pad_l.move_down, "s")

is_game_on = True
timer = 0.1
while is_game_on:
    time.sleep(timer)
    screen.update()
    score.update_score()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        print("yeah")
        ball.y_bounce()
    if ball.xcor() >= 360 and ball.distance(pad_r) < 50 or ball.xcor() <= -360 and ball.distance(pad_l) < 50:
        ball.x_bounce()

    if ball.xcor() >= 380:
        ball.reset_position()
        score.left_score()
    elif ball.xcor() <= -380:
        ball.reset_position()
        score.right_score()

screen.exitonclick()