from tkinter import *
import random

def convertRGBToHex(r,g,b):
    return "#{0:02x}{1:02x}{2:02x}".format(r,g,b)

root = Tk()
coord_list_x = []
coord_list_y = []
x = 1000
for x in range(1, 801):
    coord_list_x.append(int(x))
    coord_list_y.append(int(x))
c = Canvas(root, width=x, height=x)
c.pack()
startx = int(coord_list_x[random.randint(0,len(coord_list_x))])
starty =  coord_list_y[random.randint(0,len(coord_list_y))]
endx = coord_list_x[random.randint(0,len(coord_list_x))]
current = int(255/2)
endy = coord_list_y[random.randint(0,len(coord_list_y))]
for i in range(10*x):
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(current, current, current))
    c.create_line(startx, starty, endx, endy, fill = convertRGBToHex(current, current, current))
    current += random.randint(-2, 2)*60
    current %= 255
    coord_list_x.remove(startx)
    coord_list_x.remove(endx)
    coord_list_y.remove(starty)
    coord_list_y.remove(endy)
    startx = int(coord_list_x[random.randint(0,len(coord_list_x))])
    starty = coord_list_y[random.randint(0,len(coord_list_y))]
    endx = coord_list_x[random.randint(0,len(coord_list_x))]
    endy = coord_list_y[random.randint(0,len(coord_list_y))]
