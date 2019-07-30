# from tkinter import Canvas
# from PIL import ImageTK
import sys
import numpy as np 
import cv2
from pynput.mouse import Controller


# Notes
#     Make image black and white
#     Make windows 
#     Get input from mouse
#     On start begin comparing window 1 and 2 to mouse
#     Move to comparing window 2 and 3 when the distance to any point in window 2 is less than the distance to any point in window 1

############################################################ Global Variables ###############################################
white = [255,255,255]
black = [0,0,0]
nearBlack = [5,5,5]
dWinList = []
#Read in the letter to display as greyscale
letter = cv2.imread('ScriptL.jpg', 1) 
DBOffset = 3
DSOffset = 2

############################################################# Class Definitions #################################################
class Dwin(object):
    def __init__(self, idnum=0, ymin=0, ymax=0, xmin=0, xmax=0, direction='aa'):
        self.idnum = idnum
        self.ymin = ymin
        self.ymax = ymax
        self.xmin = xmin
        self.xmax = xmax
        self.direction = direction

############################################################# Functions ###########################################
def changeToBW (img):
    """Change image to Black and White"""
    # find the height, width, of the image
    ys = img.shape[0]
    xs = img.shape[1]
    #iterate over entire image starting at top left 
    for x in range(0, xs):
        for y in range(0, ys):
            if np.allclose((img[y,x]), nearBlack, 5, 5): #if a pixel is not black/near black make it true white
                img[y,x] = black
            else: #if a pixel is black/near black make it true black
                img[y,x] = white

def colorDwin (img, class_type="Dwin"):
    for Dwin in dWinList:
        print ("Window#= %s, xmin=%s, xmax= %s, ymin= %s ymax= %s, direction=  %s"% (Dwin.idnum, Dwin.xmin, Dwin.xmax, Dwin.ymin, Dwin.ymax, Dwin.direction))
        for x in range(Dwin.xmin, Dwin.xmax):
            for y in range(Dwin.ymin, Dwin.ymax, -1):
                if img[y, x] == black:
                    print ("Black")
                    img[y, x] = white
                # else:
                #     img[y, x] = 0

# def loadImage(img):
#     filename = ImageTk.PhotoImage(img)
#     ys = img.shape[0]
#     xs = img.shape[1]
#     canvas = Canvas(gui,height=ys,width=xs)
#     canvas.image = filename  # <--- keep reference of your image
#     canvas.create_image(0,0,anchor='nw',image=filename)
#     canvas.pack()

# def draw (img):
#     # Global variables
#     canvas = np.ones([1080,1920,3],'uint8')*255
#     test = cv2.imread("scriptL.jpg", cv2.IMREAD_COLOR)
#     image = cv2.add(test, canvas)
#     radius = 3
#     color = (0,255,0)
#     pressed = False
#     # click callback
#     def click(event, x, y, flags, param):
#         global canvas, pressed
#         if event == cv2.EVENT_LBUTTONDOWN: #pressed is only = to true when left button is pressed down
#             pressed = True
#             cv2.circle(canvas,(x,y),radius,color,-1)
#         if event == cv2.EVENT_MOUSEMOVE: #draws circle when mouse is moved
#             cv2.circle(canvas,(x,y),radius,color,-1)
#         elif event == cv2.EVENT_LBUTTONUP:
#             pressed = False
#     # window initialization and callback assignment
#     cv2.namedWindow("canvas")
#     cv2.setMouseCallback("canvas", click)
#     # Forever draw loop
#     while True:
#         cv2.imshow("image", image)
#         # key capture every 1ms
#         ch = cv2.waitKey(1)
#         if ch & 0xFF == ord('q'):
#             break
#         elif ch & 0xFF == ord('b'):
#             color = (255,0,0)
#         elif ch & 0xFF == ord('g'):
#             color = (0,255,0)
#     cv2.destroyAllWindows()

def draw (img):
    # mouse callback function
    def draw_circle(event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img,(x,y),3,(255,0,0),-1)
    # Create a black image, a window and bind the function to window
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)
    mouse = Controller()
    
    while(1):
        cv2.imshow('image',img)
        if cv2.waitKey(20) & 0xFF == 27:
            print('The current pointer position is {0}'.format(mouse.position))
            break
    cv2.destroyAllWindows()

dWinList.append(Dwin(0, 613, 583, 831, 843,))
dWinList.append(Dwin(1, 583, 574, 845, 855,))
dWinList.append(Dwin(2, 574, 544, 849, 864,))
dWinList.append(Dwin(3, 544, 514, 859, 874,))
dWinList.append(Dwin(4, 514, 484, 869, 890,))
dWinList.append(Dwin(5, 484, 454, 879, 915,))
dWinList.append(Dwin(6, 454, 424, 889, 920,))
dWinList.append(Dwin(7, 424, 394, 899, 930,))
dWinList.append(Dwin(8, 394, 364, 909, 930,))
dWinList.append(Dwin(9, 364, 334, 909, 930,))
dWinList.append(Dwin(10, 334, 304, 909, 930,))
dWinList.append(Dwin(11, 304, 289, 909, 930,))
dWinList.append(Dwin(12, 304, 289, 889, 909,))
dWinList.append(Dwin(13, 334, 304, 875, 895,))
dWinList.append(Dwin(14, 364, 334, 860, 885,))
dWinList.append(Dwin(15, 394, 364, 850, 875,))
dWinList.append(Dwin(16, 424, 394, 850, 870,))
dWinList.append(Dwin(17, 454, 424, 850, 870,))
dWinList.append(Dwin(18, 484, 454, 850, 870,))
dWinList.append(Dwin(19, 504, 484, 845, 865,))
dWinList.append(Dwin(20, 524, 504, 840, 860,))
dWinList.append(Dwin(21, 544, 524, 840, 855,))
dWinList.append(Dwin(22, 564, 544, 840, 850,))
dWinList.append(Dwin(23, 567, 564, 843, 845,))
dWinList.append(Dwin(25, 593, 567, 842, 845,))
dWinList.append(Dwin(26, 623, 593, 841, 849,))
dWinList.append(Dwin(27, 653, 623, 841, 849,))
dWinList.append(Dwin(28, 683, 653, 841, 849,))
dWinList.append(Dwin(29, 701, 683, 841, 850,))
dWinList.append(Dwin(30, 708, 701, 848, 855,))
dWinList.append(Dwin(31, 714, 708, 852, 859,))
dWinList.append(Dwin(32, 716, 712, 859, 872,))
dWinList.append(Dwin(33, 712, 702, 872, 885,))
dWinList.append(Dwin(34, 702, 690, 885, 900,))
dWinList.append(Dwin(35, 690, 665, 900, 920,))
dWinList.append(Dwin(36, 665, 635, 910, 935,))
dWinList.append(Dwin(36, 635, 605, 920, 945,))


changeToBW(letter)
#colorDwin(letter, dWinList)
# cv2.imshow('title', letter)
draw(letter)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
