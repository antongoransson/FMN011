#-*- coding: utf-8 -
import math
import matplotlib.pyplot as plt
import numpy as np


def fixedPoint(f,x0):
    x= x0
    for i in range(0,100) :
        x = f(x)
    print(x)

def f1(x):
    return (2*x+2)**(1/3)

def f2(x):
    return math.log(7-x)


def f3(x):
    return math.log(4-math.sin(x))

def plotCurve():
    x = np.linspace(-2,2,num=1)
    plt.plot(x**(3)-2*x-2)
    plt.show()

fixedPoint(f1,2.0)
fixedPoint(f2,2.0)
fixedPoint(f3,2.0)
#plotCurve()
