from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.up()
        self.resizemode("user")
        self.shapesize(0.5, 0.5)


    def food_dot(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

