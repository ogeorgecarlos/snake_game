from turtle import Turtle
from time import sleep

color = 'white'
shape = 'square'
move = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
x = 2


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.create_snake()
        self.head = self.list_t[0]

    def create_snake(self):
        x_position = 20
        self.list_t = []
        for my_turtle in range(3):
            x_position -= 20
            my_turtle = Turtle()
            my_turtle.shape(shape)
            my_turtle.color(color)
            my_turtle.penup()
            my_turtle.speed(10)
            my_turtle.setpos(x_position, 0)
            self.list_t.append(my_turtle)

    def get_food(self):
        my_turtle = Turtle()
        my_turtle.shape(shape)
        my_turtle.color('black')
        my_turtle.penup()
        my_turtle.speed(10)
        self.list_t.append(my_turtle)
        my_turtle.setposition(self.list_t[-1].xcor(),self.list_t[-1].ycor())

    def move(self):
        for n in range(len(self.list_t)-1, 0, -1):
            self.list_t[n].goto(self.list_t[n-1].pos())
        self.head.fd(move)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
            
