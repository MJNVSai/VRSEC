# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 07:57:53 2021

IMAGE PROCESSING OR APPLYING IMAGE FILTERS

@author: Krishna
"""



# flipping the image

from PIL import Image

#opening the image
img = Image.open('newspaper.jpeg')

# transposing image in other words flipping the image
flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)

# saving the file
flip_img.save('corrected.jpeg')

print("flipping the image is done")



#image enhancement using CLAHE

import cv2

#reading the image

img1 = cv2.imread('bulletwall.jpeg')

#preparation for CLAHE

clahe = cv2.createCLAHE()

#convert the image to grey scale image

gray_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

#apply enhacement
enh_img = clahe.apply(gray_img)

#saving the file
cv2.imwrite('enhancedwall.jpeg',enh_img)

print("image enhancing is done")