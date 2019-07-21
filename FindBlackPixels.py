import numpy as np 
import cv2
import sys

# Notes
#     Make image black and white
#     Make windows 
#     Get input from mouse
#     On start begin comparing window 1 and 2 to mouse
#     Move to comparing window 2 and 3 when the distance to any point in window 2 is less than the distance to any point in window 1

############################################################ Global Variables ###############################################
white = 255
black = 0
dWinList = []



#Read in the letter to display as greyscale
letter = cv2.imread('ScriptL.jpg', 0) 


############################################################# Class Definitions #################################################
class Dwin(object):
    """__init__() functions as the class constructor"""
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
            pixC = img[y, x]
            if pixC > 5: #if a pixel is not black/near black make it true white
                img[y,x] = 255
            else: #if a pixel is black/near black make it true black
                img[y,x] = 0


def isPixUpperRight(img, y, x, wId):
    # global y
    # global x
    # global wId
    y = y-10
    x = x+10
    for xw in range(x, x+9):
        for yw in range(y-9, y):
            if xw >= 1920: break
            #img[yw, xw] = 0
            if img[yw, xw] == 0:    
                wId += 1   
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'ur'))
                return 1
    return 0


def isPixUp(img, y, x, wId):
    # global y
    # global x
    # global wId
    y = y-10
    for xw in range(x, x+9):
        for yw in range(y-9, y):
            if xw >= 1920: break
            #img[yw, xw] = 0  
            if img[yw, xw] == 0:
                wId += 1   
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'u'))
                return 1, y
    return 0

def isPixRight(img, y, x, wId):
    # global y
    # global x
    # global wId
    x = x + 10
    for xw in range(x, x+9):
        for yw in range(y-9, y+1):
            #img[yw, xw] = 0
            if img[yw, xw] == 0:    
                wId += 1   
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'r'))
                return 1    
    return 0

def isPixLeft(img, y, x, wId):
    # global y
    # global x
    # global wId
    x = x - 10
    for xw in range(x, x+9):
        for yw in range(y-9, y):
            #img[yw, xw] = 0
            if img[yw, xw] == 0:    
                wId += 1   
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'l'))
                return 1  
    return 0

def isPixUpperLeft(img, y, x, wId):
    # global y
    # global x
    # global wId
    y = y-10
    x = x-10
    for xw in range(x, x+9):
        for yw in range(y-9, y):
            if xw >= 1920: break
            #img[yw, xw] = 0
            if img[yw, xw] == 0: 
                wId += 1   
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'ul'))
                return 1,
    return 0

def colorDwin (img, class_type = "Dwin"):
    for Dwin in dWinList:
        print ("Window#= %s, xmin=%s, xmax= %s, ymin= %s ymax= %s, direction=  %s"% (Dwin.idnum, Dwin.xmin, Dwin.xmax, Dwin.ymin, Dwin.ymax, Dwin.direction))
        for x in range(Dwin.xmin, Dwin.xmax):
            for y in range(Dwin.ymin, Dwin.ymax, -1):
                img[y, x] = 255



def createWindows(img):
    """Create Decision windows"""
    #change the image to black and white
    changeToBW(img)
    # find the height, width, of the image
    ys = img.shape[0]
    xs = img.shape[1]
    oneTimeFlag = 1
    wId = 1
    #iterate over entire image starting at bottom left to find most lower left pixel
    x = 0
    y = ys-1
    while x < xs:
        x += 1
        while  y > 0:
            if img[y, x] == 0:
                if oneTimeFlag:
                    oneTimeFlag = 0
                    dWinList.append(Dwin(wId, y, (y-10), x, (x+10))) #create first window at the most lower left pixel
                elif isPixUp(img, y, x, wId)[0]:
                    y = isPixUp(img, y, x, wId)[1]
                    wId += 1
                    #y = y-10
                    #wId += 1
                y -= 1
                # elif flag == 0:
                #     isPixUpperRight(img, y, x, wId)
                #     #y = y-10
                #     #x = x+10
                #     #wId += 1
                # elif flag == 0:
                #     isPixRight(img, y, x, wId)
                #     #x = x+10
                #     #wId += 1
                # elif flag == 0:
                #     isPixLeft(img, y, x, wId)
                #     #x = x-10
                #     #wId += 1
                # elif flag == 0:
                #     isPixUpperRight(img, y, x, wId)
                #     # ys = ys-10
                #     # xs = xs-10
                #     # wId += 1

    colorDwin(img, dWinList)            

#######################################################################################use while loop############################################################
# def createWindows (img):
#     """Create Decision windows"""
#     #change the image to black and white
#     changeToBW(img)
#     # find the height, width, of the image
#     ys = img.shape[0]
#     xs = img.shape[1]
#     oneTimeFlag = 1
#     wId = 1
#     # global y
#     # global x
#     # global wId
#     #iterate over entire image starting at bottom left to find most lower left pixel
#     for x in range(0, xs):
#         for y in range(ys-1, 0, -1):
#             if img[y, x] == 0:
#                 if oneTimeFlag:
#                     oneTimeFlag = 0
#                     dWinList.append(Dwin(wId, y, (y-10), x, (x+10))) #create first window at the most lower left pixel
#                 # else:
#                 #     isPixUp(img, y, x, wId)
#                 #     isPixUpperRight(img, y, x, wId)
#                 #     isPixRight(img, y, x, wId)
#                 #     isPixLeft(img, y, x, wId)
#                 #     isPixUpperRight(img, y, x, wId)
#                 elif isPixUp(img, y, x, wId)[0]:
#                     y = isPixUp(img, y, x, wId)[1]
#                     wId += 1
#                     #y = y-10
#                     #wId += 1
#                 elif flag == 0:
#                     isPixUpperRight(img, y, x, wId)
#                     #y = y-10
#                     #x = x+10
#                     #wId += 1
#                 elif flag == 0:
#                     isPixRight(img, y, x, wId)
#                     #x = x+10
#                     #wId += 1
#                 elif flag == 0:
#                     isPixLeft(img, y, x, wId)
#                     #x = x-10
#                     #wId += 1
#                 elif flag == 0:
#                     isPixUpperRight(img, y, x, wId)
#                     # ys = ys-10
#                     # xs = xs-10
#                     # wId += 1

#     colorDwin(img, dWinList)            


#                 # for xw in range(x, x+10): #window 1
#                 #     for yw in range(y-10, y+1):

#                 #        img[yw, xw] = 0
#                 #         # if img[yw, xw] == 0:
#                 #         #     #print ("Pixel # x= %s, y= %s, window # %s" % (x, y, w))
#                 #         #     img[yw, xw] == 255
#                 #         #     d = 1 
#                 #         # else:
#                 #         #     d = 0
               
#                 # return         
#             #make other windows    
#             # x + 10
#             # y + 10 
#             # w += 1  
createWindows(letter)

cv2.imshow('title', letter)
cv2.waitKey(0)
cv2.destroyAllWindows()

