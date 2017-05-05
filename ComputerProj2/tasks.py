#-*- coding: utf-8 -
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.interpolate as cs
from scipy.optimize import fsolve


def tasks():
    t = np.array([ 70, 70, 55, 22, 13, 10, 10])
    z = np.array([ 0, 0.5, 1, 1.5, 2, 2.5, 3])*100
    p = cs.CubicSpline(z,t,bc_type='clamped')
    x = np.linspace(0,3,num=100)*100
    print(x)
    root= fsolve(p,100,args=2)
#    plt.plot(z,t,'o',label='Data')
    plt.plot(x,-0.01*p(x,1),label='Heat flux')
#    plt.plot(x,p(x),'r',label='S') #Plots the interpolated curve
#    plt.plot(x,p(x,1),label='S\'',color='b') # Plots the derivate
    plt.plot(x,p(x,2),label='S\'\'') #Plots the second derivate
    plt.axvline(x=root, linestyle='dashed',color='k',label='Thermical depth') #Plots a dashed line at the thermical depth
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.plot(root,0,'o',color='k')
    plt.text(50,0.015,str(100*100*-0.01*p(root,1)))
    plt.annotate('Thermical depth = '+str(round(root[0],2))+ 'm', xy=(root,0 ), xytext=(1.8,-100),arrowprops=dict(facecolor='black', shrink=0.05))
    plt.legend(loc='best')
    plt.show()

tasks()
