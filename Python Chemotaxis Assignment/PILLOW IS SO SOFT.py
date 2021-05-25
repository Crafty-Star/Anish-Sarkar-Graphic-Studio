from PIL import Image

try:
    original = Image.open("pizza.gif")

    width, height = original.size  
    newsize = (20,300)
    im2 = original.resize(newsize)
    im2.show()
except:
    print("Unable to load image")
