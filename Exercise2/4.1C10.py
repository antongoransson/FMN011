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
    c1 = x_c.item(0)
    c2=x_c.item(1)
    return c1,c2

def plotA(b,x,c1,c2):
    x_c = np.linspace(-2,8,num=11)
    print(x_c)
    y=c2*x_c+c1
    nbrOfVotes = y[1]-y[0]
    print(nbrOfVotes)
    plt.plot(x,b,'o')
    plt.plot(x_c,y,'r')
    #plt.grid(True, which='both')
    votes = 'Votes/change %='+str(nbrOfVotes)
    plt.text(3,30,votes)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.xlabel('Vote change %')
    plt.ylabel('Incumbent vote change %')

def exercise4_1C10():
    b=np.matrix([44.6,57.8,49.9,61.3,49.6,61.8,49.0,44.7,59.2,53.9,46.5,54.7,50.3,51.2,45.7]).T
    x=np.array([1.49, 3.03, 0.57, 5.74, 3.51, 3.73, 2.98,-0.18, 6.23, 3.38, 2.15, 2.10, 3.93, 2.47,-0.41])
    A= np.matrix([x,x]).T
    for i in range(len(x)):
        A[i,0]=1
    c1,c2= normEquations(A,b,x)
    plotA(b,x,c1,c2)
    plt.show()
exercise4_1C10()
