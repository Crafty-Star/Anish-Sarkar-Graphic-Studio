from tkinter import *
import tkinter.messagebox
from PIL import *
from tkinter.colorchooser import askcolor              
from tkinter.filedialog import *
import shutil

def pixel(image, pos, color):
    # Place pixel at pos=(x,y) on image, with color=(r,g,b).
    r,g,b = color
    x,y = pos
    image.put("#%02x%02x%02x" % (r,g,b), (x,y))

def negative():
    for x in range(photo.width()):
        for y in range(photo.height()):
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

def halfofthem():
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
    photo = newphoto  
            
def blur():
    global photo
    newphoto = PhotoImage()
    for x in range(photo.width()):
        for y in range(photo.height()):
            oldcolor = photo.get(x,y)
            oldr = oldcolor[0]
            oldg = oldcolor[1]
            oldb = oldcolor[2]
            if x == 0 or y == 0 or x == photo.width()-1 or y == photo.height()-1:
                pixel(newphoto, (x,y), (oldr, oldg, oldb))
            else:
                nbrs = [[0,1],[1,0],[0,-1],[-1,0], [0,0]]
                rgbsum = [0,0,0]
                for change in nbrs:
                    nx = x + change[0]
                    ny = y + change[1]
                    thecolor = photo.get(nx, ny)
                    rgbsum[0] += thecolor[0]
                    rgbsum[1] += thecolor[1]
                    rgbsum[2] += thecolor[2]
                pixel(newphoto,(x,y), (rgbsum[0]//5, rgbsum[1]//5, rgbsum[2]//5))
    photolabel['image'] = newphoto
    photo = newphoto

def fadetoblack():
    for i in range(10): 
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
        root.update()

def exaa():
    for x in range(photo.width()):
        for y in range(photo.height()):
            oldcolor = photo.get(x,y)
            oldr = oldcolor[0]
            oldg = oldcolor[1]
            oldb = oldcolor[2]
            newr = oldb
            newg = oldr
            newb = oldg
            pixel(photo,(x,y), (newr, newg, newb))
    root.update()
def exbb():
    for x in range(photo.width()):
        for y in range(photo.height()):
            oldcolor = photo.get(x,y)
            oldr = oldcolor[0]
            oldg = oldcolor[1]
            oldb = oldcolor[2]
            newr = oldr/2
            newg = oldg/2
            newb = oldb/2
            pixel(photo,(x,y), (newr, newg, newb))
    root.update()
##def excc():
##    for x in range(photo.width()):
##        for y in range(photo.height()):
##            oldcolor = photo.get(x,y)
##            oldr = oldcolor[0]
##            oldg = oldcolor[1]
##            oldb = oldcolor[2]
##            newr = oldb
##            newg = oldr
##            newb = oldg
##            pixel(photo,(x,y), (newr, newg, newb))
##    root.update()
def save():
    global pic
    toSave = filedialog.asksaveasfile(mode='w',defaultextension='.jpg')
    pic.save(toSave)
def openNewerWindow():
    photoEdit = Toplevel(root)
    photoEdit.title("Photo Editor")
    photoEdit.geometry("500x250")
    negativeize = Button(photoEdit,text = "negative", activebackground = "black", bd = 4, bg = "white", command = negative).pack()
    hor = Button(photoEdit,text = "flip horizontal", bd = 4, command = fliphorizontal).pack()
    black = Button(photoEdit,text = "fade to black", bd = 4, command = fadetoblack).pack()
    blu = Button(photoEdit, text = "blur", bd = 4, command = blur).pack()
    poster = Button(photoEdit, text = "posterize", bd = 4, command = posterize).pack()
    exa = Button(photoEdit, text = "exa", bd = 4, command = exaa).pack()
    exb = Button(photoEdit, text = "exb", bd = 4, command = exbb).pack()
##    exc = Button(photoEdit, text = "exc", bd = 4, command = excc).pack()
    end = Button(photoEdit, text = "EXIT",activebackground = "crimson",bd = 4,bg = "salmon",command =photoEdit.destroy).pack()

def openNewWindow():
    photoEditor = Toplevel(root)
    photoEditor.title("Photo Editor")
    photoEditor.geometry("500x500")
    photolabel = Label(photoEditor, image = photo).pack()
    saveing = Button(photoEditor,text = "SAVE",activebackground = "light green", bd = 5, bg = "forest green",command = save).pack()
    end = Button(photoEditor, text = "EXIT",activebackground = "crimson",bd = 4,bg = "salmon",command =photoEditor.destroy).pack()
    openNewerWindow()

def callback():
    #gets file path
    photoname = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("gif files","*.gif"),("png files","*.png")))
    #gets file name
    filenamelist = list(photoname.split("/"))
    filename = filenamelist[-1]
    #copies file
    try:
        shutil.copyfile(photoname, filename)
        load(True,filename)
    except:
        load(True,filename)
def load(photoobject = False, name = ""):
    #try:
    global photo
    if photoobject == False:
        picname = imagetext.get()
    else:
        picname = name
    global listpicname
    listpicname = list(picname.split("."))
    if(listpicname[1]!= 'gif') :
        img = Image.open(picname)
        img.save(listpicname[0]+".gif")
        picname = listpicname[0]+".gif"
    photo = PhotoImage(file = picname)
    root.wm_state('iconic')
    root.iconify()
    openNewWindow()
    #except:
        #tkinter.messagebox.showerror("ERROR","There either exists no such image or it is misspelled.")



   
root = Tk()
root.title("Images")

Button(text='Select file', command=callback).pack(fill=X)

imagetext = Entry(root)
imagetext.pack()

loadbutton = Button(root, text = "Specify image", command = load)
loadbutton.pack()

end = Button(root, text = "EXIT",activebackground = "crimson",bd = 4,bg = "salmon",command =root.destroy).pack()
root.mainloop()

newphoto = None
