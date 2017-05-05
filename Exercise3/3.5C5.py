#-*- coding: utf-8 -
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy.polynomial.polynomial as poly
import numpy.polynomial.chebyshev as chev

def f(x):
    return np.exp(-x**2)
def C5(n):
    evenX = np.linspace(-1,1,num=n)
    x= np.arange(-1,1,0.01)
    chevX = np.zeros(n)
    for i in range (1,n+1):
        chevX[i-1]= np.cos((2*i-1)*np.pi/(2*n))

    evenY =f(evenX)
    chevY = f(chevX)
    evenCoeffs = np.polyfit(evenX,evenY,n)
    chevCoeffs = np.polyfit(chevX,chevY,n)
    p1 = np.poly1d(evenCoeffs)
    p2 = np.poly1d(chevCoeffs)
    return p1,p2

def plotC5(n):
    x=  np.arange(-1,1,0.01)
    p1,p2 = C5(n)
    plt.figure()
    plt.title('polynomial of degree ' + str(n))
    plt.plot(x,f(x),label='real')
    plt.plot(x,p1(x),label='even')
    plt.plot(x,p2(x),label='chev')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend(loc='best')

def plotError(n):
    even,chev=C5(n)
    x= np.arange(-1,1,0.01)
    function = f(x)
    errorE = function - even(x)
    errorC = function - chev(x)
    plt.figure()
    plt.title('Error of degree ' + str(n))
    plt.plot(x,errorE,label='even')
    plt.plot(x,errorC,label='chev')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend(loc='best')

plotError(10)
plotError(20)
plotC5(10)
plotC5(20)
plt.show()
