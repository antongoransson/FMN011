 #-*- coding: utf-8 -
import math

import numpy as np






def bisection(a,b,sigma):
    while(b-a)/2.0 > sigma:
        c = (b+a)/2.0
        print ("lul")
        if(function(c)*function(a) > 0):
            a=c
        elif(function(c)*function(a) < 0):
            b=c
    return c

def function(x):
    return np.cos(x)-np.sin(x)

print(bisection(0,1,0.000006))
