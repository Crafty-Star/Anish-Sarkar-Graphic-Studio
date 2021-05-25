from tkinter import *
import math
import random
import time
root = Tk()
c = Canvas(root, width=900, height=900)
c.pack()

def convertRGBToHex(r,g,b):
    return "#{0:02x}{1:02x}{2:02x}".format(r,g,b)

currenx = int(255/2)
currenx = 0
curreny = int(255/2)
curreny = 0
currenz = int(255/2)
currenz = 0

ptlist = []
angle = 0
dangle = math.pi/1
for i in range(36):
    x = 450 + 600 * math.cos(angle)
    y = 450 + 600 * math.sin(angle)
    ptlist.append((x,y))
    angle += dangle
starti = 0
finishi = 10
for i in range(36):
    c.create_line(450, 450, ptlist[finishi][0], ptlist[finishi][1], fill = convertRGBToHex(currenx, curreny, currenz))
    currenx += random.randint(-2, 2)*60
    currenx %= 255
    curreny += random.randint(-2, 2)*60
    curreny %= 255
    currenz += random.randint(-2, 2)*60
    currenz %= 255
    starti = (starti + 1) % 36
    finishi = (finishi + 1) % 36
