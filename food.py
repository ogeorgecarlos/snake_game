from turtle import Turtle
from random import randint

FOOD_COLOR = 'white'
FOOD_SHAPE = 'circle'
FOOD_SIZE = 0.5
FOOD_SPEED = 'fastest'


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color(FOOD_COLOR)
        self.shape(FOOD_SHAPE)
        self.shapesize(FOOD_SIZE)
        self.penup()
        self.speed(FOOD_SPEED)
        self.setposition(randint(-280, 280), randint(-280, 280))

    def change_position(self):
        self.setposition(randint(-280, 280), randint(-280, 280))
