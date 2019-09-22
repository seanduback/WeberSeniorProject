from collections import deque
import numpy as np
import datetime
import cv2
import math


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
letter = cv2.imread('bw_image.png', 1)
pixDistFirst = []
pixDistSecond = []
minPixDist = {}
# grab the referenceto the webcam
camera = cv2.VideoCapture(0)
# define the lower and upper boundaries of the "green"
colorLower = (0, 120, 70)
colorUpper = (50, 255, 180)
winNum = 0
tLCorner = (350, 160)
bLCorner = (350, 500)
tRCorner = (450, 160)
bRCorner = (450, 500)

############################################################# Class Definitions #################################################

class Dwin(object):
    def __init__(self, idnum=0, ymin=0, ymax=0, xmin=0, xmax=0):
        self.idnum = idnum
        self.ymin = ymin
        self.ymax = ymax
        self.xmin = xmin
        self.xmax = xmax

############################################################# Functions ###########################################

def distance(x0, y0, x1, y1):
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

def getMinDistance (img, dWinNum, inputX, inputY):
    countFirst = 0
    countSecond = 0

    # for Dwin in dWinList:
    #     if Dwin.idnum == dWinNum:
    for x in range(dWinList[dWinNum].xmin, dWinList[dWinNum].xmax):
        for y in range(dWinList[dWinNum].ymin, dWinList[dWinNum].ymax, -1):
            if np.array_equal(img[y, x], black):
                countFirst += 1
                pixDistFirst.insert(countFirst, distance(x, y, inputX, inputY))
        
    #elif Dwin.idnum == (dWinNum+1):
    for x in range(dWinList[dWinNum+1].xmin, dWinList[dWinNum+1].xmax):
        for y in range(dWinList[dWinNum+1].ymin, dWinList[dWinNum+1].ymax, -1):
            if  np.array_equal(img[y, x],black):
                countSecond += 1
                pixDistSecond.insert(countSecond, distance(x, y, inputX, inputY))
    
    if countFirst != 0: minPixDist.update({dWinNum: min(pixDistFirst)})
    if countSecond != 0: minPixDist.update({dWinNum+1: min(pixDistSecond)})
    if countFirst != 0 or countSecond != 0:  

        if minPixDist[dWinNum+1] < minPixDist[dWinNum]:
            print ("Window#= %s, Distance from Input to nearest letter pixel = %s"% (dWinNum+1, minPixDist[dWinNum+1]))
            pixDistFirst.clear()
            pixDistSecond.clear()
            return dWinNum+1, minPixDist[dWinNum+1]
        else:
            print ("Window#= %s, Distance from Input to nearest letter pixel = %s"% (dWinNum, minPixDist[dWinNum]))
            pixDistFirst.clear()
            pixDistSecond.clear()
            return dWinNum, minPixDist[dWinNum]

def colorDwin (img, class_type="Dwin"):
    for Dwin in dWinList:
        print ("Window#= %s, xmin=%s, xmax= %s, ymin= %s ymax= %s"% (Dwin.idnum, Dwin.xmin, Dwin.xmax, Dwin.ymin, Dwin.ymax))
        for x in range(Dwin.xmin, Dwin.xmax):
            for y in range(Dwin.ymin, Dwin.ymax, -1):
                if np.array_equal(img[y, x], black):
                    print ("x=%s y=%s"%(x, y))
                    img[y, x] = white
                # else:
                #     img[y, x] = 0


def init ():
    #make Distance windows
    #def __init__(self, idnum=0, ymin=0, ymax=0, xmin=0, xmax=0):
    dWinList.append(Dwin(0, 421, 404, 366, 374))
    dWinList.append(Dwin(1, 404, 402, 372, 376))
    dWinList.append(Dwin(2, 402, 396, 374, 378))
    dWinList.append(Dwin(3, 396, 394, 376, 383))
    dWinList.append(Dwin(4, 394, 390, 379, 384))
    dWinList.append(Dwin(5, 390, 386, 380, 385))
    dWinList.append(Dwin(6, 386, 365, 382, 400))
    dWinList.append(Dwin(7, 365, 345, 390, 410))
    dWinList.append(Dwin(8, 345, 325, 395, 415))
    dWinList.append(Dwin(9, 325, 305, 400, 420))
    dWinList.append(Dwin(10, 305, 285, 405, 425))
    dWinList.append(Dwin(11, 285, 265, 410, 430))
    dWinList.append(Dwin(12, 265, 245, 420, 440))
    dWinList.append(Dwin(13, 245, 225, 420, 440))
    dWinList.append(Dwin(14, 225, 205, 420, 440))
    dWinList.append(Dwin(15, 205, 185, 420, 440))
    #Dwin 16 begins left movement
    dWinList.append(Dwin(16, 205, 185, 400, 420))
    #Dwin 17 begins down movement
    dWinList.append(Dwin(17, 225, 205, 390, 410))
    dWinList.append(Dwin(18, 245, 225, 385, 405))
    dWinList.append(Dwin(19, 265, 245, 380, 400))
    dWinList.append(Dwin(20, 285, 265, 380, 400))
    dWinList.append(Dwin(21, 305, 285, 375, 395))
    dWinList.append(Dwin(22, 325, 305, 375, 390))
    dWinList.append(Dwin(23, 345, 325, 375, 385))
    dWinList.append(Dwin(24, 365, 345, 375, 385))
    dWinList.append(Dwin(25, 385, 365, 370, 380))
    dWinList.append(Dwin(26, 405, 385, 370, 380))
    dWinList.append(Dwin(27, 425, 405, 370, 380))
    dWinList.append(Dwin(28, 445, 425, 370, 380))
    dWinList.append(Dwin(29, 465, 445, 370, 380))
    dWinList.append(Dwin(30, 490, 465, 370, 380))
    #Dwin 28 begins right movement
    dWinList.append(Dwin(31, 495, 475, 380, 400))
    dWinList.append(Dwin(32, 495, 475, 400, 420))
    #Dwin 30 begins up movement
    dWinList.append(Dwin(33, 475, 455, 410, 430))
    dWinList.append(Dwin(34, 455, 435, 420, 440))
    dWinList.append(Dwin(35, 435, 405, 430, 450))

    # #Create square boarder around letter
    # cv2.line(letter, tLCorner, bLCorner, 5)
    # cv2.line(letter, tRCorner, tLCorner, 5)
    # cv2.line(letter, tRCorner, bRCorner, 5)
    # cv2.line(letter, bRCorner, bLCorner, 5)

init()
#colorDwin(letter, dWinList)
while True:
    cv2.imshow("Learn to Write!", letter)
    key = cv2.waitKey(1) & 0xFF

    # if the q key is pressed, stop the loop
    if key == ord("q"):
        break

# while True:
   
    # grab the current frame
    (grabbed, frame) = camera.read()
    frame = cv2.flip(frame, 1)

    # resize the frame, blur it, and convert it to the HSV color space
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # construct a mask for the color then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, colorLower, colorUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        centerX = (int(M["m10"] / M["m00"])+50)
        centerY = (int(M["m01"] / M["m00"])+50)
        if centerX < 800 and centerY < 600:
            winNum, pixDistance = getMinDistance(letter, winNum, x, y)
            cv2.circle(letter, (centerX, centerY), 1, (0, 0, 255), -1)
            

    cv2.imshow("Learn to Write!", letter)
    key = cv2.waitKey(1) & 0xFF

    # if the q key is pressed, stop the loop
    if key == ord("q"):
        break

# if the q key is pressed, stop the loop
camera.release()
cv2.destroyAllWindows()



