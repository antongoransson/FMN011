 #-*- coding: utf-8 -
import math
import matplotlib.pyplot as plt

import numpy as np
##VEKTORLÖSNING
x1=[];
for i in range (1,15):
 x1.append(10**(-i))

a1=[]
for i in range(0,14):
    a1.append((1- 1/(math.cos(x1[i])))/ (math.tan(x1[i])**(2)))
b =[]
for i in range(0,14):
    b.append( ((1-(1-x1[i])**(3)))/x1[i])


x2 = np.logspace(-1,-14, num=14)
a2 = (1- 1/(np.cos(x2)))/ (np.tan(x2)**(2))
a3 = (np.cos(x2)**2 - np.cos(x2))/ np.sin(x2)**(2)
b2 =(1-(1-x2)**(3))/x2
b3 = (10**(14)*x3**(2)+3*x2*10**(14)-3*x2**(2)*10**(14))*10**(-14)
print(b2)
print(b3)
