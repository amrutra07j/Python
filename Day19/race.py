import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 480)
color = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black"]
y = -220
tims = []
for i in range(8):
    tim = Turtle("turtle")
    tim.color(color[i])
    tim.up()
    y += 50
    tim.goto(-230, y)
    tims.append(tim)

tom = Turtle()
tom.hideturtle()
tom.speed("fastest")
tom.up()
tom.goto(230, -220)
tom.down()
tom.setheading(90)
tom.forward(440)

choice = screen.textinput(title="Select winner", prompt="Which one will one?")

game_start = True
while game_start:
    for i in tims:
        i.speed("fastest")
        i.forward(random.randint(0, 10))
        if i.xcor() >= 210:
            print(f"{i.color()[0]} is the winner")
            if i.color()[0] == choice:
                print("You are the winner and you owe a party to me ")
            else:
                print(f"you are as useless as {choice} turtle")

            game_start = False
            break

screen.exitonclick()
