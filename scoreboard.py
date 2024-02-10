import turtle
class Score(turtle.Turtle):
    """
    Calculates score of the user
    """
    def __init__(self):
        super().__init__()
        self.score=0
        self.createscore()
    def createscore(self):
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.write(f'Score :{self.score}',font='Arial' )

    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f'Score :{self.score}',font='Arial' )

    def game_over(self):
        self.clear()
        self.penup()
        self.home()
        self.write('GAMEOVER', align='center', font='Arial')
        self.goto(0, -30)
        self.write(f'Your Score:{self.score}', align='center', font='Arial')



