#-*- coding: utf-8 -
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import *


def func(d):
    x= np.linspace(2,4,num=11)
    y=np.zeros([len(x)])
    A=np.matrix(np.ones([len(x),d+1]))
    for i in range(len(x)):
        for j in range(0,d+1):
            y[i]=y[i]+x[i]**j
            A[i,j]=x[i]**j
    b=np.matrix(y).T
    #np.set_printoptions(precision=5,suppress=True)
    A_c = A.T*A
    c=solve(A.T*A,A.T*b)
    print("######  C      ######")
    print(c)
    print("###### CONDITION NUMBER######")
    print("    ",cond(A.T*A,2))
    print("_________________________________________________________________ ")
def exercise4_1C9():
    func(5)
    func(6)
    func(8)

exercise4_1C9()
