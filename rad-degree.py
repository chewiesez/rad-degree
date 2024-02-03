#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 09:13:34 2022

@author: fost
"""

#python coding challenge for beginners - convert radians to degrees
 # Degree sign = u"\u00b0"

import math 
def choose_func():
    c = input('Enter 1 to convert RADIAN to DEGREE \nEnter 2 to convert DEGREE to RADIAN:\n')
    while c != '1' and c!= '2':
        choose_func()
    if c == '1':
        convert_radians()
    elif c == '2': 
        convert_degrees()


def convert_radians():
    r = float(input('Enter radians:\n'))
    k = 57.2958
    deg = (r*k)
    print(str(deg) + u"\u00b0")

def convert_degrees():
    d = float(input('Enter degrees:\n'))
    k = 180
    r = d * math.pi/k
    print("\u03C0" + " " + str(r))
  
   
choose_func()
