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

# initLetter(letter, dWinList) 

# colorDwin(letter, dWinList)
# cv2.imshow('title', letter)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

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
colorDwin(letter, dWinList)
cv2.imshow('title', letter)
cv2.waitKey(0)
cv2.destroyAllWindows()
