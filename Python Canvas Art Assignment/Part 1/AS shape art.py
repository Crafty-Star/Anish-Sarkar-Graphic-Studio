from tkinter import *
import math
root = Tk()
c = Canvas(root, width=500, height=500)
c.pack()

ptlist = []
angle = 0
dangle = math.pi/18 
for i in range(36):
    x = 250 + 150 * math.cos(angle)
    y = 250 + 150 * math.sin(angle)
    ptlist.append((x,y))
    angle += dangle
starti = 0
finishi = 10 
for i in range(36):
    # FROM MR. GREGG--Uncommenting some of these to take a look!
    # c.create_rectangle(ptlist[starti][0], ptlist[starti][1], ptlist[finishi][0], ptlist[finishi][1])
    # c.create_arc(ptlist[starti][0], ptlist[starti][1], ptlist[finishi][0], ptlist[finishi][1])
    c.create_oval(ptlist[starti][0], ptlist[starti][1], ptlist[finishi][0], ptlist[finishi][1])
    starti = (starti + 1) % 36
    finishi = (finishi + 1) % 36
