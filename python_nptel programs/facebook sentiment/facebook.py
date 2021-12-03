# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 07:55:44 2021

FACEBOOK SENTIMENT ANALYSIS

@author: Krishna
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# to download any package ex: vader lexicon we below statement
nltk.downloader.download('vader_lexicon')

file = 'comments.xls'

# reading the excel file
xl = pd.ExcelFile(file)

# parsing Excel sheet to data frames
dfs = xl.parse(xl.sheet_names[0])

#removes the blank rows from the data frames
#dfs = list(dfs['Timeline'])
dfs = list(dfs)
print("the data frames are: \n\n",dfs,"\n")

sid = SentimentIntensityAnalyzer()
#the below str1 takes the utc time which is in excel file
str1 = "UTC+05:30"

for data in dfs:
    a = data.find(str1)
    # if it finds str1 it returns 0 or 1 if not finds the str1 it returns -1
    if a == -1:
        ss = sid.polarity_scores(data)
        print(data)
        
        for k in ss:
            print(k,ss[k])