##Decaimiento 
from numpy import *
from matplotlib.pyplot import *

T8=[]
H8=[]
T5=[]
H5=[]
Tt=[]
Ht=[]
Tk=[]
Hk=[]
h8o= 1.32e-15/1e-15
t8=2.02641822e+17
h5o=9.392e-15/1e-15
t5=3.191e16
hto=1.26816e-15/1e-15
tt=6.3725e17
hko=1.05e-14/1e-15
tk=5.674e16
to=1.413716694115407e+17 #4.5e9yr
t=linspace(0,to,1000)

h8= h8o*e**(-t/t8)
H8=append(H8,h8)
T8=append(T8,t)

h5= h5o*e**(-t/t5)
H5=append(H5,h5)
T5=append(T5,t)

ht= hto*e**(-t/tt)
Ht=append(Ht,ht)
Tt=append(Tt,t)

hk= hko*e**(-t/tk)
Hk=append(Hk,hk)
Tk=append(Tk,t)


figure()
plot(T8,H8,color="blue",label="U-238")
plot(T5,H5,color="red",label="U-235")
plot(Tt,Ht,color="green",label="Th-232")
plot(Tk,Hk,color="black",label="K-40")
xlabel("t(s)")
ylabel("h(w/g)e-15")
legend()
show()

