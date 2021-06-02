earthAngle = 0

def setup():
    size(700,700,P3D)   # This third parameter is needed to draw in 3D
    # noStroke()          # This gets rid of the triangulation of the spheres
    
def draw():
    global earthAngle
    background(0,0,30)
    fill(255,255,0)
    translate(width/2, height/2, 0)
    sphere(100)     # Draw the sun.  You can ONLY draw spheres at (0,0), so the translation was needed here
    
    earthAngle += 0.05
    rotateZ(radians(30))   # To tilt the orbit, if you like.  The z-axis points out towards you.
    # The y-axis points up
    rotateY(earthAngle)
    translate(200,0, 0)
    fill(0,0,255)
    sphere(30)     # Draw the earth 

        
        
        

    
        
                
