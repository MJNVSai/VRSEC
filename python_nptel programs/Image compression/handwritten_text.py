# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 08:56:20 2021

DIGITAL TEXT TO HAND WRITTEN

@author: Krishna
"""

import pywhatkit as pt

text = '''Buttabomma Lyrics Translation English
Inthakanna manchi polikedhi
Naaku thattaledhu kaani ammu
Ee love anedhi bubble gum-u
Antukunnadhante podhi nammu

A comparision better than this
didn’t striked me, oh dear!
This love is like a bubble gum
It wont come off once its stuck, believe me

Mundununchi andharanna maategaani
Mallo antunnane ammu
Idhi cheppakunda vacche thummu
Premanaapalevu nannu nammu

These are the words all say from past,
But I am saying it again ,oh dear
This is like sneeze which comes uninvitedly
You cant stop falling in love,believe me'''

pt.text_to_handwriting(text,save_to="mytext",rgb=(0,0,255))

pt.image_to_ascii_art("lena.png","lena_asciiart")
pt.image_to_ascii_art("yesuraju.jpeg","yesuraju_asciiart") 

