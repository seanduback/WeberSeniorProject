import numpy as np 
import cv2
import sys
from pandas import DataFrame

img = cv2.imread('ScriptL.jpg', cv2.IMREAD_COLOR)
white = [255, 255, 255]
white_1 = [254, 254, 254]
white_2 = [250, 250, 250]
white_3 = [252, 252, 252]
white_4 = [253, 253, 253]
white_5 = [251, 251, 251]
white_6 = [249, 249, 249]
black = [0, 0, 0]
black_1 = [1, 1, 1]
black_2 = [2, 2, 2]
black_3 = [3, 3, 3]
black_4 = [4, 4, 4]
black_5 = [5, 5, 5]

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
        #if [r, g, b] != black:
        # if img[y, x] == white_1 or white_2 or white_3 or white_4 or white_5 or white_6:
        #     img[y, x] = white
        if [r, g, b] == black_1 or black_2 or black_3 or black_4 or black_5: 
        #if [r, g, b] != white or white_1 or white_2 or white_3 or white_4 or white_5 or white_6:
            #img[y, x] = black
            #px = img[y,x]
            # #ds = x*y
            #PixColor = { }
            print ("Pixel # x= %s, y= %s  Color = %s" % (x, y, [r, g, b]))
            #img[y,x] = white
        else:  
            count += 1
            if count == 100000:
                print ("1")
                count = 0
        
cv2.imshow('HandwritingHelp',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
#         'Price': [32000,35000,37000,45000]
#         }

# df = DataFrame(Cars, columns= ['Brand', 'Price'])

# export_excel = df.to_excel (r'C:\Users\Ron\Desktop\export_dataframe.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path

# print (df)