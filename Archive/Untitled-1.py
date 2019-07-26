import numpy as np
import cv2
# Global variables
canvas = np.ones([648,1152,3],'uint8')*255
radius = 3
color = (0,255,0)
pressed = False
# click callback
def click(event, x, y, flags, param):
    global canvas, pressed
    # if event == cv2.EVENT_LBUTTONDOWN: #pressed is only = to true when left button is pressed down
    #     pressed = True
    #     cv2.circle(canvas,(x,y),radius,color,-1)
    if event == cv2.EVENT_MOUSEMOVE: #draws circle when mouse is moved
        cv2.circle(canvas,(x,y),radius,color,-1)
    elif event == cv2.EVENT_LBUTTONUP:
        pressed = False
# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)
# Forever draw loop
while True:
    test = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
    img = cv2.add(test, canvas)
    cv2.imshow("image", img)
    # key capture every 1ms
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('b'):
        color = (255,0,0)
    elif ch & 0xFF == ord('g'):
        color = (0,255,0)
cv2.destroyAllWindows()