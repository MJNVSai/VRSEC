# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 18:52:52 2021

IMAGE COMPRESSION

@author: Krishna
"""

import numpy as np

from PIL import Image

im = Image.open('lena.png')
pixelmap = im.load()

i = np.asanyarray(im)
print("image matrix: \n",i)
#print("pixel map is: \n",pixelmap)

# creating the duplicate image with same original image dimensions
img = Image.new(im.mode,im.size) # mode means shape
pixelnew = img.load()

'''
0 - 31 = 0
32 - 63 = 1
64 - 95 = 2
96 - 127 = 3
128 - 159 = 4
160 - 191 = 5
192 - 223 = 6
224 - 225 = 7
'''

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixelmap[i,j] >= 0 and pixelmap[i,j] <= 31:
            pixelnew[i,j] = 0
            
        elif pixelmap[i,j] >= 32 and pixelmap[i,j] <= 63:
            pixelnew[i,j] = 1
            
        elif pixelmap[i,j] >= 64 and pixelmap[i,j] <= 95:
            pixelnew[i,j] = 2
            
        elif pixelmap[i,j] >= 96 and pixelmap[i,j] <= 127:
            pixelnew[i,j] = 3
            
        elif pixelmap[i,j] >= 128 and pixelmap[i,j] <= 159:
            pixelnew[i,j] = 4
            
        elif pixelmap[i,j] >= 160 and pixelmap[i,j] <= 191:
            pixelnew[i,j] = 5
            
        elif pixelmap[i,j] >= 192 and pixelmap[i,j] <= 223:
            pixelnew[i,j] = 6
            
        elif pixelmap[i,j] >= 224 and pixelmap[i,j] <= 255:
            pixelnew[i,j] = 7
            
img.save('lena_2.png')
I1 = np.asanyarray(Image.open('lena_2.png'))
print("compressed image matrix: ",I1)