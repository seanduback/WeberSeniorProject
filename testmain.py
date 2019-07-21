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

def isPixUp(img, y, x, wId):
    y = y-10
    for xw in range(x, x+9):
        for yw in range(y-9, y):
            if xw >= 1920: break
            elif img[yw, xw] == 0:
                wId += 1   
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'u'))
                return 1
    return 0

def isPixUpperRight(img, y, x, wId):
    y = y-10
    x = x+10
    for xw in range(x, x+9):
        for yw in range(y-9, y):
            if xw >= 1920: break
            elif img[yw, xw] == 0:    
                wId += 1   
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'ur'))
                return 1
    return 0




def isPixRight(img, y, x, wId):
    x = x+10
    for xw in range(x, x+9):
        for yw in range(y-9, y+1):
            if img[yw, xw] == 0: 
                wId += 1   
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'r'))
                return 1
    return 0

def isPixLeft(img, y, x, wId):
    x = x - 10
    for xw in range(x, x+9):
        for yw in range(y-9, y):
            if img[yw, xw] == 0:
                wId += 1
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'l'))
                return 1, x
    return 0

def isPixUpperLeft(img, y, x, wId):
    y = y-10
    x = x-10
    for xw in range(x, x+9):
        for yw in range(y-9, y):
            if xw >= 1920: break
            elif img[yw, xw] == 0:
                wId += 1
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'ul'))
                return 1, y, x
    return 0

def isPixDown(img, y, x, wId):
    y = y+10
    for xw in range(x, x+9):
        for yw in range(y-9, y):
            if xw >= 1920: break
            elif img[yw, xw] == 0:
                wId += 1
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'd'))
                return 1, y
    return 0

def isPixDownLeft(img, y, x, wId):
    y = y+10
    x = x-10
    for xw in range(x, x+9):
        for yw in range(y-9, y):
            if xw >= 1920: break
            elif img[yw, xw] == 0:
                wId += 1
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'dl'))
                return 1, y, x
    return 0

def isPixDownRight(img, y, x, wId):
    y = y+10
    x = x+10
    for xw in range(x, x+9):
        for yw in range(y-9, y):
            if xw >= 1920: break
            elif img[yw, xw] == 0:    
                wId += 1   
                dWinList.append(Dwin(wId, y, y-10, x, x+10, 'dr'))
                return 1, y, x
    return 0

def createFirstWindow(img, y, x, wId):
    dWinList.append(Dwin(wId, y, y-10, x, x+10, 'fr')) #create first window at the most lower left pixel
    return


def colorDwin (img, class_type = "Dwin"):
    for Dwin in dWinList:
        print ("Window#= %s, xmin=%s, xmax= %s, ymin= %s ymax= %s, direction=  %s"% (Dwin.idnum, Dwin.xmin, Dwin.xmax, Dwin.ymin, Dwin.ymax, Dwin.direction))
        for x in range(Dwin.xmin, Dwin.xmax):
            for y in range(Dwin.ymin, Dwin.ymax, -1):
                img[y, x] = 0



def createWindows(img, class_type = "Dwin"):
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
    while x < xs-1:
        for Dwin in dWinList:
            for xd in range(Dwin.xmin, Dwin.xmax):
                if x >= 1920:
                    break
                elif x == xd:
                    x += 10
                else:
                    break
            break
        y = ys-1
        while  y > 0:
            for Dwin in dWinList:
                for yd in range(Dwin.ymin, Dwin.ymax, -1):
                    if y == yd:
                        y -= 10
                    else:
                        break
                break
            if img[y, x] == 0:
                if oneTimeFlag:
                    oneTimeFlag = 0
                    createFirstWindow(img, y, x, wId)
                elif isPixUp(img, y, x, wId):
                    y = y-10
                    wId += 1
                elif isPixRight(img, y, x, wId):
                    x = x+10
                    wId += 1
                elif isPixUpperRight(img, y, x, wId):
                    y = y-10
                    x = x+10
                    wId += 1
                # elif isPixDown(img, y, x, wId):
                #     y = isPixUp(img, y, x, wId)[1]
                #     wId += 1
                # elif isPixLeft(img, y, x, wId):
                #     x = isPixLeft(img, y, x, wId)[1]
                #     wId += 1
                # elif isPixUpperLeft(img, y, x, wId):
                #     y = isPixUpperLeft(img, y, x, wId)[1]
                #     x = isPixUpperLeft(img, y, x, wId)[2]
                #     wId += 1
                else:
                    y -= 1
            else:
                y -= 1
        x += 1




    colorDwin(img, dWinList)            

dWinList.append(Dwin(0, 0, 0, 0, 0))
createWindows(letter, dWinList)

cv2.imshow('title', letter)
cv2.waitKey(0)
cv2.destroyAllWindows()

