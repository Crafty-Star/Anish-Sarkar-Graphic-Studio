from tkinter import *
import random

def pixel(photo, pos, color):
    # Place pixel at pos=(x,y) on photo, with color=(r,g,b).
    r,g,b = color
    x,y = pos
    photo.put("#%02x%02x%02x" % (r,g,b), (x,y))

# These filters all operate in the same way.
#   You are creating a brand-new image, using pixels from the three
#   original ones. They should all be the same size for this to work,
#   since I am using photopeter in the loop.
def halfandhalf():
    global newphoto
    newphoto = PhotoImage()
    for x in range(0, photopeter.width()):
        for y in range(0, photopeter.height()):
            if x < photopeter.width()//2:
               pixel(newphoto, (x,y), photojacob.get(x,y))
            else:
               pixel(newphoto, (x,y), photopeter.get(x,y))
    photolabelnew['image'] = newphoto

def altcol():
    global newphoto
    newphoto = PhotoImage()
    for x in range(0, photopeter.width()):
        for y in range(0, photopeter.height()):
            if x % 2 == 0:
               pixel(newphoto, (x,y), photojacob.get(x,y))
            else:
               pixel(newphoto, (x,y), photopeter.get(x,y))
    photolabelnew['image'] = newphoto

def randpix():
    global newphoto
    newphoto = PhotoImage()
    for x in range(0, photopeter.width()):
        for y in range(0, photopeter.height()):
            if random.randint(0,1) == 0:
               pixel(newphoto, (x,y), photojacob.get(x,y))
            else:
               pixel(newphoto, (x,y), photopeter.get(x,y))
    photolabelnew['image'] = newphoto

def toptobottom():
    global newphoto
    newphoto = PhotoImage()
    for x in range(0, photopeter.width()):
        for y in range(0, photopeter.height()):
            if y < 80:
                pixel(newphoto, (x,y), photopeter.get(x,y))
            elif y < 120:
                pixel(newphoto, (x,y), photojacob.get(x,y))
            else:
                pixel(newphoto, (x,y), phototheo.get(x,y))
    photolabelnew['image'] = newphoto               
                                       
def save():
    newphoto.write("SavedImage.jpeg")

root = Tk()
root.title("Filter window")

photopeter = PhotoImage(file = "SmallPeter.gif")   
photolabelpeter = Label(root, image = photopeter)
photolabelpeter.grid(row = 0, column = 0)

photojacob = PhotoImage(file = "SmallJacob.gif")
photolabeljacob = Label(root, image = photojacob)
photolabeljacob.grid(row = 0, column = 1)

phototheo = PhotoImage(file = "SmallTheo.gif")
photolabeltheo = Label(root, image = phototheo)
photolabeltheo.grid(row = 0, column = 2)

newphoto = PhotoImage()   # It will resize itself to the size of the new image
photolabelnew = Label(root, image = newphoto)
photolabelnew.grid(row = 0, column = 3)

halfbutton = Button(root, text = "Half and half", command = halfandhalf)
halfbutton.grid(row = 2, column = 0)

altcbutton = Button(root, text = "Alternate columns", command = altcol)
altcbutton.grid(row = 3, column = 0)

randbutton = Button(root, text = "Random pixels", command = randpix)
randbutton.grid(row = 4, column = 0)

toptobottom = Button(root, text = "Top to bottom", command = toptobottom)
toptobottom.grid(row = 5, column = 0)

savebutton = Button(text = "Save image as jpeg", command = save)
savebutton.grid(row = 6, column = 0)

# Need a global variable to store the new image
# Otherwise, the image will be lost
newphoto = None



        
