import cv2
import numpy as np 

white = [255,255,255]
black = [0,0,0]
nearBlack = [5,5,5]

letter = cv2.imread('ScriptLsmall.jpg', 1) 
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

changeToBW(letter)
cv2.imwrite("BW_ScriptLsmall.jpg", letter)
