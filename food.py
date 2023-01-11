from turtle import Turtle, Screen
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(0.5)
        self.penup()
        self.speed('fastest')
        self.setposition(randint(-280, 280), randint(-280, 280))

    def change_position(self):
        self.setposition(randint(-280, 280), randint(-280, 280))