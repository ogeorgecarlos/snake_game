from turtle import Turtle, Screen

text_score = 'Current Score: '
text_score_color = 'white'


class Turtle_text(Turtle):
    def __init__(self):
        super().__init__()
        self.color(text_score_color)
        self.penup()
        self.hideturtle()
        self.score = 0

    def scoreboard(self):
        self.clear()
        self.setposition(-50, 280)
        self.write(f'{text_score}{self.score}', font=('arial', 12, 'bold'))

    def game_over(self):
        self.setposition(-80, 0)
        self.pencolor('red')
        self.write('GAME OVER!', 'center', font=('arial', 20, 'bold'))

    def update_score(self):
        self.score += 1

'''
s = Screen()
s.screensize(600, 600)
s.bgcolor('black')




teste = Turtle_text()
teste.scoreboard()




s.exitonclick()'''
