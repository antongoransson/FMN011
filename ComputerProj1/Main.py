#-*- coding: utf-8 -
import math
import numpy as np
import matplotlib.pyplot as plt

def geval(l,b,d):
    L=np.zeros(6)
    L.fill(l)
    p = getP(L,15,1)
    h= getH(L,p)
    x = getXPCord(b,d,p)
    y = getYPCord(b,d,p)
    print(p,h,x,y)

def getP(L,b,d):
    P = np.zeros(3)
    for i in range(3):
        P[i]= (1/(2*b))*(b**(2) + L[2*i]**(2)-L[2*i+1]**(2))
    return P
##SQRT blir negativ för L=3
def getH(L,P):
    h = np.zeros(3)
    for i in range(3):
        h[i]= np.sqrt(L[2*i+1]**(2)-P[i]**2)
    return h

def getXPCord(b,d,P):
    x = np.zeros(3)
    x[0] =np.sqrt((3)/6)*(2*b+d-3*P[0])
    x[1] = -(np.sqrt(3)/6)*(b+2*d)
    x[2] = -(np.sqrt(3)/6)*(b-d-3*P[2])
    return x

def getYPCord(b,d,p):
    y = np.zeros(3)
    y[0] = 0.5*(d+p[0])
    y[1] = 0.5*(b-2*p[1])
    y[2] = -0.5*(b+d-p[2])
    return y

def getMinLegLength(b,d):
    return b/2

def Task1():
    print(getMinLegLength(15,1))
    geval(8,15,1)


def guessXT(a,b,d,xt,p,h,XP,YP):
    e1= a**(2) + 2*xt[0]*xt[1]-2*xt[0]*(xp[0]+np.sqrt(3)(*yp[0]-yp[1]))
     -2*xp[1]*xt[1]-((np.sqrt(3)*xp[0]-yp[0]+yp[1])**(2)+h[0]**(2)+h[1]**(2)-4*xp[0]**(2)-xp[1]**(2))
