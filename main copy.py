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
letter = cv2.imread('BW_Letter.jpg', 1)
pixDist = []
minPixDist = []
# grab the referenceto the webcam
camera = cv2.VideoCapture(0)
# define the lower and upper boundaries of the "green"
colorLower = (0, 120, 70)
colorUpper = (50, 255, 180)
winNum = 0
tLCorner = (643, 183)
bLCorner = (643, 825)
tRCorner = (1127, 183)
bRCorner = (1127, 825)

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

def distance(x0, y0, x1, y1):
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

def getMinDistance (img, dWinNum, inputX, inputY, class_type="Dwin"):
    countFirst = 0
    countSecond = 0

    for Dwin in dWinList:
        if Dwin.idnum == dWinNum:
            for x in range(Dwin.xmin, Dwin.xmax):
                for y in range(Dwin.ymin, Dwin.ymax, -1):
                    if np.array_equal(img[y, x], black):
                        countFirst += 1
                        pixDist.insert(countFirst, distance(x, y, inputX, inputY))
                        #pixDist[countFirst].append(distance(x, y, inputX, inputY))
            minPixDist.insert(dWinNum, min(pixDist)) 
            #minPixDist[dWinNum].append(min(pixDist))
            
        elif Dwin.idnum == (dWinNum+1):
            for x in range(Dwin.xmin, Dwin.xmax):
                for y in range(Dwin.ymin, Dwin.ymax, -1):
                    if  np.array_equal(img[y, x],black):
                        countSecond += 1
                        pixDist.insert(countSecond, distance(x, y, inputX, inputY))
            minPixDist.insert(dWinNum+1, min(pixDist)) 

    if minPixDist[dWinNum+1] < minPixDist[dWinNum]:
        print ("Window#= %s, Distance from Input to nearest letter pixel = %s"% (Dwin.idnum, minPixDist[dWinNum+1]))
        
        return dWinNum+1, minPixDist[dWinNum+1]
    else:
        print ("Window#= %s, Distance from Input to nearest letter pixel = %s"% (Dwin.idnum, minPixDist[dWinNum]))
        return dWinNum, minPixDist[dWinNum]

    # for i in range (dWinNum, dWinNum + 1):
    #     for xd in dWinList (Dwin(i).xmin, Dwin(i).xmax):
    #         for yd in range (Dwin(i).ymin, Dwin(i).ymax, -1): 
    #             if img[yd, xd] == black:
    #                 count += 1
    #                 pixDist[count] = distance(xd, yd, inputX, inputY)
    #     maxPixDist[i].append(max(pixDist))
    
    # if maxPixDist[i+1] > maxPixDist[i]:
    #     return dWinNum+1, maxPixDist[i+1]
    # else:
    #     return dWinNum, maxPixDist[i]                 
                    

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



cv2.line(letter, tLCorner, bLCorner, 5)
cv2.line(letter, tRCorner, tLCorner, 5)
cv2.line(letter, tRCorner, bRCorner, 5)
cv2.line(letter, bRCorner, bLCorner, 5)

while True:
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
        centerX = (int(M["m10"] / M["m00"]) + 645)
        centerY = (int(M["m01"] / M["m00"]) + 185)
        cv2.circle(letter, (centerX, centerY), 2, (0, 0, 255), -1)
        winNum, pixDistance = getMinDistance(letter, winNum, x, y)

    cv2.imshow("Learn to Write!", letter)
    key = cv2.waitKey(1) & 0xFF

    # if the q key is pressed, stop the loop
    if key == ord("q"):
        break

# if the q key is pressed, stop the loop   
camera.release()
cv2.destroyAllWindows()



