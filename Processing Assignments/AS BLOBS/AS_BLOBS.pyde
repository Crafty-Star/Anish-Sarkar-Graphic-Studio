thetime = 0     # Global variable, which must be defined here

def makeNoise(thetime):
    noiseScale = 0.001    # Again, smaller values will produce larger cloud clumps
    for y in range(height):
        for x in range(width):
            noiseVal = noise((x*noiseScale)/2, (y*noiseScale)/2, thetime)
            if noiseVal < 0.3:
                thecolor = color(random(50,200),0,0)
            elif noiseVal < 0.6:
                thecolor = color(0,random(60,200),0)
            else:
                thecolor = color(0,0,random(50,200))
            # thecolor = color(255*noiseVal, 0, 255*(1-noiseVal))
            set(x, y, thecolor)

def setup():
    size(600, 400)

def draw():
    global thetime
    makeNoise(thetime)
    thetime += 0.05
