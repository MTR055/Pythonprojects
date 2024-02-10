import time
import turtle as t
import snake
import food
import scoreboard
import candy

my_screen=t.Screen()
my_screen.screensize(250,250)
my_screen.tracer(0)

turt=snake.Snake_body()
food=food.Food()
score=scoreboard.Score()
boundary=candy.Create_boundary()


mode=my_screen.textinput('select mode','custom or classic')
my_screen.onkey(turt.moveup,'Up')
my_screen.onkey(turt.movedown,'Down')
my_screen.onkey(turt.moveright,'Right')
my_screen.onkey(turt.moveleft,'Left')
my_screen.listen()


game_is_on=True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    turt.move_snake()
    if  food.distance(turt.segments[0]) <15:
        food.clear()
        food.createfood()
        turt.add_segments()
        score.update_score()
    if mode=='custom':
        if turt.segments[0].xcor()>250 or turt.segments[0].xcor()<-250 or turt.segments[0].ycor()>250 or turt.segments[0].ycor()<-250:
            score.game_over()
            game_is_on=False
    if mode=='classic':
        if turt.segments[0].xcor()>245 or turt.segments[0].xcor()<-245:
            turt.segments[0].goto(-turt.segments[0].xcor(),turt.segments[0].ycor())
        if turt.segments[0].ycor() > 245 or turt.segments[0].ycor() < -245:
            turt.segments[0].goto(turt.segments[0].xcor(), -turt.segments[0].ycor())
    for i in range(1,len(turt.segments)):
        if turt.segments[0].distance(turt.segments[i])<10:
            score.game_over()
            game_is_on=False
    if abs(turt.segments[0].xcor()-boundary.walls[0].xcor())<5 and abs(turt.segments[0].ycor()-boundary.walls[0].ycor())<100:
        score.game_over()
        game_is_on = False













my_screen.exitonclick()