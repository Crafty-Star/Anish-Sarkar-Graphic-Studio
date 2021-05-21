from turtle import*
import random, time, math

def db(clickx,clicky):
    thecolor = 255
    thewidth = 20
    t = Turtle()
    t.hideturtle()
    t.clear()
    t.pensize(thewidth)
    t.pencolor(thecolor,thecolor,thecolor)
    t.up()
    t.goto(clickx, clicky)
    t.down()
    t.stamp()
    x = clickx
    y = clicky
##    width = ts.window_width()/2  
##    height = ts.window_height()/2
    width  =600
    height =400
    while x < height:
        dx = random.randint(-7,7)
        dy = random.randint(-15,0)
        newx = x + dx
        newy = y + dy
        t.goto(newx, newy)
        thecolor -=2
        if thewidth <= 1 or thecolor <= 0:
            ts.update()
            t.clear()
            break
        t.pencolor(thecolor,thecolor,thecolor)
        thewidth -= .1999
        t.pensize(thewidth)
        t.pencolor(thecolor,thecolor,thecolor)
        x = newx
        y = newy
        if (width-abs(x))<0 or (height - abs(y)) < 0:
            ts.update()
            t.clear()
    ts.update()
    t.clear()

t = Turtle()
ts = t.getscreen()    
ts.setup(width = 1200, height = 800)
ts.colormode(255)    
ts.register_shape("Cloud.gif")
t.shape("Cloud.gif")
t.hideturtle()    
ts.tracer(1, 0)
ts.bgcolor("black")
##ts.setworldcoordinates(0, 0, -50, -50)
ts.bgpic("original.gif")
canvas = ts.getcanvas()
canvas.itemconfig(ts._bgpic, anchor="sw")  
while True:
    order = list(range(-200, 200, 20))
    random.shuffle(order)
    for x in order:
        db(x*2, 200)
