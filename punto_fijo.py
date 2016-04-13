#!/usr/bin/python

import numpy as np


def g(x):
    value =x-(x*x-2)/(3.0)
    return value
    
def punto_fijo(f,p0,N):
    
    g = lambda x: x-f(x)
    
    for i in xrange(0,N):
        p1=g(p0)
        p0=p1
    return p0

pf(g,2,20)
        




