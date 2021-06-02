earthAngle = 0
moonAngle = 0

def setup():
    size(700,700)

def draw():
    # The origin returns to the upper-left corner at the beginning of the loop
    global earthAngle, moonAngle
    # Wipe out everything drawn the last time
    background(0,0,0)
    #  Draw in yellow
    fill(255,255,0)
    # Move origin to the center of the screen
    translate(width/2, height/2)
    circle(0,0,100)  # The sun.  Centered at (0,0), with diameter 100 pixels
             
    earthAngle += 0.05
    # Rotate and translate to where we want to draw the earth
    rotate(earthAngle)
    # The earth will be 200 units from the sun
    translate(200,0)
    # Draw in blue
    fill(0,0,255)
    circle(0,0,30)    # The earth
    
    moonAngle += 0.10
    # Rotate and translate to where we want to draw the moon
    rotate(moonAngle)
    # The moon will be 50 units from the earth
    translate(50,0)
    # Draw in red
    fill(255,0,0)
    circle(0,0,10)    # The moon
    
    # At the end of draw the origin moves back to the upper-left corner, as usual
