import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cars = []
player = Player()
car_man = CarManager()
score_board = Scoreboard()
score_board.write_level()
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")

game_is_on = True
x = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_man.create_car()
    car_man.move_cars()
    if player.level_up_p():
        score_board.write_level()
        car_man.update_level()
    for i in car_man.cars:
        if i.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

