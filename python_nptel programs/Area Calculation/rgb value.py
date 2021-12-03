# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 17:31:54 2021

TO KNOW THE RGB VALUES OF PICTURE

@author: Krishna
"""

from PIL import Image
im = Image.open('image_3.png')

rgb_im = im.convert('RGB')
r,g,b = rgb_im.getpixel((1,1))
#r,g,b = rgb_im.getpixel((150,1))

# here 1,1, are x,y coordinates

print()
print(rgb_im)

print("the R G B values are: ",r,g,b)