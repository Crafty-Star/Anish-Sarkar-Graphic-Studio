from turtle import*
import random, time, math
def burn(x,y):
    t = Turtle()
    t.hideturtle()
    for awy in range(1,11):
        xr = random.randint(-5,100)
        yr = random.randint(-1,100)
        t.up()
        t.goto(x+xr,y+yr)
        t.down()
        t.shape("flame_ONE.gif")
        t.stamp()
    time.sleep(0.5)
##    t.update()
def growtree(x,y):
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(x,y)
    t.shape("NH-Tree.gif")
    t.stamp()
def db(clickx,clicky):
##    treecoords = trees()
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
        if thewidth <= 1 or thecolor <= 0 or newy <= -300:
            t.up()
            growtree(newx,newy+50)
##            t.update()
            time.sleep(0.5)
            burn(newx,newy)
            t.clear()
            break
        t.pencolor(thecolor,thecolor,thecolor)
        thewidth -= .1999
        t.pensize(thewidth)
        t.pencolor(thecolor,thecolor,thecolor)
        x = newx
        y = newy
##        for xcope in treecoords:
##            if abs(x - int(xcope)) < 15 and abs(y - (-400)) < 15:
##                

t = Turtle()
ts = t.getscreen()    
ts.setup(width = 1400, height = 850)
ts.colormode(255)    
ts.register_shape("NH-Tree.gif")
ts.register_shape("flame_ONE.gif")
ts.register_shape("Forest2.gif")
print("hi")
t.hideturtle()    
print("bye")
ts.tracer(1,0.9)
ts.bgcolor("black")
##ts.setworldcoordinates(0, 0, -50, -50)
ts.bgpic("Forest2.gif")
##canvas = ts.getcanvas()
##canvas.itemconfig(ts._bgpic, anchor="sw") 
ts.listen()  
ts.onclick(db,btn = 1)
##ts.onclick(trees, btn = 2)
