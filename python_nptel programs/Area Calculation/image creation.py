# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:11:39 2021

CREATING THE IMAGES

@author: Krishna
"""

import numpy as np
from PIL import Image

width = 500
height = 420

array = np.zeros([height,width,3],dtype=np.uint8)

img = Image.fromarray(array) 
img.save('image_1.png')

'''
here 3 = byte value equally distributed for red ,blue,green compositions
        and dtype is a datatype and uint is the unsighned int
        and [height,width,3] is a shape of the image
'''
