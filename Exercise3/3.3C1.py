#-*- coding: utf-8 -
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy.polynomial.polynomial as poly
import numpy.polynomial.chebyshev as chev


nodes=np.arange(0,4)*np.pi/6
y= np.sin(nodes)
print(nodes)
x=np.linspace(-2,2,num=100)
f= np.sin(x)
coeffs= chev.chebfit(nodes,y,4)
p = chev.chebval(x,coeffs)
plt.plot(nodes,y,'o',x,f,x,p)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()
