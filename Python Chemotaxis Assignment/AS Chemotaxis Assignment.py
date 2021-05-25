from turtle import *
import random, time

class Bacteria(Turtle):
    def __init__(self, color = "red", x=0, y=0):
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
        
    def moveTowardsTarget(self, x, y):
        self.setheading(self.towards(x,y))
        self.forward(random.randint(10,30))
        
    def isCloseTo(self, x, y):
        if abs(self.xcor() - x) < 10 and abs(self.ycor() - y) < 10:
            return True
        else:
            return False
        
    def getLarger(self):
        currentxscale = self.shapesize()[0]
        currentyscale = self.shapesize()[1]
        self.shapesize(currentxscale + 0.1, currentyscale + 0.1)
        

class Food(Turtle):
    def __init__(self, color = "black", x=200, y=200):
        Turtle.__init__(self)
        self.shape('square')
        self.up()
        self.goto(x,y)
        self.fillcolor(color)
        
    def moverandomly(self):
        newx = self.xcor() + random.randint(-10,10)
        newy = self.ycor() + random.randint(-10,10)
        self.goto(newx, newy)
def changeRepulsion(clickx, clicky):
    repulseon = not repulseon

blist = []
# Initially they are attracted towards the origin
repulseon = False

# A mouse click changes the repulsion from on to off       
def changeRepulsion(clickx, clicky):
    global repulseon
    repulseon = not repulseon

# Contains the coordiates of the mouse as it moves
mousex = 0
mousey = 0
screen = Screen()
screen.colormode(255)
screen.tracer(0)

f = Food()
score = 0

# This will work since the basic Turtle goto has two input parameters
# Move the food to the mouse position on a click
screen.onclick(f.goto)

# You don't need targetx and targety variables in this program,
#   since the bacteria always move towards the food

# Place a bacteria on the screen
blist = []
for i in range(1):
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    blist.append(Bacteria((r,g,b)))
    
def mainloop():
    global score
    f.moverandomly()
    for b in blist:
        b.moveRandomly()
        b.moveTowardsTarget(f.xcor(), f.ycor())
        if b.isCloseTo(f.xcor(), f.ycor()):
            b.getLarger()
            f.goto(random.randint(-250,250), random.randint(-250,250))
            score += 1
            print (score)
    screen.update()    # Needed when the tracer is set to zero
    screen.ontimer(mainloop, 10)
    
mainloop()
