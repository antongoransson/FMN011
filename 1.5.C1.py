#-*- coding: utf-8 -
import math
import matplotlib.pyplot as plt
import numpy as np

def secant_method(f,x0,x1):
    x_prev = x0
    x_i = x1
    x_i = x_i - f(x_i)*(x_i-x_prev)/(f(x_i)-f(x_prev))

    for n in range (0,100):
        xprev = x_i
        x_i = x_i - f(x_i)*(x_i-x_prev)/(f(x_i)-f(x_prev))
    print(x_i)

def f1(x):
    return x**(3)-2*x-2

def f2(x):
    return np.exp(x) + x -7

def f3(x):
    return np.exp(x) + np.sin(x) -4

secant_method(f1,1,2)
secant_method(f2,1,2)
secant_method(f3,1,2)
