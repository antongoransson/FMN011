#-*- coding: utf-8 -
import math
import numpy as np

def theorem1_6(f,x):
    for i in range(0,1000):
        x = f(x)
    print(x)


def f1(x):
    return math.cos(x)
def f2(x):
    return math.cos(x)**(2)

theorem1_6(f2,1)
