#-*- coding: utf-8 -
import math

import numpy as np


def fixedPoint(f,x):
    while x-f(x) >10**(-5):
        x=f(x)

    print(x)

def f1(x):
    return x**(-3) -2*x-2

def f2(x):
    return math.exp**(x) + x -7

def f3(x):
    return math.exp**(x)+ math.sin(x) -4

fixedPoint(f1,2)
