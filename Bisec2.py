# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import math 

# <codecell>

def biseccion(f,a,b,pres):
    
    if f(a)*f(b)>0.0:
         print "No hay raiz en el intervalo dado"
          
    iteraciones=math.log(1.0/pres)/math.log(2)
    N=int(iteraciones)
    
    for i in xrange(1,N):
        pm=(a+b)/2.0
        
        if f(pm)*f(a)<0.0:
            b=pm
        if f(pm)*f(b)<0.0:
            a=pm
            
    return pm    
    

# <codecell>

def cos(x):
    cos=np.cos(x)
    return cos

# <codecell>

print biseccion(cos,2,3,0.000000001)

# <codecell>


