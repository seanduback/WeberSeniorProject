# from tkinter import Canvas
# from PIL import ImageTK
import sys
import numpy as np 
import cv2
from pynput.mouse import Controller
from collections import deque
import datetime

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
pixDist = []



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

def greenBallTracking (img):
    # this is code I got from the site below
    # https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

    # define the lower and upper boundaries of the "green"
    greenLower = (55//2, 50, 6)    # lower limit
    greenUpper = (90//2, 255, 255) # upper limit
  
    # grab the referenceto the webcam
    camera = cv2.VideoCapture(1)

    # grab the current frame
    (grabbed, frame) = camera.read()

    # resize the frame, blur it, and convert it to the HSV color space
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # construct a mask for the color "green", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # centroid
        c = max(cnts, key=cv2.contourArea)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size
        if radius > 2:
            cv2.circle(img, center, 5, (0, 0, 255), -1)

    # cleanup the camera
    camera.release()

def distance(x0, y0, x1, y1):
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

def getMaxDistance (img, dWinNum, inputX, inputY):
    for i in range (dWinNum, dWinNum + 1):
        for x in range (Dwin(i).xmin, Dwin(i).xmax):
            for y in range (Dwin(i).ymin, Dwin(i).ymax, -1): 
                if img[y, x] == black:
                    count += 1
                    pixDist[count] = distance(x, y, inputX, inputY)
        maxPixDist[i] = max(pixDist)
    if maxPixDist[i+1] > maxPixDist[i]:
        return dWinNum+1, maxPixDist[i+1]
    else:
        return dWinNum, maxPixDist[i]                 
                    

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

key = cv2.waitKey(1) & 0xFF
# if the q key is pressed, stop the loop
if key == ord("q"):
    cv2.destroyAllWindows()
else: 
    greenBallTracking(letter)
    cv2.imshow("Frame", letter)