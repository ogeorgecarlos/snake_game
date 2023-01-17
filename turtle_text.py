from turtle import Turtle

text_score = 'Current Score: '
text_hscore = 'High Score: '
text_score_color = 'white'


class Turtle_text(Turtle):
    def __init__(self):
        
        super().__init__()
        self.color(text_score_color)
        self.penup()
        self.hideturtle()
        self.score = 0
        with open('high_score.txt', 'r') as file:
            self.higscore = int(file.read())

    def scoreboard(self):
        self.clear()
        self.setposition(-150, 280)
        self.write(f'{text_score}{self.score}, {text_hscore}{self.higscore}', font=('arial', 12, 'bold'))

    def game_over(self):
        self.setposition(-80, 0)
        self.pencolor('red')
        self.write('GAME OVER!', 'center', font=('arial', 20, 'bold'))

    def update_score(self):
        self.score += 1
        if self.score > int(self.higscore):
            self.higscore = self.score
            with open('high_score.txt', 'w') as file:
                file.write(str(self.higscore))

    def reset_score(self):
        self.score = 0


'''
s = Screen()
s.screensize(600, 600)
s.bgcolor('black')




teste = Turtle_text()
teste.scoreboard()




s.exitonclick()'''
