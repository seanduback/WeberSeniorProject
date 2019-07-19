import numpy as np 
import cv2
import sys

img = cv2.imread('LowerCaseCursiveL.jpg', cv2.IMREAD_COLOR)
white = [255, 255, 255]
black = [0, 0, 0]
count = 0
#dimensions = img.shape
 
# height, width, number of channels in image
ys = img.shape[0]
xs = img.shape[1]
#channels = img.shape[2]

# print('Image Dimension    : ',dimensions)
# print('Image Height       : ',height)
# print('Image Width        : ',width)
# #print('Number of Channels : ',channels) 

for x in range(0, xs):
    for y in range(0, ys):
        [r, g, b] = img[y, x]
        r /= 255.0
        g /= 255.0
        b /= 255.0
        if [r, g, b] != black:
            # px = img[y,x]
            # #ds = x*y
            # print ("Pixel # x= %s, y= %s  Color = %s" % (x, y, px))
            img[y,x] = white
        else:  
            count += 1
            if count == 100000:
                print ("1")
                count = 0
        
cv2.imshow('title',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

