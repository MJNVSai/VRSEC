# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:27:51 2021

@author: Krishna
"""

import speech_recognition as sr
audio = ("05 - Pachcha Bottesi.wav")
# it uses audio file as source

r = sr.Recognizer() # it initilizes the recognizer

with sr.AudioFile(audio) as source:
    sound = r.record(source)
# it reads the audio file

try:
    print("audio file contains: \n" + r.recognize_google(sound))
except sr.UnknownValueError :
    print("GooGle speech recognition could not understand audio")
except sr.RequestError :
    print("could't get the results from Google Speech Recognition")
    

