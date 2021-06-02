from tkinter import *
import math, time, random

# Define the behavior of a planet.  
class Planet:
    def __init__(self, canvas, x, y, dx, dy, r = 1, color = "red"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        # The planets are circles now, but you can change that
        self.ball = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill = color, width = 0)

    def move(self):
        # I have added code to move to make the ball a little larger each
        #  time it moves.  This gives a more realistic look.  
        self.x += self.dx
        self.y += self.dy
        self.canvas.move(self.ball, self.dx, self.dy)
        # Expands the ball about its center, by a factor of 1.1 in each direction
        self.canvas.scale(self.ball, self.x, self.y, 1.1, 1.1)
        
# Variables to keep track of the current mouse coordinates
mousex = 400
mousey = 400

# Method called when the user moves the mouse on the screen.
# It just adjusts mousex and mousey appropriately, so that new
#    planets will start from that position
def startlocation(event):
    global mousex
    global mousey
    mousex = event.x
    mousey = event.y

# The planets will draw on a Tkinter canvas
root = Tk()
root.title("Move the mouse around the screen!")
c = Canvas(root, width = 800, height = 800)
c.pack()
# Bind mouse motion on the canvas to a function
c.bind('<Motion>', startlocation)
# List of all the planets
planets = []

def mainloop():
    # Note that this program continually creates planets, which is
    #  why the while loop is inside the main loop here.
    
    # Make another round of planets, at the current mouse position
    # But don't start them right at the click location--put them a
    #  couple of dx and dy units away to start with.
    global planets
    angle = 0
    while angle < 6.28:
        # Adjusts how fast they move
        scale = random.uniform(20, 30)
        dx = math.cos(angle) * scale
        dy = math.sin(angle) * scale
        angle += 0.005
        if random.randint(1,10) == 1:
            # Make another planet, and add it to the list of all of them
            p = Planet(c, mousex + 2*dx, mousey + 2*dy, dx, dy)
            planets.append(p)
            
    #  Loop to move all the planets
    for p in planets:
        p.move()
        if p.x > 800 or p.y > 800 or p.x < 0 or p.y < 0:
            # This must be p.ball, not just p!  Doh!
            c.delete(p.ball)
            planets.remove(p)      
                   
    root.after(1, mainloop)
    
# Start up the main loop, which repeats forever
mainloop()






    

        
