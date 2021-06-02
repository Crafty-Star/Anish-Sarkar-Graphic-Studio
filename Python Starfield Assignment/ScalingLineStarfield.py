from tkinter import *
import math, time, random
def convertRGBToHex(r,g,b):
    return "#{0:02x}{1:02x}{2:02x}".format(r,g,b) 
# Define the behavior of a line segment  
class Line:
    def __init__(self, canvas, x, y, dx, dy, color = "yellow"):
        self.canvas = canvas
        # The center of the line, so you can scale it later about that point
        self.x = x
        self.y = y
        # How much it moves.  Used to draw the initial line as well
        self.dx = dx
        self.dy = dy
        # This draws the line in the direction that it is moving
        self.line = self.canvas.create_line(x-dx/2, y-dy/2, x+dx/2, y+dy/2, fill = color, width = random.randint(1,4))

    def move(self):
        # Move the line the correct amount
        self.x += self.dx
        self.y += self.dy
        self.canvas.move(self.line, self.dx, self.dy)
        # Make the line longer as it moves towards the edges of the screen
        self.canvas.scale(self.line, self.x, self.y, 1.1, 1.1)
        

mousex = 450
mousey = 450
root = Tk()
c = Canvas(root, width = 900, height = 900, bg = "black")
c.pack()

planets = []

def mainloop():
    global planets
    angle = 0
    while angle < 6.28:
        scale = random.uniform(20,30)
        dx = math.cos(angle) * scale
        dy = math.sin(angle) * scale
        angle += 0.03
        if random.randint(1,2) == 1:
            color = "white"
            p = Line(c, mousex + dx, mousey + dy, dx, dy, color)
            planets.append(p)
    for p in planets:
        p.move()
        if p.x > 800 or p.x < 100 or p.y >800 or p.y <100:
            c.itemconfig(p.line, fill = convertRGBToHex(137,207,240))
        elif p.x > 700 or p.x < 200 or p.y >700 or p.y <200:
            c.itemconfig(p.line, fill = convertRGBToHex(15,82,186))
        elif p.x > 600 or p.x < 300 or p.y >600 or p.y <300:
            c.itemconfig(p.line, fill = convertRGBToHex(137,207,240))
        elif p.x > 500 or p.x < 400 or p.y >500 or p.y <400:
            c.itemconfig(p.line, fill = convertRGBToHex(176,223,229))
            
        if p.x > 900 or p.y > 900 or p.x < 0 or p.y < 0:
            c.delete(p.line)
            planets.remove(p)      
                   
    root.after(1, mainloop)
    
mainloop()
