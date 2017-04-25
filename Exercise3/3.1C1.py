#-*- coding: utf-8 -
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline
import numpy.polynomial.polynomial as poly





def plot():
    x1= np.array([1960,1970,1990,2000])
    x2= np.array([1960,1970,1990,2000,2010])
    y1 = np.array([3039585530,3707475887,5281653820,6079603571])
    y2 = np.array([3039585530,3707475887,5281653820,6079603571,6895889000])
    z = poly.polyfit(x2, y2, 2)
    p= poly.polyval(x2,z)
    #z = poly.polyfit(x2, y2, 2)
    #p= poly.polyval(z)
    f = interp1d(x1, y1, kind='cubic')
    f = CubicSpline(x1, y1)
    xNew = np.linspace(1960,2010,num=1000)
    plt.plot(x2,y2,'o',x1,f(x1),'-',x2,p,'--')
#    plt.grid(True, which='both')
    val1= float(f(1980))
    val2 = poly.polyval(1980,z)
    spline = 'Cubic spline: (' + str(1980)+ ',' + str(round(val1,0)) +')'
    pol = 'Quad pol: (' + str(1980)+ ', ' + str(round(val2,0)) + ')'
    plt.text(1955,6895889000,spline)
    plt.text(1955,6695889000,pol)
    plt.text(1955,6495889000,'Real value: '+ str(4452584592))
    #votes = 'Votes/change %='+str(nbrOfVotes)
#    plt.text(3,30,votes)
    plt.axhline(y=3e9, color='k')
    plt.axvline(x=1950, color='k')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.show()
plot()
