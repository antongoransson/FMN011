#-*- coding: utf-8 -
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as colors
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import mpl_toolkits.mplot3d as a3
import mpl_toolkits.mplot3d.art3d as art


def geval(l,b,d):
    L=np.zeros(6)
    L.fill(l)
    p = getP(L,15,1)
    h= getH(L,p)
    x = getXPCord(b,d,p)
    y = getYPCord(b,d,p)

def getP(L,b,d):
    P = np.zeros(3)
    for i in range(3):
        P[i]= (1/(2*b))*(b**(2) + L[2*i]**(2)-L[2*i+1]**(2))
    return P

def getH(L,P):
    h = np.zeros(3)
    for i in range(3):
        h[i]= np.sqrt(L[2*i]**(2)-P[i]**2)
    return h

def getLegCords(xt,yt,zt,bx,by,bz):
    lx = np.zeros((6,2))
    ly = np.zeros((6,2))
    lz = np.zeros((6,2))
    for i in range(2):
        lx[i] = np.array([bx[i],xt[0]])
        ly[i] = np.array([by[i],yt[0]])
        lz[i] = np.array([bz[i],zt[0]])
    for i in range(2,4):
        lx[i] = np.array([bx[i],xt[1]])
        ly[i] = np.array([by[i],yt[1]])
        lz[i] = np.array([bz[i],zt[1]])
    for i in range(4,6):
        lx[i] = np.array([bx[i],xt[2]])
        ly[i] = np.array([by[i],yt[2]])
        lz[i] = np.array([bz[i],zt[2]])
    return lx,ly,lz

def getXPCord(b,d,P):
    x = np.zeros(3)
    x[0] = (np.sqrt(3)/6)*(2*b+d-3*P[0])
    x[1] = -(np.sqrt(3)/6)*(b+2*d)
    x[2] = -(np.sqrt(3)/6)*(b-d-3*P[2])
    return x

def getYPCord(b,d,p):
    y = np.zeros(3)
    y[0] = 0.5*(d+p[0])
    y[1] = 0.5*(b-2*p[1])
    y[2] = -0.5*(b+d-p[2])
    return y

def getYTCord(xt,xp,yp):
    yt = np.zeros(3)
    yt[0] = np.sqrt(3)*xt[0] - (np.sqrt(3)*xp[0] - yp[0])
    yt[1] = yp[1]
    yt[2] = -np.sqrt(3)*xt[2]+ np.sqrt(3)*xp[2] + yp[2]
    return yt

def getZTCord(h,xt,xp):
    zt = np.zeros(3)
    zt[0]= np.sqrt(h[0]**(2)-4*(xt[0]-xp[0])**(2))
    zt[1]= np.sqrt(h[1]**(2)-4*(xt[1]-xp[1])**(2))
    zt[2]= np.sqrt(h[2]**(2)-4*(xt[2]-xp[2])**(2))
    return zt

def getMinLegLength(b,d):
    return b/2

def getBaseCordsX(b,d):
    bx= np.zeros(6)
    bx[0] = np.sqrt(3)*(2*b+d)/6.0
    bx[1] = -np.sqrt(3)*(b-d)/6.0
    bx[2] = -np.sqrt(3)*(b+2*d)/6.0
    bx[3] = -np.sqrt(3)*(b+2*d)/6.0
    bx[4] = -np.sqrt(3)*(b-d)/6.0
    bx[5] = np.sqrt(3)*(2*b+d)/6.0
    return bx

def getBaseCordsY(b,d):
    by= np.zeros(6)
    by[0] = d/2.0
    by[1] = (b+d)/2.0
    by[2] = b/2.0
    by[3] = -b/2.0
    by[4] = -(b+d)/2.0
    by[5] = -d/2.0
    return by

def stf(x,*data):
    a,b,d,L,p,h,xp,yp = data
    xt1=x[0]
    xt2=x[1]
    xt3=x[2]
    print(xt1,xt2,xt3)
    F= np.zeros(3)
    F[0]= a**2+ 2*xt1*xt2-2*xt1*(xp[0]+np.sqrt(3)*(yp[0]-yp[1]))-2*xp[1]*xt2-((np.sqrt(3)*xp[0]-yp[0]+yp[1])**(2)+h[0]**(2)+h[1]**(2)-4*xp[0]**(2)-xp[1]**(2))+ 2*np.sqrt((h[0]**(2)-4*(xt1-xp[0])**(2))*(h[1]**(2)-(xt2-xp[1])**(2)))
    F[1]= a**(2)-4*xt1*xt3-2*xt1*(xp[0]-3*xp[2]+np.sqrt(3)*(yp[0]-yp[2]))-2*xt3*(-3*xp[0]+xp[2]+np.sqrt(3)*(yp[0]-yp[2])) -((np.sqrt(3)*(xp[0]+xp[2])-yp[0]+yp[2])**(2)+(h[0]**(2)+h[2]**(2))-4*xp[0]**(2)-4*xp[2]**(2))+2*np.sqrt((h[0]**(2)-4*(xt1-xp[0])**(2))*(h[2]**(2)-4*(xt3-xp[2])**(2)))
    F[2]= a**(2) + 2*xt2*xt3-2*xt3*(xp[2]+np.sqrt(3)*(yp[1]-yp[2]))-2*xp[1]*xt2-((np.sqrt(3)*xp[2]-yp[1]+yp[2])**(2)+(h[1]**(2)+h[2]**(2))-xp[1]**(2)-4*xp[2]**(2))+ 2*np.sqrt((h[1]**(2)-(xt2-xp[1])**(2))*(h[2]**(2)-4*(xt3-xp[2])**(2)))
    return F


def plotCurve(x,y):
    x = np.linspace(-10,10,num=1000)
    fig, ax = plt.subplots()
    ax.plot(x,y)
    #ax.set_aspect('equal')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.show()

def task1():
    print(getMinLegLength(15,1))
    geval(8,15,1)

def task2():
    a=10
    b=15
    d=1
    L = np.zeros(6)
    L.fill(11.5)
    p = getP(L,b,d)
    h= getH(L,p)
    xp = getXPCord(b,d,p)
    yp = getYPCord(b,d,p)
    x0 = np.array([4,-3,4])
    data = a,b,d ,L,p,h,xp,yp
    x = fsolve(stf,x0,data)
    print(x)
    print (stf(x,*data))
def task3():
    a=10
    b=15
    d=1
    L = np.zeros(6)
    L.fill(11.5)
    p = getP(L,b,d)
    h= getH(L,p)
    xp = getXPCord(b,d,p)
    yp = getYPCord(b,d,p)
    x0 = xp
    data = a,b,d ,L,p,h,xp,yp
    x = fsolve(stf,x0,data)
    print(x)
    print(stf(x,*data))

def task5(L):
    a=10
    b=15
    d=1
    L = L
#    L= np.array([15,15,8,8,8,8])
    p = getP(L,b,d)
    h= getH(L,p)
    print(h)
    xp = getXPCord(b,d,p)
    yp = getYPCord(b,d,p)
    x0 = np.array([7.5,-5,2.3])
#    print(x0)
    data = a,b,d,L,p,h,xp,yp
    xt = fsolve(stf,x0,data)
    yt = getYTCord(xt,xp,yp)
    zt = getZTCord(h,xt,xp)
    bx = getBaseCordsX(b,d)
    by = getBaseCordsY(b,d)
    bz = np.zeros(6)
    print(xp,xt)
    lx,ly,lz= getLegCords(xt,yt,zt,bx,by,bz)
    data= xt,yt,zt,bx,by,bz,lx,ly,lz
    drawFigure(*data)

def drawFigure(*data):
    xt,yt,zt,bx,by,bz,lx,ly,lz= data
    fig = plt.figure()
    ax = Axes3D(fig)
    top = ax.plot_trisurf(xt,yt,zt,color='cyan')
    base= ax.plot_trisurf(bx,by,bz,color='red')
    for i in range(6): #Adds the legs
         ax.add_collection3d(ax.plot_wireframe(lx[i],ly[i],lz[i],linewidths=7,colors='gray'))
    ax.add_collection3d(top)
    ax.add_collection3d(base)
    ax.auto_scale_xyz([-10, 10], [-13, 13], [0, 15])


#task1()
task3()
L = np.zeros(6)
L.fill(15)
#task5(L)
L=([8,15,8,15,8,15])
#task5(L)
L= np.array([15,15,8,8,8,8])
#task5(L)
L.fill(8)
#task5(L)
#plt.show()
