import turtle
import random
colours=['Green','Red','Blue','Orange','Yellow','Brown','Purple','Black','Violet']
class Food(turtle.Turtle):
    """
    Created food for the turtl
    """
    def __init__(self):
        super().__init__()
        self.createfood()

    def createfood(self):
        self.shape('circle')
        self.shapesize(0.5)
        self.color(random.choice(colours))
        self.penup()
        self.hideturtle()
        xcornew=random.choice([i for i in range(-230,230) if i not in range(-5,6)])
        ycornew=random.randint(-230,230)
        self.goto(xcornew,ycornew)
        self.showturtle()
