from variables import snake, food, turtle_text
from my_screen import screen
from time import sleep

game_is_on = True
while game_is_on:
    screen.update()
    snake.list_t[-1].color('white')
    sleep(0.1)
    snake.move()

    # check if snake get a food and update you size
    turtle_text.scoreboard()
    if snake.list_t[0].distance(food) < 15:
        turtle_text.update_score()
        food.change_position()
        snake.get_food()

    # check if snack chocks with the wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        turtle_text.game_over()
        game_is_on = False

    # Check if the snake chocks with your own tails
    for n in snake.list_t[1:]:
        if snake.head.distance(n) < 15:
            turtle_text.game_over()
            game_is_on = False

screen.exitonclick()