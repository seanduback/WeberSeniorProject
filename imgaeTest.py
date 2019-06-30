""" from PIL import Image, ImageDraw

im = Image.open('C:/Users/seand/Desktop/Test.png')
draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

# write to stdout
im.save(sys.stdout, "PNG")
# im.show() 
 """

from PIL import Image, ImageDraw
import sys, pyautogui, time 

im = Image.open('Test.jpg')
draw = ImageDraw.Draw(im)
#Draw a rectangle to cover "Test" text
""" for x in range(500):
    for y in range(300):
        draw.point((x,y), fill=128) """
draw.point((100,100), fill=128)
del draw
# write to stdout
im.save(sys.stdout.encoding, "PNG")
im.show()
