from turtle import Screen
from snake import Snake

snake = Snake()

# Screen's set
# -----------------------
s_width = 600
s_height = 600
s_color = 'black'
s_title = 'My Snake Game'

screen = Screen()
screen.setup(width=s_width, height=s_height)
screen.bgcolor(s_color)
screen.title('My Snake Game')
screen.listen()
screen.tracer(0)

screen.onkey(snake.up, 'Up')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
# -----------------------