#!/usr/bin/python

def f(x):
    r1=x-np.cos(x)
    return r1

def df(x):
    r2=1+np.cos(x)
    return r2
    
def nr(f,df,pin,N):
    p=pin
    for i in xrange(0,N):
        p=p-(f(p)/df(p))
        print p
    return p
