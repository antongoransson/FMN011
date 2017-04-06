#-*- coding: utf-8 -
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from numpy.linalg import *

def f(n):
    A = np.matrix(np.zeros((n,n)))
    for i in range (n):
        for j in range(n):
            A[i,j]=5/(i+1+2*(j+1)-1)
    x= np.matrix(np.ones(n)).T
    b= A*x
    Ainv = inv(A)
    sol = solve(A,b)
    forwardErr= norm(x-sol,np.inf)/norm(x,np.inf)
    condNbr = norm(A,np.inf)*norm(Ainv,np.inf)
    backWardErr = norm(b-A*sol,np.inf)/norm(b,np.inf)
    emf = forwardErr/backWardErr
    print("#####################      n=",n,"      #####################")
    print("##################### CONDITION NUMBER #####################")
    print("                    ",condNbr)
    print("##################### SOLUTION MATRIX  #####################")
    #print(sol)
    print("#####################  Forward ERROR  #####################")
    print("                    ",forwardErr )
    print("#####################  Error Magnification  ###################")
    print("                    ",emf )
    print("_________________________________________________________________ ")
for i in range(6,7):
    f(6)
    f(10)
