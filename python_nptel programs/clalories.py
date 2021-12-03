# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:14:29 2021

week 8 nptel joc quiz

@author: Krishna
"""

import pandas as tiger

data = {
        "calories": [420,380,390],
        "duration": [50,40,45]
        }

myvar = tiger.DataFrame(data)

# myvar = pandas.DataFrame(data)
#myvar = tiger.Series(data)

print(myvar)