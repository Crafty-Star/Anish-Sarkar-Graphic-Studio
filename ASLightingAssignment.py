from turtle import*
import random, time, math

def drawlbolt(clickx,clicky, movement = 0, width = 20, thecolor = 255):
    thewidth = width
    t.pencolor(thecolor,thecolor,thecolor)
    t.pensize(thewidth)
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
    end = False
    while x > -width and x < width and y > -height and y < height and not end:
        t.hideturtle() ##Drawing begins
        dx = random.randint(-10+movement,10+movement)
        dy = random.randint(-10,0)
        newx = x + dx
        newy = y + dy
        t.goto(newx, newy)##Drawing ends
        thecolor -=2##Edits begin
        t.pencolor(thecolor,thecolor,thecolor)
        ##Edits end
        if thewidth <= 1 or thecolor <= 0:##Checking begins
            ts.update()
            break
        thewidth = thewidth - 0.1999
        t.pensize(thewidth)##Width edit
        t.pencolor(thecolor,thecolor,thecolor)## Color edit
        x = newx##Coordinate edits
        y = newy
        if (width-abs(x))<0 or (height - abs(y)) < 0:
            ts.update()
            ##Checking ends
            break
        if random.randint(0,50) == 50:
            end = True
            drawlbolt(x,y,movement + 5, thewidth, thecolor)
            drawlbolt(x,y,movement - 5, thewidth, thecolor)
            ts.update()
            t.clear()
    return
t = Turtle()
ts = t.getscreen()    
ts.setup(width = 1200, height = 800)
ts.colormode(255)    
t.hideturtle()    
ts.tracer(1, 0)
ts.bgcolor("black")
##ts.setworldcoordinates(0, 0, -50, -50)
ts.bgpic("original.gif")
canvas = ts.getcanvas()
canvas.itemconfig(ts._bgpic, anchor="sw")  
ts.onclick(drawlbolt)

