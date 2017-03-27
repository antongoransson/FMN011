#-*- coding: utf-8 -
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def newtonRaphMethod(f,fprim,x):
    for i in range(0,10):
        if(fprim(x)==0):
            break
        else:
            x= x-f(x)/fprim(x)
    print(x)

def function(x):
    return np.exp(np.sin(x)**(3)) + x**(6) -2*x**(4) -x**(3) -1.0

def functionPrim(x):
    return 3.0*np.exp(np.sin(x)**(3))*np.sin(x)**(2)*np.cos(x) + 6*x**(5) -8*x**(3) -3*x**(2)

def plotCurve():
    x = np.linspace(-2,2,num=1000)
    fig, ax = plt.subplots()
    ax.plot(x,function(x))
    #ax.set_aspect('equal')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.show()
print(fsolve(function,-1))
newtonRaphMethod(function, functionPrim,-1.0)
newtonRaphMethod(function, functionPrim,0)
newtonRaphMethod(function, functionPrim,2)
plotCurve()
