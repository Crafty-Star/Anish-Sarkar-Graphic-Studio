from turtle import*
import random, time

def drawlbolt(clickx,clicky):
    t.pencolor(255,255,255)
    t.width(4)
    t.up()
    t.goto(clickx, clicky)
    t.down()
    x = clickx
    y = clicky
    width = ts.window_width()/2   
    height = ts.window_height()/2 
    while x < height:              
        dx = random.randint(-10,10)
        dy = random.randint(-10,10)
        newx = x + dx
        newy = y + dy
        t.goto(newx, newy)
        x = newx
        y = newy
    ts.update()
    time.sleep(0.25)
    t.clear()

t = Turtle()
ts = t.getscreen()    
ts.setup(800, 600)    
ts.colormode(255)     

t.hideturtle()
          
ts.tracer(100)
ts.bgcolor("black")   
ts.onclick(drawlbolt)
