import time
from turtle import Screen

from food import Food
from score import Score
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
snake = Snake()
food = Food()
food.food_dot()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_over = True
while is_game_over:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) <= 15:
        food.food_dot()
        score.scorer()
        snake.add_tim()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_over = False
        score.game_over()

    lst = snake.tims[1:]
    for tim in lst:
        if snake.head.distance(tim) < 10:
            is_game_over = False
            score.game_over()

screen.exitonclick()
