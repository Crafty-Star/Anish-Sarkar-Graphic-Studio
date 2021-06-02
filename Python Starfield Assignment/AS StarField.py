from tkinter import *
import math, time, random

def convertRGBToHex(r,g,b):
    return "#{0:02x}{1:02x}{2:02x}".format(r,g,b) 
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
        self.line = self.canvas.create_line(x-dx/2, y-dy/2, x+dx/2, y+dy/2, fill = color, width = random.randint(1,2))

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
root.title("Move the mouse around the screen!")
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
        # FROM MR. GREGG--I'm adding these lines of code as a color change example
        #   Hopefully you can adjust this to your liking
        if p.x < 500 or p.x > 400 or p.y < 500 or p.y > 400:
             c.itemconfig(p.line, fill = convertRGBToHex(59, 161, 194))
        if p.x < 400 or p.x > 500 or p.y < 400 or p.y > 500:
             c.itemconfig(p.line, fill = "light blue")
        if p.x < 300 or p.x > 600 or p.y < 300 or p.y > 600:
             c.itemconfig(p.line, fill = convertRGBToHex(53, 77, 85))
        if p.x < 200 or p.x > 700 or p.y < 200 or p.y > 700:
             c.itemconfig(p.line, fill = convertRGBToHex(60, 81, 87))
        if p.x < 100 or p.x > 800 or p.y < 100 or p.y > 800:
             c.itemconfig(p.line, fill = convertRGBToHex(68, 85, 90))            
        if p.x > 900 or p.y > 900 or p.x < 0 or p.y < 0:
            c.delete(p.line)
            planets.remove(p)      
                   
    root.after(1, mainloop)
    
mainloop()






    

        
