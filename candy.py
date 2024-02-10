import turtle
class Create_boundary():
    """
    creates boudaries of boxes
    """
    def __init__(self):
        self.walls = []
        self.create_boundary()
        self.wall1()


    def create_boundary(self):
        x=turtle.Turtle()
        x.hideturtle()
        x.penup()
        x.goto(250, -250)
        x.pendown()
        x.pensize(3)
        x.goto(250, 250)
        x.goto(-250, 250)
        x.goto(-250, -250)
        x.goto(250, -250)

    def wall1(self):
            y = turtle.Turtle()
            y.penup()
            y.showturtle()
            y.shape('square')
            y.goto(0, -150)
            y.shapesize(stretch_wid=10, stretch_len=0.25)
            self.walls.append(y)


