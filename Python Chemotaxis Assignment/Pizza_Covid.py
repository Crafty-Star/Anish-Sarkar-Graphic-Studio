from turtle import *
import random, time, shutil, sys

# from playsound import playsound
import subprocess

from PIL import Image
t = Turtle()
ts = t.getscreen()
ts.setup(width = 1600, height = 1200)
ts.tracer(0,0)
ts.bgcolor("grey")
t.hideturtle()
##bac = Image.open("OG.gif")
shutil.copyfile("OG_Orig.gif", "OG.gif")
shutil.copyfile("pizza_Orig.gif", "pizza.gif")
ts.register_shape("pizza.gif")
ts.register_shape("OG.gif")
# ts.register_shape("M_O.gif")     I commented this out since I don't have the GIF
ts.register_shape("explode.gif")
class Bacteria(Turtle):
    def __init__(self, x=0, y=0):
        Turtle.__init__(self)
        self.shape("OG.gif")
        self.up()
        self.goto(x,y)
        self.resizemode("user")
        self.count = 0
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
##    def counter(self):
##        if self.count == 100:
##            pass
##        else:
##            return False
    def getLarger(self):
##        self.pensized+=0.5
####        currentxscale = self.shapesize()[0]
####        currentyscale = self.shapesize()[1]
####        self.shapesize(currentxscale + 0.1, currentyscale + 0.1)
##        self.pensize(self.pensized)
####        self.resizemode(auto)
        covid = Image.open("OG.gif")
        width, height = covid.size
        newxy = (int(width*1.02), int(height*1.02))
        im2 = covid.resize(newxy)
        im2.save("OG.gif")
        self.screen.register_shape("OG.gif")
        self.shape("OG.gif")
        
class Food(Turtle):
    def __init__(self, color = "black", x=200, y=200):
        Turtle.__init__(self)
        self.shape("pizza.gif")
        self.up()
        self.goto(x,y)
        self.fillcolor(color)    
    def moverandomly(self):
        newx = self.xcor() + random.randint(-10,10)
        newy = self.ycor() + random.randint(-10,10)
        self.goto(newx, newy)
    def exit(self):
        sys.exit()
    def checksize(self, width, height):
        if width < 20:
            self.shape("explode.gif")
##            self.stamp()
            # sys.exit()
            return True
        else:
            return False
    def getSmaller(self):
        pizza = Image.open("pizza.gif")
        width, height = pizza.size
        if self.checksize(width, height) == True:
            print("Game Over!")
            # playsound("Physi1.wav")
            # sys.exit()
            subprocess.Popen(["afplay", "Physi1.wav"])
        else:    
            newxy = (int(width-1.9), int(height-1.9))
            im2 = pizza.resize(newxy)
            im2.save("pizza.gif")
            self.screen.register_shape("pizza.gif")
            self.shape("pizza.gif")
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
blist = []
for i in range(1):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    blist.append(Bacteria(x,y))
def mainloop():
    global score
    f.moverandomly()
    for b in blist:
        b.moveRandomly()
        b.moveTowardsTarget(f.xcor(), f.ycor())
        if b.isCloseTo(f.xcor(), f.ycor()):
            b.getLarger()
            f.getSmaller()
            f.goto(random.randint(-250,250), random.randint(-250,250))
            score += 1
            print (score)
            if score == 100:
                b.explode()
                sys.exit()
                f.exit()
    screen.update()    # Needed when the tracer is set to zero
    screen.ontimer(mainloop, 10)
    
mainloop()
