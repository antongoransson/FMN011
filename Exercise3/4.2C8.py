#-*- coding: utf-8 -
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())
def func(x, a, b, c):
    return a * np.exp(b * x) + c

def exerciseC8():
    x = np.arange(1961,2011,1)
    x1 = x-1961
    y= np.array([320.58,321.01,322.25,322.24,322.16,324.01,325.00,325.57,327.34,328.07,328.92,330.07,332.48,333.09,333.97,334.87,336.75,338.01,339.47,341.46,342.91,
    344.14,345.75,347.43,348.93,350.21,351.84,354.22,355.67,357.16,359.34,359.66,360.28,361.68,363.79,365.41,366.80,369.30,371.00,371.82,374.02,375.55,378.35,380.61,382.24,384.94,386.43,388.49,390.18,393.22]) -279
    popt, pcov = curve_fit(func, x1, y,p0=(2, 0.01,2))
    f = func(x1, *popt)
    rmse_val = rmse(y,f)
    plt.plot(x,y,'o',label='data')
    plt.plot(x, f,label='exp fit')
    plt.legend(loc='best')
    plt.text(1970,100,"rms error is: " + str(rmse_val))
    plt.show()

exerciseC8()
