import random
import turtle as t
colours=['Green','Red','Blue','Orange','Yellow','Brown','Purple','Black','Violet','Magenta','DarkOrchid','Bisque',
         'DarkOliveGreen','LightSkyBlue','DarkGray','OrangeRed','Tan']
coor=[0,-20,-40]
class Snake_body():
    def __init__(self):
        self.segments=[]
        self.create_snake()


    def create_snake(self):
        for i in range(3):
            x = t.Turtle()
            x.shape('square')
            x.penup()
            x.goto(coor[i],0)
            self.segments.append(x)

    def move_snake(self):
        for i  in range(len(self.segments)-1, 0, -1):
            newcoordxx=self.segments[i - 1].xcor()
            newcoordyy=self.segments[i - 1].ycor()
            self.segments[i].goto(newcoordxx, newcoordyy)
        self.segments[0].forward(20)
    def moveup(self):
        if self.segments[0].heading() !=270:
            self.segments[0].setheading(90)
    def movedown(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def moveleft(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def moveright(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def add_segments(self):
        x = t.Turtle()
        x.shape('square')
        x.penup()
        x.hideturtle()
        x.color(random.choice(colours))
        x.goto(self.segments[-1].xcor(),self.segments[-1].ycor())
        x.showturtle()
        self.segments.append(x)







