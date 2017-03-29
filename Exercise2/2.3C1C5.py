#-*- coding: utf-8 -
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from numpy import linalg as lin

def f(n):
    A = np.zeros((n,n))
    for i in range (n):
        for j in range(n):
            A[i][j]=5/(i+1+2*(j+1)-1)
    x= np.ones(n)
    b= A@(x)
    Ainv = lin.inv(A)
    sol = lin.solve(A,b)
    relRes= lin.norm(sol-x,np.inf)/lin.norm(x,np.inf)
    condNbr = lin.norm(A,np.inf)*lin.norm(Ainv,np.inf)
    relErr= condNbr*relRes
    print("################## n=",n,"#####################")
    print("################## CONDITION NUMBER ##################")
    print(condNbr)
    print("################## SOLUTION MATRIX ##################")
    print(sol)
    print("################## RELATIVE ERROR ##################")
    print(relErr*100 , "%")
    print()
for i in range(6,16):
    f(i)
