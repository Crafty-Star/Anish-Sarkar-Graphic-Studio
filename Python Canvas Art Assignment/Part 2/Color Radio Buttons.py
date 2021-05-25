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
R1 = Radiobutton(root,activebackground = "red",activeforeground = convertRGBToHex(166,16,30), text = "Red", variable = color, value = "red")
R1.pack(anchor = W)
R2 = Radiobutton(root,activebackground = "blue",activeforeground = convertRGBToHex(0, 0, 128), text = "Blue", variable = color, value = "blue")
R2.pack(anchor = W)
R3 = Radiobutton(root,activebackground = "green",activeforeground = convertRGBToHex(80, 200, 120), text = "Green", variable = color, value = "green")
R3.pack(anchor = W)
R4 = Radiobutton(root,activebackground = "black",activeforeground = convertRGBToHex(54, 69, 79), text = "Black", variable = color, value = "black")
R4.pack(anchor = W)
R5 = Radiobutton(root,activebackground = "white",activeforeground = convertRGBToHex(248, 248, 255), text = "White", variable = color, value = "white")
R5.pack(anchor = W)
def inputat():
   custom = "Color Choice : " + str(color.get())
   label.config(text = selection)
label = Label(root)
label.pack()
root.mainloop()
