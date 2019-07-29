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
            pixC = img[y, x]
            if pixC > 5: #if a pixel is not black/near black make it true white
                img[y,x] = 255
            else: #if a pixel is black/near black make it true black
                img[y,x] = 0

def isPixUp(img, y, x, wId):
    yL = y-DBOffset
    for xw in range(x, x+DSOffset):
        for yw in range(yL, y-1):
            if xw >= 1920: break
            elif img[yw, xw] == 0:
                # wId += 1   
                # dWinList.append(Dwin(wId, y-1, yL, x, x+DSOffset, 'u'))
                return yL, x, wId, 0 
    return 0

def isPixUpperRight(img, y, x, wId):
    yL = y-DBOffset
    xL = x+DBOffset
    for xw in range(xL+1, xL+DBOffset):
        for yw in range(yL, y-1):
            if xw >= 1920: break
            elif img[yw, xw] == 0:    
                # wId += 1   
                # dWinList.append(Dwin(wId, yL,  y-1, x+1, xL, 'ur'))
                return yL, xL, wId, 0 
    return 0

def isPixRight(img, y, x, wId):
    xL = x+DBOffset
    for xw in range(xL, xL+DSOffset):
        for yw in range(y-DSOffset, y):
            if img[yw, xw] == 0: 
                wId += 1   
                dWinList.append(Dwin(wId, y, y-DBOffset, xL, xL+DBOffset, 'r'))
                return y, xL, wId, 0 
    return y, x, wId, 1

def isPixLeft(img, y, x, wId):
    xL = x - DBOffset
    for xw in range(xL, xL-DSOffset):
        for yw in range(y-DSOffset, y):
            if img[yw, xw] == 0:
                wId += 1
                dWinList.append(Dwin(wId, y, y-DBOffset, xL, xL+DBOffset, 'l'))
                return y, xL, wId, 0 
    return y, x, wId, 1

def isPixUpperLeft(img, y, x, wId):
    yL = y-DBOffset
    xL = x-DBOffset
    for xw in range(xL, xL+DSOffset):
        for yw in range(yL-DSOffset, yL):
            if xw >= 1920: break
            elif img[yw, xw] == 0:
                wId += 1
                dWinList.append(Dwin(wId, yL, yL-DBOffset, xL, xL+DBOffset, 'ur'))
                return yL, xL, wId, 0 
    return y, x, wId, 1

def isPixDown(img, y, x, wId):
    yL = y+DBOffset
    for xw in range(x, x+4):
        for yw in range(yL-4, yL):
            if xw >= 1920: break
            elif img[yw, xw] == 0:
                wId += 1
                dWinList.append(Dwin(wId, yL, yL-DBOffset, x, x+DBOffset, 'd'))
                return yL, x, wId, 0 
    return y, x, wId, 1 

def isPixDownLeft(img, y, x, wId):
    yL = y+DBOffset
    xL = x-DBOffset
    for xw in range(xL, xL+DSOffset):
        for yw in range(yL-DBOffset, yL):
            if xw >= 1920: break
            elif img[yw, xw] == 0:
                wId += 1
                dWinList.append(Dwin(wId, yL, yL-DBOffset, xL, xL+DBOffset, 'dl'))
                return yL, xL, wId, 0 
    return y, x, wId, 1

def isPixDownRight(img, y, x, wId):
    yL = y+DBOffset
    xL = x+DBOffset
    for xw in range(xL, xL+DBOffset):
        for yw in range(yL-DBOffset, yL):
            if xw >= 1920: break
            elif img[yw, xw] == 0:    
                wId += 1   
                dWinList.append(Dwin(wId, yL, yL-DBOffset, xL, xL+DBOffset, 'dr'))
                return yL, xL, wId, 0
    return y, x, wId, 1

def createFirstDWindow(img, y, x, wId):
    dWinList.append(Dwin(wId, y, y-3, x, x+3, 'fr')) #create first window at the most lower left pixel

def initLetter(img, class_type = "Dwin"):
    """Convert img to BW and Create Decision windows"""
    #change the image to black and white
    changeToBW(img)
    # find the height, width, of the image
    ys = img.shape[0]
    xs = img.shape[1]
    oneTimeFlag = 1
    wId = 1
    #iterate over image starting at bottom left to find most lower left pixel
    x = 0
    y = ys-1
    while x < xs-1:
        y = ys-1
        while  y > 0:
            if img[y, x] == 0:
                if oneTimeFlag:
                    oneTimeFlag = 0
                    createFirstDWindow(img, y, x, wId)
                    createDWindows(img, y, x, wId)
                    return 
            else:
                y -= 1
        x += 1     

def createDWindows(img, y, x, wId):
    u, r, ur, ul, l, d, dr, dl, end = 0, 0, 0, 0, 0, 0, 0, 0, 0
    while end != 1:
        if isPixUp(img, y, x, wId):
            wId += 1   
            dWinList.append(Dwin(wId, y-1, y-DBOffset, x, x+DSOffset, 'u'))
            y = y-DBOffset
        elif isPixUpperRight(img, y, x, wId):
            wId += 1   
            dWinList.append(Dwin(wId, y-DBOffset,  y-1, x+1, x+DBOffset, 'ur'))
            y = y-DBOffset
            x = x+DBOffset
        # y, x, wId, r = isPixRight(img, y, x, wId)
        # y, x, wId, ul = isPixUpperLeft(img, y, x, wId)
        # y, x, wId, l = isPixLeft(img, y, x, wId)
        # y, x, wId, d = isPixDown(img, y, x, wId)
        # y, x, wId, dl = isPixDownLeft(img, y, x, wId)
        # y, x, wId, dr = isPixDownRight(img, y, x, wId)
        # elif u == 1 and r == 1 and ur == 1 and ul == 1 and  l == 1 and  d == 1 and  dr == 1 and dl == 1:
        #     end = 1
        else:
            return

def colorDwin (img, class_type="Dwin"):
    for Dwin in dWinList:
        print ("Window#= %s, xmin=%s, xmax= %s, ymin= %s ymax= %s, direction=  %s"% (Dwin.idnum, Dwin.xmin, Dwin.xmax, Dwin.ymin, Dwin.ymax, Dwin.direction))
        for x in range(Dwin.xmin, Dwin.xmax):
            for y in range(Dwin.ymin, Dwin.ymax, -1):
                if img[y, x] == 0:
                    print ("Black")
                    img[y, x] = 255
                # else:
                #     img[y, x] = 0

initLetter(letter, dWinList)

colorDwin(letter, dWinList)
cv2.imshow('title', letter)
cv2.waitKey(0)
cv2.destroyAllWindows()


