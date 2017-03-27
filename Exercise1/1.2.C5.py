#-*- coding: utf-8 -
import math
import numpy as np
import matplotlib.pyplot as plt

def theorem1_6(f,x):
    for i in range(0,1000):
        x = f(x)
    print(x)


def f1(x):
    return np.cos(x)
def f2(x):
    return np.cos(x)**(2)


def plotCurves():
    x = np.linspace(-5,5)
    plt.plot(x, x, label='x')
    plt.plot(x, f1(x), label='f1')
    plt.plot(x, f2(x), label='f2')
    plt.legend(loc='upper left')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')


theorem1_6(f1,1)
theorem1_6(f2,1)
plotCurves()
plt.show()
