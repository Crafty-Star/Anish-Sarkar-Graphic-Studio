from tkinter import *
import random
import math
from math import *

def convertRGBToHex(r,g,b):
    return "#{0:02x}{1:02x}{2:02x}".format(r,g,b)

root = Tk()
c = Canvas(root, width = 900, height = 900)
c.pack()
currenx = int(255/2)
currenx = 0
curreny = int(255/2)
curreny = 0
currenz = int(255/2)
currenz = 0
startx = 0
starty = 0
endx = 300
endy = 0
for i in range(300):
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    currenx += random.randint(-2, 2)*60
    currenx %= 255
    curreny += random.randint(-2, 2)*60
    curreny %= 255
    currenz += random.randint(-2, 2)*60
    currenz %= 255
    startx = endx
    starty = endy
    if i%4 == 0:
        endx -= 300-i
        endy += (300-i)*math.tan(math.radians(i/10))
    elif int(i+1)%4 == 0:
        endy -= 300-i
        endx += (300-i)*math.cos(math.radians(i/10))
    elif int(i+2)%4 == 0:
        endx += 300 - i
        endy -= (300-i)*math.sin(math.radians(i/10))
    else:
        endy += 300-i
        endx -= (300-i)*math.cos(math.radians(i/10))
    endx %= 300
    endy %= 300
startx = 300
starty = 0
endx = 600
endy = 0
for i in range(450):
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    currenx += random.randint(-2, 2)*60
    currenx %= 255
    curreny += random.randint(-2, 2)*60
    curreny %= 255
    currenz += random.randint(-2, 2)*60
    currenz %= 255
    startx = endx
    starty = endy
    if random.randint(1, 100) <50:
        endx += 203*random.randint(1, int(300/75))
    else:
        endx -= 203*random.randint(1, int(300/75))
    if random.randint(1, 100) <50:
        endy += 203*random.randint(1, int(300/75))
    else:
        endy -= 203*random.randint(1, int(300/75))
    endx %= 300
    endx += 300
    endy %= 300
startx = 600
starty = 0
endx = 900
endy = 0
current = int(255/2)
for i in range(300):
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    currenx += random.randint(-2, 2)*60
    currenx %= 255
    curreny += random.randint(-2, 2)*60
    curreny %= 255
    currenz += random.randint(-2, 2)*60
    currenz %= 255
    startx = endx
    starty = endy
    if i%4 == 0:
        endx -= 300-2*i*math.tan(radians(i/10))
    elif int(i+1)%4 == 0:
        endy -= 300-2*i*math.tan(radians(i/10))
    elif int(i+2)%4 == 0:
        endx += 900 - 2*i*math.tan(radians(i/10))
    else:
        endy += 300-2*i*math.tan(radians(i/10))
    endx %= 300
    endy %= 300
    endx += 600
startx = 0
starty = 300
endx = 300
endy = 300
current = int(255/2)
for i in range(300):
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    currenx += random.randint(-2, 2)*60
    currenx %= 255
    curreny += random.randint(-2, 2)*60
    curreny %= 255
    currenz += random.randint(-2, 2)*60
    currenz %= 255
    startx = endx
    starty = endy
    if i%4 == 0:
        endx -= 300-i
        endy -= (300-i)*math.sin(math.radians(i/10))
    elif int(i+1)%4 == 0:
        endy -= 300-i
        endx += (300-i)*math.cos(math.radians(i/10))
    elif int(i+2)%4 == 0:
        endx += 300 - i
        endy += (300-i)*math.sin(math.radians(i/10))
    else:
        endy += 300-i
        endx -= (300-i)*math.cos(math.radians(i/10))
    endx %= 300
    endy %= 300
    endy += 300
startx = 600
starty = 300
endx = 600
endy = 300
current = int(255/2)
for i in range(300):
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    currenx += random.randint(-2, 2)*60
    currenx %= 255
    curreny += random.randint(-2, 2)*60
    curreny %= 255
    currenz += random.randint(-2, 2)*60
    currenz %= 255
    startx = endx
    starty = endy
    if i%4 == 0:
        endx -= 300-i
    elif int(i+1)%4 == 0:
        endy -= 300-i
    elif int(i+2)%4 == 0:
        endx += 300 - i
    else:
        endy += 300-i
    endx %= 300
    endy %= 300
    endx+=300
    endy+=300
startx = 600
starty = 300
endx = 900
endy = 300
current = int(255/2)
for i in range(300):
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    currenx += random.randint(-2, 2)*60
    currenx %= 255
    curreny += random.randint(-2, 2)*60
    curreny %= 255
    currenz += random.randint(-2, 2)*60
    currenz %= 255
    startx = endx
    starty = endy
    if i%4 == 0:
        endx -= 300-i
        endy -= 10*math.tan(math.radians(i/10))
    elif int(i+1)%4 == 0:
        endy -= 300-i
        endx -= 10*math.tan(math.radians(i/10))
    elif int(i+2)%4 == 0:
        endx += 300 - i
        endy += 10*math.tan(math.radians(i/10))
    else:
        endy += 300-i
        endx += 10*math.tan(math.radians(i/10))
    endx %= 300
    endy %= 300
    endx += 600
    endy += 300
startx = 0
starty = 600
endx = 300
endy = 600
current = int(255/2)
for i in range(300):
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    currenx += random.randint(-2, 2)*60
    currenx %= 255
    curreny += random.randint(-2, 2)*60
    curreny %= 255
    currenz += random.randint(-2, 2)*60
    currenz %= 255
    startx = endx
    starty = endy
    if i%4 == 0:
        endx -= 300-i
        endy -= (300-i)*math.sin(math.radians(i/10))
    elif int(i+1)%4 == 0:
        endy -= 300-i
        endx -= (300-i)*math.sin(math.radians(i/10))
    elif int(i+2)%4 == 0:
        endx += 300 - i
        endy += (300-i)*math.sin(math.radians(i/10))
    else:
        endy += 300-i
        endx += (300-i)*math.sin(math.radians(i/10))
    endx %= 300
    endy %= 300
    endy += 600
startx = 600
starty = 600
endx = 600
endy = 600
current = int(255/2)
for i in range(300):
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    currenx += random.randint(-2, 2)*60
    currenx %= 255
    curreny += random.randint(-2, 2)*60
    curreny %= 255
    currenz += random.randint(-2, 2)*60
    currenz %= 255
    startx = endx
    starty = endy
    if i%4 == 0:
        endx -= 300-2**(i % (math.log(300)/math.log(2)))
    elif int(i+1)%4 == 0:
        endy -= 300-2**(i % (math.log(300)/math.log(2)))
    elif int(i+2)%4 == 0:
        endx += 300 - 2**(i % (math.log(300)/math.log(2)))
    else:
        endy += 300-2**(i % (math.log(300)/math.log(2)))
    endx %= 300
    endy %= 300
    endy += 600
    endx += 300
startx = 600
starty = 600
endx = 900
endy = 600
current = int(255/2)
for i in range(300):
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(currenx, curreny, currenz))
    currenx += random.randint(-2, 2)*60
    currenx %= 255
    curreny += random.randint(-2, 2)*60
    curreny %= 255
    currenz += random.randint(-2, 2)*60
    currenz %= 255
    startx = endx
    starty = endy
    if i%4 == 0:
        endx -= 300-i
        endy += (300-i)*math.cos(math.radians(i/10))
    elif int(i+1)%4 == 0:
        endy -= 300-i
        endx += (300-i)*math.cos(math.radians(i/10))
    elif int(i+2)%4 == 0:
        endx += 300 - i
        endy -= (300-i)*math.cos(math.radians(i/10))
    else:
        endy += 300-i
        endx -= (300-i)*math.cos(math.radians(i/10))
    endx %= 300
    endy %= 300
    endx+= 600
    endy += 600

            
    
