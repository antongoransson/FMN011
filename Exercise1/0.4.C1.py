 #-*- coding: utf-8 -
import math
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

##VEKTOR LÖSNING UTAN FORLOOP
x2 = np.logspace(-1,-14, num=14)
a2 = (1- 1/(np.cos(x2)))/ (np.tan(x2)**(2))
a3 = -1 / (1+1/np.cos(x2))
b2 =(1-(1-x2)**(3))/x2
b3 =3-3*x2+ x2**(2)
print("################## EKVATION 1 ORIGINAL ######################")
print(a2)
print("")
print("################## EKVATION 1 FIXAD ######################")
print(a3)
print("")
print("################## EKVATION 2 ORIGINAL ######################")
print(b2)
print("")
print("################## EKVATION 2 FIXAD ######################")
print(b3)
print("")
