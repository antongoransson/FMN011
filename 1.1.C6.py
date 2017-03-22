 #-*- coding: utf-8 -
import math
import numpy as np
def bisection(a,b,sigma):
    c=5
    while(b-a)/2.0 > sigma:
        c = (b+a)/2.0
        if(function(c)*function(a) > 0):
            a=c
        elif(function(c)*function(a) < 0):
            b=c
    return c

def function(x):
    return math.cos(x)-math.sin(x)

print(bisection(0,1,10**(-6)))
