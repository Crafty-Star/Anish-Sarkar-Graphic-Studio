from turtle import *
import random, time

class Bacteria(Turtle):
    def __init__(self, color = "red", x=400, y=400):
        Turtle.__init__(self)
        self.shape("circle")
        self.up()
        self.goto(x,y)
        self.color("black", color)  # Specify both the outline and fill color
        self.resizemode("user")
        rnd = random.uniform(1.0,2.0)
        self.shapesize(rnd, rnd)    # Does not work for GIF files!
        
    def moveRandomly(self):
        newx = self.xcor() + random.randint(-5,5)
        newy = self.ycor() + random.randint(-5,5)
        self.goto(newx, newy)
        
    def moveAwayFromTarget(self, x, y):
        self.setheading(self.towards(x,y) + 180)
        self.forward(random.randint(2,5))
        
    def isCloseTo(self, x, y):
        if abs(self.xcor() - x) < 10 and abs(self.ycor() - y) < 10:
            return True
        else:
            return False
        
    def commitSuicide(self):
        self.hideturtle()
        print("You lost a piece of bacteria!")

    def stayOnScreen(self, pixelborder):
        newx = self.xcor()
        newy = self.ycor()
        if self.xcor() < pixelborder:
            newx = pixelborder
        if self.ycor() < pixelborder:
            newy = pixelborder
        if self.xcor() > self.getscreen().window_width() - pixelborder:
            newx = self.getscreen().window_width() - pixelborder
        if self.ycor() > self.getscreen().window_height() - pixelborder:
            newy = self.getscreen().window_height() - pixelborder
        self.goto(newx, newy)
        

class Killer(Turtle):
    def __init__(self, color = "black", x=200, y=200):
        Turtle.__init__(self)
        self.shape('square')
        self.up()
        self.goto(x,y)
        self.fillcolor(color)
        
# Contains the coordiates of the mouse as it moves
mousex = 600
mousey = 400

# List that contains all the bacteria
blist = []

screen = Screen()
screen.colormode(255)
screen.tracer(0)                   # Use automatic updates

def motion(event):
    global mousex
    global mousey
    mousex = event.x
    mousey = event.y
    
canv = screen.getcanvas()   # Only the canvas can detect a mouse motion
canv.bind('<Motion>', motion)
# Change everything to canvas coordinates
# x is now between 0 and screen.window_width()
# y is now between 0 and screen.window_height()
screen.setworldcoordinates(0, screen.window_height(), screen.window_width(), 0)

t = Turtle()
t.up()
t.goto(400, 300)
t.down()
t.circle(200)

score = 0

# Make five bacteria to start with
for i in range(5):
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    
    cb = Bacteria((red,green,blue))
    blist.append(cb)

# Make the killer square, which will follow the mouse
killer = Killer()
    
while True:
    # Move the killer to the current mouse position
    killer.goto(mousex, mousey)
    for b in blist:
        b.moveRandomly()
        b.moveAwayFromTarget(killer.xcor(), killer.ycor())
        # Will stay 75 pixels away from the edge of the screen
        b.stayOnScreen(75)
        if b.isCloseTo(killer.xcor(), killer.ycor()):
            b.commitSuicide()

        # b.xcor()  and  b.ycor()  tell you where the bacteria is
        #  If those coordinates are outside the dish, subtract one from the score
        
    screen.update()
    time.sleep(0.001)
