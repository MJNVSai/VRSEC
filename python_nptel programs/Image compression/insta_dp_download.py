# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 16:11:55 2021

DOWNLOAD INSTAGRAM DP

use pip install instaloader

@author: Krishna
"""

import instaloader

ig = instaloader.Instaloader()

profile = input("enter insta username: ")

ig.download_profile(profile,profile_pic_only=True)