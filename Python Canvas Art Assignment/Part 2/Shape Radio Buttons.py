from tkinter import *
import math
import random
import time
root = Tk()
c = Canvas(root, width=450, height=450)
c.pack()

def convertRGBToHex(r,g,b):
    return "#{0:02x}{1:02x}{2:02x}".format(r,g,b)


color = StringVar()
R1 = Radiobutton(root, text = "Lines", variable = color, value = "lines")
R1.pack(anchor = W)
R2 = Radiobutton(root, text = "Square", variable = color, value = "square")
R2.pack(anchor = W)
R3 = Radiobutton(root, text = "Circle", variable = color, value = "circle")
R3.pack(anchor = W)
R4 = Radiobutton(root, text = "Triangle", variable = color, value = "triangle")
R4.pack(anchor = W)
R5 = Radiobutton(root, text = "Polygon", variable = color, value = "polygons")
R5.pack(anchor = W)
def inputat():
   custom = "Shape Choice : " + str(color.get())
   label.config(text = selection)
label = Label(root)
label.pack()
root.mainloop()
