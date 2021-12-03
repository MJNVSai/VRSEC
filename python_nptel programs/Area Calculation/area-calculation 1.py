# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 17:45:05 2021

AREA CALCULATION - METHOD - 1

@author: Krishna
"""
'''
    https://pinetools.com/image-color-picker
'''

import imageio
import scipy.misc as sp
from PIL import Image
import numpy as np
import random

img = imageio.imread("india.jpg")  

count_pun = 0 #pun means punjab
count_in = 0 #in means india
count = 0

while count <= 100000:
    x = random.randint(0,850)
    y = random.randint(0,800)
    z = 0
    
    # here x is bredth and y is length of the image
    # and 907 is the bredth of the image and 836 is the length of the image
    
    if img[x][y][z] == 60:
        # 60 is the rgb value of india
        count_in += 1
        count += 1
    else:
        if img[x][y][z] == 80:
            # 80 is the rgb value of punjab
            count_pun += 1
            count += 1
            
area_pun = (count_pun/count_in)*3287263

# here area of the india = 3287263

print("area of the punjab approximate value is: ",area_pun) 
    