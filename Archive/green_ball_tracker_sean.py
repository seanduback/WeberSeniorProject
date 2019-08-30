
# this is code I got from the site below
# https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

# press q to exit

# import the necessary packages
from collections import deque
import numpy as np
import datetime
import cv2

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (0, 120, 70)
greenUpper = (50, 255, 180)
pts = deque(maxlen=100)
# if a video path was not supplied, grab the reference
# to the webcam
camera = cv2.VideoCapture(0)
letter = cv2.imread('BW_Letter.jpg', 1)


# keep looping
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()

    # resize the frame, blur it, and convert it to the HSV
    # color space
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
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        #dWinNum, maxPixDist = getMaxDistance(letter, dWinNum, x, y)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size
        if radius > 0:
            # x goes from 0 (camera left) to 600 (camera right) 
            #print('x: {} \t y: {}  #:{} \t D: {} \t '.format(x, y, dWinNum, maxPixDist))
            print('{} \t x: {} \t y: {}'.format(datetime.datetime.now(), x, y))
            # draw the centroid on the frame
            cv2.circle(letter, center, 5, (0, 0, 255), -1)
            

    # show the frame to our screen
    cv2.imshow("Frame", letter)
    key = cv2.waitKey(1) & 0xFF

    # if the q key is pressed, stop the loop
    if key == ord("q"):
        break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
