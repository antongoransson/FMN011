#-*- coding: utf-8 -
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import *

def normEquations(A,b,x):
    b= b
    x =x
    A=A
    lstsqr = lstsq(A,b)
    x_c = lstsqr[0]
    res = b-A*x_c
    rmse = norm(res,2)/np.sqrt(len(x))
    c1 = x_c.item(0)
    c2=x_c.item(1)
    print ("C1=",c1,"   C2=", c2)
    print("RMSE=",rmse)
    return c1,c2, rmse

def plotA(b,x,c1,c2,rmse):
    x_c = np.linspace(0,1.11,num=1000)
    y=c2*x_c+c1
    plt.plot(x,b,'o')
    plt.plot(x_c,y,'r')
    #plt.grid(True, which='both')
    k = 'C1='+str(round(c1,3))
    m= 'C2='+str(round(c2,3))
    r = 'RMSE='+str(round(rmse,3))
    plt.text(0.7,7000,r)
    plt.text(0.7,7500,m)
    plt.text(0.7,8000,k)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.xlabel('Price')
    plt.ylabel('Sales')

def plotB(b,x,c1,c2):
    x_c = np.linspace(0,1.11,num=1000)
    y=(c2*x_c+c1)*(x_c-0.23)
    fig =plt.figure()
    plt.plot(x_c,y)
    m = np.amax(y)
    xMax = x_c[np.argmax(y)]
    plt.plot(xMax,m,'ro')
    cords = 'Max sales : ('+str(round(xMax,3))+';'+ str(round(m,3))+ ')'
    plt.annotate(cords, xy=(xMax,m ), xytext=(xMax-0.2, m+2000),
            arrowprops=dict(facecolor='black', shrink=0.05))
    #plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.ylim(-2000,7000)
    plt.xlabel('Price')
    plt.ylabel('Sales')

def exercise4_1():
    b= np.matrix([3980, 2200, 1850, 6100, 2100, 1700, 2000, 4200, 2440, 3300, 2300,6000,1190,1960,2760,4330,6960,4160,1990,2860,1920,2160]).T
    x =np.array([0.59,0.80,0.95,0.45,0.79,0.99,0.90,0.65,0.79,0.69,0.79,0.49,1.09,0.95,0.79,0.65,0.45,0.60,0.89,0.79,0.99,0.85])
    A= np.matrix([x,x]).T
    for i in range(len(x)):
        A[i,0]=1
    c1,c2,rmse = normEquations(A,b,x)
    plotA(b,x,c1,c2,rmse)
    plotB(b,x,c1,c2)
    plt.show()

exercise4_1()
