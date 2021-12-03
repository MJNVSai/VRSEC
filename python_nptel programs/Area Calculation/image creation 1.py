# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 19:42:37 2021

CREATING THE COLOUR IMAGE

@author: Krishna
"""

import numpy as np
from PIL import Image

width = 5
height = 4

array = np.zeros([height,width,3],dtype=np.uint8)

'''
here 3 = byte value equally distributed for red ,blue,green compositions
        and dtype is a datatype and uint is the unsighned int
        and [height,width,3] is a shape of the image
'''

img = Image.fromarray(array)
img.save("image_2.png")

array1 = np.zeros([100,200,3],dtype=np.uint8)

array1[:,:100] = [255,128,0] # is an orange colour
array1[:,100:] = [0,0,255] # is a blue colour

#array1[::100] = [255,128,0] 
#array1[:100:] = [0,0,255] 

'''
ex: [255,128,0] that means it takes 255 as composition for red colour
 and 128 as composition for green colour
 and 0 as composition for blue colour
 lastly all compositions mixed we get orange colour
 '''

img = Image.fromarray(array1)
img.save("image_3.png")