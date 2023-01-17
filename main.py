from snake import Snake
from food import Food
from turtle_text import Turtle_text
from turtle import Screen
from time import sleep

# turtles on screen
snake = Snake()
food = Food()
turtle_text = Turtle_text()

# Screen's set
# -----------------------
WIDTH = 600
HEIGHT = 600
COLOR = 'black'
TITLE = 'My Snake Game'
GO_UP = 'Up'
GO_DOWN = 'Down'
GO_LEFT = 'Left'
GO_RIGHT = 'Right'

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(COLOR)
screen.title(TITLE)
screen.listen()
screen.tracer(0)

screen.onkey(snake.up, GO_UP)
screen.onkey(snake.right, GO_RIGHT)
screen.onkey(snake.down, GO_DOWN)
screen.onkey(snake.left, GO_LEFT)
# -----------------------

SLEEP_SPEED = 0.1
SNAKE_NAIL_COLOR = 'white'
DISTANCE_TO_GET_FOOD = 15
DISTANCE_TO_COLISION_NAIL = 15


game_is_on = True
while game_is_on:
    screen.update()
    snake.list_t[-1].color(SNAKE_NAIL_COLOR)
    sleep(SLEEP_SPEED)
    snake.move()

    # check if snake get a food and update you size
    turtle_text.scoreboard()
    if snake.head.distance(food) < DISTANCE_TO_GET_FOOD:
        turtle_text.update_score()
        food.change_position()
        snake.get_food()

    # check if snack chocks with the wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        snake.reset()
        turtle_text.reset_score()

    # Check if the snake chocks with your own tails
    for n in snake.list_t[1:]:
        if snake.head.distance(n) < DISTANCE_TO_COLISION_NAIL:
            snake.reset()
            turtle_text.reset_score()

screen.exitonclick()