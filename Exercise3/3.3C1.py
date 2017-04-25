#-*- coding: utf-8 -
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy.polynomial.polynomial as poly
import numpy.polynomial.chebyshev as chev


x1=np.linspace(0,np.pi/2,num=4)
x=np.linspace(-2,2,num=100)
f= np.sin(x)
f1= np.sin(x1)
coeffs = chev.chebfit(x1,f1,4)
p = chev.chebval(x,coeffs)
roots = chev.chebroots(coeffs)
print(roots)
plt.figure()
plt.plot(chev.chebval(x1,roots),roots,'o',x,f,'--',x,p,'-')#,x,y1,'--')
#plt.figure()
plt.plot(chev.chebval(x1,roots),roots,'o')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
#plt.text(1997,2.3e8,'Oil production 2010: '+ str(poly.polyval(2010,coeffs)))
plt.show()





#Program 3.3 Building a sin calculator key, attempt #1
#Approximates sin curve with degree 3 polynomial
# (Caution: do not use to build bridges,
# at least until we have discussed accuracy.)
#Input: x
#Output: approximation for sin(x)
function y=sin1(x)
#First calculate the interpolating polynomial and
# store coefficients
b=pi*(0:3)/6
yb=sin(b) # b holds base points
c=newtdd(b,yb,4)
#For each input x, move x to the fundamental domain and evaluate
# the interpolating polynomial
s=1 # Correct the sign of sin
x1=mod(x,2*pi)
if x1>pi
x1 = 2*pi-x1;
s = -1;
end
if x1 > pi/2
x1 = pi-x1;
end
y = s*nest(3,c,x1,b);
