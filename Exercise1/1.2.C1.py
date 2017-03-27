#-*- coding: utf-8 -
import math
import matplotlib.pyplot as plt
import numpy as np


def fixedPoint(f,x0):
    x= x0
    for i in range(0,1000) :
        x = f(x)
    print(x)

def f1(x):
    return (2*x+2)**(1/3)

def f2(x):
    return np.log(7-x)


def f3(x):
    return np.log(4-np.sin(x))

def plotCurve():
    x = np.linspace(-2,3)
    plt.plot(x, x, label='x')
    plt.plot(x, f1(x), label='f1')
    plt.plot(x, f2(x), label='f2')
    plt.plot(x, f3(x), label='f3')
    plt.legend(loc='upper left')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()

fixedPoint(f1,2.0)
fixedPoint(f2,2.0)
fixedPoint(f3,2.0)
plotCurve()
