from tkinter import *
from turtle import *
import random

class TurtlePlanet(Turtle):
    def __init__(self, x, y, angle, velocity, color):
        super().__init__()
        
        self.shape("circle")
        self.color(color)
        self.hideturtle()
        self.up()
        self.goto(x,y)
        self.showturtle()
        self.setheading(angle)
        self.velocity = velocity

    def move(self):
        self.forward(self.velocity)

# Get the screen that all the turtles will draw on
screen = Screen()
screen.setup(width = 800, height = 800)
screen.bgcolor("black")
# For fastest possible speed, with manual updates
screen.tracer(0)

# All objects currently on the screen should be in this list
planets = []

# Populate the list with a bunch of planets.
#  In this program, there will be no additional planets made.
angle = 0
while angle < 360:   # Turtle graphics works in degrees, not radians
    speed = random.randint(20, 30)
    if random.randint(1,2) == 1:
        tp = TurtlePlanet(0, 0, angle, speed, "red")
        planets.append(tp)
    angle += 10

# Infinite loop which continually moves all the planets in the list
while True:
    # Continually add more planets to the list!
    angle = 0
    while angle < 360:   # Turtle graphics works in degrees, not radians
        speed = random.randint(20, 30)
        if random.randint(1,10) == 1:
            tp = TurtlePlanet(0, 0, angle, speed, "red")
            planets.append(tp)
        angle += 10

    # Move all the planets
    for p in planets:
        p.move()
        # So it doesn't lag when they go offscreen
        if p.xcor() > 425 or p.ycor() > 425 or p.xcor() < -425 or p.ycor() < -425:
            p.clear()
            
    screen.update()
       



    




        
        
        
        
