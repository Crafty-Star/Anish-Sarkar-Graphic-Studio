from tkinter import *

def pixel(image, pos, color):
    # Place pixel at pos=(x,y) on image, with color=(r,g,b).
    r,g,b = color
    x,y = pos
    image.put("#%02x%02x%02x" % (r,g,b), (x,y))

# These first three filters just change the pixels in photo directly.
#  They do not require making a new image.
def negative():
    for x in range(photo.width()):
        for y in range(photo.height()):
            # oldcolor is a tuple containing the RGB values at (x,y)
            oldcolor = photo.get(x,y)
            newr = 255 - oldcolor[0]
            newg = 255 - oldcolor[1]
            newb = 255 - oldcolor[2]
            pixel(photo,(x,y), (newr, newg, newb))

def fliphorizontal():
    for y in range(photo.height()):
        for x in range(photo.width()//2):
            leftcolor = photo.get(x,y)
            rightcolor = photo.get(photo.width() - x - 1, y)
            pixel(photo, (x,y), rightcolor)
            pixel(photo, (photo.width() - x - 1, y), leftcolor)

def posterize():
    for x in range(photo.width()):
        for y in range(photo.height()):
            oldcolor = photo.get(x,y)
            if oldcolor[0] > 128:
                newr = 255
            else:
                newr = 0
            if oldcolor[1] > 128:
                newg = 255
            else:
                newg = 0
            if oldcolor[2] > 128:
                newb = 255
            else:
                newb = 0
            pixel(photo,(x,y), (newr, newg, newb))

# The next two filters make a brand-new image, and then replace the original image
#   with the new one at the very end. 
def halfofthem():
    # Need to explicitly declare photo as global, since it's getting changed
    #   by the function to a new value
    global photo
    newphoto = PhotoImage()
    x = 0
    y = 0
    for i in range(0, photo.width(), 2):
        for j in range(0, photo.height(), 2):
           pixel(newphoto, (x,y), photo.get(i,j))
           y += 1
        x += 1
        y = 0
    photolabel['image'] = newphoto
    photo = newphoto  # Needed if you want to do another filter after this one
            
def blur():
    global photo
    newphoto = PhotoImage()
    for x in range(photo.width()):
        for y in range(photo.height()):
            oldcolor = photo.get(x,y)
            oldr = oldcolor[0]
            oldg = oldcolor[1]
            oldb = oldcolor[2]
            # Don't change pixels on the edge
            if x == 0 or y == 0 or x == photo.width()-1 or y == photo.height()-1:
                pixel(newphoto, (x,y), (oldr, oldg, oldb))
            else:
                # Which neighbors we will look at
                nbrs = [[0,1],[1,0],[0,-1],[-1,0], [0,0]]
                # Sums of all the rgb values of those neighbors
                rgbsum = [0,0,0]
                for change in nbrs:
                    nx = x + change[0]
                    ny = y + change[1]
                    thecolor = photo.get(nx, ny)
                    rgbsum[0] += thecolor[0]
                    rgbsum[1] += thecolor[1]
                    rgbsum[2] += thecolor[2]
                # Create the pixel in the new photo
                pixel(newphoto,(x,y), (rgbsum[0]//5, rgbsum[1]//5, rgbsum[2]//5))
    photolabel['image'] = newphoto
    photo = newphoto

# This shows how you can write a filter that changes the image dynamically.
#  It goes through a loop and changes the image 10 times before quitting.
def fadetoblack():
    for i in range(10):    # Will be completely black in 10 iterations
        for x in range(photo.width()):
            for y in range(photo.height()):
                oldcolor = photo.get(x,y)
                newr = oldcolor[0] - 26
                if newr < 0:
                    newr = 0
                newg = oldcolor[1] - 26
                if newg < 0:
                    newg = 0
                newb = oldcolor[2] - 26
                if newb < 0:
                    newb = 0
                pixel(photo,(x,y), (newr, newg, newb))
        root.update()   # The image didn't change without this line! Not sure why...
                                                    
def load():
    global photo
    picname = imagetext.get()
    photo = PhotoImage(file = picname)
    photolabel['image'] = photo

def save():
    photo.write("SavedImage.jpeg")

root = Tk()
root.title("Filter window")

# The name of the image is photo. The idea is that you can attach it to a label,
#    and position it on the screen like any other label.
photo = PhotoImage()
photolabel = Label(root, image = photo)
photolabel.pack()

# Buttons for all of the filters.
flipbutton = Button(root, text = "Flip Horizontally", command = fliphorizontal)
flipbutton.pack()
negbutton = Button(root, text = "Negative", command = negative)
negbutton.pack()
blurbutton = Button(text = "Blur", command = blur)
blurbutton.pack()
halfbutton = Button(text = "Half the pixels", command = halfofthem)
halfbutton.pack()
fadebutton = Button(text = "Fade to black", command = fadetoblack)
fadebutton.pack()
posterbutton = Button(text = "Posterize!", command = posterize)
posterbutton.pack()

# Text box to type in a file name to use for the image.
imagetext = Entry(root)
imagetext.pack()

loadbutton = Button(root, text = "Load image", command = load)
loadbutton.pack()
savebutton = Button(text = "Save image as jpeg", command = save)
savebutton.pack()

# Need a global variable to use in the ones that create a new image
# Otherwise, the image will be lost
newphoto = None



        
