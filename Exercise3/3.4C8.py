#-*- coding: utf-8 -
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d,PPoly
import numpy.polynomial.polynomial as poly
from numpy.linalg import *


def exerciseC8(d):
    x= np.linspace(2,4,num=11)
    y=np.zeros([len(x)])
    A=np.matrix(np.ones([len(x),d+1]))
    for i in range(len(x)):
        for j in range(0,d+1):
            y[i]=y[i]+x[i]**j
            A[i,j]=x[i]**j
    y=np.matrix(y)
    q,r= qr(A)
#    print("###### CONDITION NUMBER######")
#    print("    ",cond(q*r*(q*r).T,2))
    b=q.T*y.T;
    c=solve(r,b)
    print(c)

exerciseC8(5)
exerciseC8(6)
exerciseC8(8)
