from turtle import *
import random, time

t = Turtle()
ts = t.getscreen()
ts.setup(width = 1600, height = 1200)
ts.tracer(0,0)
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
ts.tracer(0,0)
ts.register_shape("stick.gif")
height = 0
limit = -335
hai = True
num = 0
def addTurtle():
    t = Turtle()
    t.shape("snow")
    t.color("white")
    t.fillcolor("white")
    t.setheading(heading)
    tlist.append(t)
    t.up()
    t.goto(random.randint(-750,750), random.randint(-300,300))
def makesnowman(size = 0):
    t = Turtle()
    t.hideturtle()
    t.color("white")
    t.fillcolor("white")
    t.up()
    t.up()
    t.begin_poly()
    t.fillcolor('white')
    t.circle(23+size)
    t.end_poly()
    p = t.get_poly()
    t.color("white")
    ts.register_shape("snow_one", p)
    t.up()
    t.begin_poly()
    t.fillcolor('white')
    t.circle(14+size)
    t.end_poly()
    p = t.get_poly()
    t.color("white")
    ts.register_shape("snow_two", p)
    t.up()
    t.begin_poly()
    t.fillcolor('white')
    t.circle(8+size)
    t.end_poly()
    p = t.get_poly()
    t.color("white")
    ts.register_shape("snow_three", p)
    t.up()
    t.begin_poly()
    t.color("black")
    t.circle(2+size)
    t.end_poly()
    p = t.get_poly()
    ts.register_shape("eye", p)
    t.left(90)
    t.fillcolor('white')
    t.goto(-200, -350)
    t.down()
    t.shape("snow_one")
    t.stamp()
    t.up()
    t.forward(37+size)
    t.down()
    t.shape("snow_two")
    t.stamp()
    t.up()
    t.forward(20+size)
    t.down()
    t.shape("snow_three")
    t.stamp()
    t.up()
    t.forward(15)
    t.left(90)
    t.forward(3*size/2)
    t.shape("eye")
    t.down()
    t.stamp()
    t.up()
    t.backward(3*size+0.2)
    t.down()
    t.stamp()
def snowman(size):
    print("80")
    t = Turtle()
##    t.penspeed(10)
    t.hideturtle()
    t.up()
    t.shape("stick.gif")
    t.goto(-200, -200)
    t.right(90)
    t.down()
    t.showturtle()
    t.forward(400)
    makesnowman((size/10)+5)
    
tlist = []
heading = 270  
for i in range(10):
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
                   
while hai == True:
    for flake in tlist:
        flake.setheading(heading)   
        flake.forward(random.randint(5,15))
        if flake.ycor() < limit:
            flake.shape("snow")
            flake.stamp()
            height += 0.005
            num += 1
            print("clo")
            limit += height
            if num%20 == 0:
                print("90")
                snowman(num)
                height = 0
                limit = -335
            if height > 15 or num == 50:
                height = 0
                limit = -335
            flake.goto(random.randint(-720,720), 300)
            flake.shape("snow")
            flake.setheading(270)
    ts.update()
    time.sleep(0.05)
