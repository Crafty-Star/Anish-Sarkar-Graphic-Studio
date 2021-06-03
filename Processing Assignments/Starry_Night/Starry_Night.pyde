# All circles will be drawn at (0,0).
# The coordinate system gets moved!

earthangle = 0  # The amount we will rotate each time
marsangle = 0
moonangle = 0

def setup():
    size(1200, 1000)
    background(0,0,0)
    
def draw():
    global earthangle, moonangle, marsangle
    background(0,0,0)
    translate(width/2, height/2)
    
    for x in range(0,100):
        fill(255,255,255)
        circle(random(-600,600),random(-600,600),10)
    
    fill(255,255,0)
    circle(0,0,200)               # Draw the sun at (0,0)
    
    rotate(radians(earthangle))   # Earthangle itself is in degrees
    translate(200, 0)             # The earth is 200 pixels from the sun
    fill(0,0,255)
    circle(0,0,50)                
    earthangle += 1 
    
    rotate(radians(moonangle))
    translate(50, 0)              # The moon is 50 pixels from the earth
    fill(255,255,255)
    circle(0,0, 20)
    moonangle += 2
    
    resetMatrix()                 # There is a better way to do this, but start over for now
    translate(width/2, height/2)  # Move (0,0) to the center of the screen again
    rotate(radians(marsangle))
    translate(400, 0)             # Mars is 400 pixels from the sun
    fill(255,0,0)
    circle(0,0,55)
    marsangle += 0.5
    
    # The origin moves back to the upper-left corner at the end of the draw loop
    
    
