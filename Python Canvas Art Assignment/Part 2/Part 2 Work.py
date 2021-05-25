from tkinter import *
##import math
import random
##import time
root = Tk()
c = Canvas(root, width=750, height=750)
c.pack()

def convertRGBToHex(r,g,b):
    return "#{0:02x}{1:02x}{2:02x}".format(r,g,b)

def line_generator(colo, num, ran):
    for x in range(0,int(num)):
        startx = random.randint(0,900)
        starty = random.randint(0,900)
        endx = random.randint(startx-ran,startx+ran)%750
        endy = random.randint(starty-ran,starty+ran)%750
        c.create_line(startx, starty, endx, endy, fill = colo.get())
def inputat():
   line_generator(color,e1.get() ,w.get())
color = StringVar()
R1 = Radiobutton(root, text = "Red", variable = color, value = "red")
R1.pack(anchor = W)
R2 = Radiobutton(root, text = "Blue", variable = color, value = "blue")
R2.pack(anchor = W)
R3 = Radiobutton(root, text = "Green", variable = color, value = "green")
R3.pack(anchor = W)
R4 = Radiobutton(root, text = "Black", variable = color, value = "black")
R4.pack(anchor = W)
R5 = Radiobutton(root, text = "White", variable = color, value = "white")
R5.pack(anchor = W)
R1.select()
l1 = Label(root, text="Number of lines")
l1.pack()
e1 = Entry(root)
e1.pack()
l2 = Label(root,text = "Size of lines")
l2.pack()
w = Scale(root, from_=1, to=350, orient=HORIZONTAL)
w.pack()
frame = Frame(root, relief=RAISED, borderwidth=1)
frame.pack(fill=BOTH, expand=True)
b1 = Button(root, text = "Enter", command = inputat)
b1.pack(side = RIGHT, padx = 5, pady = 5)
# FROM MR. GREGG--I'm going to try to fix this for you.  The idea is
#   tricky--the command has to be a function name, not a function call.
#   The "lambda" is a clever way to make this work.
# closeButton = Button(root, text="Clean", command = c.delete("all"))
# closeButton = Button(root, text="Clean", command = lambda: c.delete("all"))

def deleteall():
    c.delete("all")
closeButton = Button(root, text="Clean", command = deleteall)
closeButton.pack(side=RIGHT, padx=5, pady=5)
root.mainloop()
