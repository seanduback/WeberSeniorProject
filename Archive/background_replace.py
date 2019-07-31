import cv2

cap = cv2.VideoCapture(1)

greenLower = (55//2, 50, 6)    # lower limit
greenUpper = (90//2, 255, 255) # upper limit

# give a few iterations for the lighting to adjust
count = 0
while(count < 50):
    return_frame, frame_original = cap.read()
    count += 1

while(True):
    return_frame, frame = cap.read()

    blurred = cv2.GaussianBlur(frame, (11,11), 0)  # blur to filter out noise
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) # convert to HSV space
    
    
    mask = cv2.inRange(hsv, greenLower, greenUpper) # find the green
    mask = cv2.erode(mask, None, iterations=2)      # erode to remove stray pixels
    mask = cv2.dilate(mask, None, iterations=3)     # dilate to restore image
    
    mask_inv = 255 - mask # inverse of the mask
    bg = cv2.bitwise_and(frame,frame, mask=mask_inv)                           # the background is taken from the mask_inv
    original_patch = cv2.bitwise_and(frame_original,frame_original, mask=mask) # the original_patch is taken from the mask
    
    final = bg + original_patch # add background and original_patch to form final image
    cv2.imshow('frame', final)
    
    # press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# close things out
cap.release()
cv2.destroyAllWindows()