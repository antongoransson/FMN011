#-*- coding: utf-8 -
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d,PPoly
import numpy.polynomial.polynomial as poly

def plot():
    x=np.array([1994,1995,1996,1997,1998,1999,2000,2001,2002,2003])
    x1 =np.linspace(1990,2012,num=1000)
    y=np.array([67.052,68.008,69.803,72.024,73.400,72.063,74.669,74.487,74.065,76.777])*1e6

    #x=np.array([1920 ,1930, 1940, 1950, 1960, 1970, 1980, 1990])
    #y=np.array([106.5, 123.1, 132.1, 152.3, 180.7, 205.0, 227.2, 249.5])

    coeffs = poly.polyfit(x, y, 9)
    #coeffs = coeffs[::-1]
    p = np.poly1d(coeffs)
    p1= poly.polyval(x1,p)
    print(coeffs)
    plt.plot(x,y,'o',x1,p1,'-')#,x,y1,'--')#,x,y1,'--')
    plt.text(1997,2.3e8,'Oil production 2010: '+ str(poly.polyval(2010,coeffs)))
    plt.show()

plot()
