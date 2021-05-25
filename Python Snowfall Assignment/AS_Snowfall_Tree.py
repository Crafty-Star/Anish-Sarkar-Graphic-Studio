from turtle import *
import random, time

t = Turtle()
ts = t.getscreen()
ts.setup(width = 1600, height = 1200)
ts.tracer(0)
t.hideturtle()
ts.bgcolor("black")
ts.bgpic("Forest2.gif")
t.hideturtle()
t.up()
t.begin_poly()
t.fillcolor('white')
t.circle(10)
t.end_poly()
p = t.get_poly()
ts.register_shape("snow", p)
t.shape("snow")
ts.register_shape("NH-tree.gif")
height = 0
limit = -335
def createtree():##GO TREES!
    t = Turtle()
    t.hideturtle()
    t.shape("MH-tree.gif")
    t.goto(random.randint(-750, 750), random.randint(-320, -335))
def addTurtle():
    t = Turtle()
    t.shape("snow")
    t.color('white')
    t.fillcolor("white")
    t.setheading(heading)
    tlist.append(t)
    t.up()
    t.goto(random.randint(-750,750), random.randint(-300,300))
tlist = []
heading = 270  
for i in range(5):
    addTurtle()
def blowleft():
    global heading
    heading -= 5
def blowright():
    global heading
    heading += 5
def mouseclick(x, y):
    addTurtle()
    
ts.listen()          
ts.onkeypress(blowleft, "Left")
ts.onkeypress(blowright, "Right")
ts.onclick(mouseclick)
                   
while True:
    for flake in tlist:
        flake.setheading(heading)   
        flake.forward(random.randint(10,30))
        if flake.ycor() < limit:
            flake.shape("snow")
            flake.stamp()
            height += 0.0001
            limit += height
            flake.goto(random.randint(-720,720), 300)
            flake.shape("snow")
            flake.setheading(270)
    ts.update()
    time.sleep(0.05)
