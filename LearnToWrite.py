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
letter = cv2.imread('BW_ScriptLsmall.jpg', 1)
pixDistFirst = []
pixDistSecond = []
minPixDist = {}
# grab the referenceto the webcam
camera = cv2.VideoCapture(0)
# define the lower and upper boundaries of the "green"
colorLower = (0, 120, 70)
colorUpper = (50, 255, 180)
winNum = 0
tLCorner = (643, 183)
bLCorner = (643, 660)
tRCorner = (1250, 183)
bRCorner = (1250, 660)

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
    dWinList.append(Dwin(1, 599, 1, 1, 799,))


    # #Create square boarder around letter
    # cv2.line(letter, tLCorner, bLCorner, 5)
    # cv2.line(letter, tRCorner, tLCorner, 5)
    # cv2.line(letter, tRCorner, bRCorner, 5)
    # cv2.line(letter, bRCorner, bLCorner, 5)

init()
colorDwin(letter, dWinList)
while True:
    cv2.imshow("Learn to Write!", letter)
    key = cv2.waitKey(1) & 0xFF

    # if the q key is pressed, stop the loop
    if key == ord("q"):
        break

# while True:
   
#     # grab the current frame
#     (grabbed, frame) = camera.read()
#     frame = cv2.flip(frame, 1)

#     # resize the frame, blur it, and convert it to the HSV color space
#     blurred = cv2.GaussianBlur(frame, (11, 11), 0)
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # construct a mask for the color then perform
#     # a series of dilations and erosions to remove any small
#     # blobs left in the mask
#     mask = cv2.inRange(hsv, colorLower, colorUpper)
#     mask = cv2.erode(mask, None, iterations=2)
#     mask = cv2.dilate(mask, None, iterations=2)

#     # find contours in the mask and initialize the current
#     # (x, y) center of the ball
#     cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
#     center = None

#     # only proceed if at least one contour was found
#     if len(cnts) > 0:
#         # find the largest contour in the mask, then use
#         # centroid
#         c = max(cnts, key=cv2.contourArea)
#         ((x, y), radius) = cv2.minEnclosingCircle(c)
#         M = cv2.moments(c)
#         centerX = (int(M["m10"] / M["m00"])+50)
#         centerY = (int(M["m01"] / M["m00"])+50)
#         if centerX < 800 and centerY < 600:
#             cv2.circle(letter, (centerX, centerY), 2, (0, 0, 255), -1)
#             #winNum, pixDistance = getMinDistance(letter, winNum, x, y)

#     cv2.imshow("Learn to Write!", letter)
#     key = cv2.waitKey(1) & 0xFF

#     # if the q key is pressed, stop the loop
#     if key == ord("q"):
#         break

# # if the q key is pressed, stop the loop
# camera.release()
# cv2.destroyAllWindows()



