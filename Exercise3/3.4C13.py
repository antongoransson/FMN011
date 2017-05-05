#-*- coding: utf-8 -
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d,PPoly
import numpy.polynomial.polynomial as poly
from scipy.interpolate import interp1d, CubicSpline

def plot():
    x=np.array([1994,1995,1996,1997,1998,1999,2000,2001,2002,2003])
    x1 =np.linspace(1990,2012,num=1000)
    y=np.array([67.052,68.008,69.803,72.024,73.400,72.063,74.669,74.487,74.065,76.777])*1e6
    notAknot = CubicSpline(x,y,bc_type='not-a-knot')
    #parabolic = CubicSpline(x,y,bc_type=((3,0.0),(3,0.0)))
    natural = CubicSpline(x,y,bc_type='natural')

    plt.plot(x,y,'o',label='data')
    plt.plot(x1,notAknot(x1),label='not-a-knot')
    plt.plot(x1,natural(x1),label='natural')#,x,y1,'--')#,x,y1,'--')
    #plt.text(1997,2.3e8,'Oil production 2010: '+ str(poly.polyval(2010,coeffs)))
    plt.axhline(y=0, color='k')
    plt.axvline(x=1990, color='k')
    plt.legend(loc='best')
    plt.show()

plot()
