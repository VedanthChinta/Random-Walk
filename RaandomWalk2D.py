# -*- coding: utf-8 -*-
import numpy as np
import pylab
import random
n=10000
x=np.zeros(n)
y=np.zeros(n)
Directions=["North","South","West","East"]
for i in range(1,n):
    checkdir=random.choice(Directions)
    if checkdir=="North":
        x[i]=x[i-1]
        y[i]=y[i-1]+1
    elif checkdir=="South":
        x[i]=x[i-1]
        y[i]=y[i-1]+1
    elif checkdir=="West":
        x[i]=x[i-1]-1
        y[i]=y[i-1]
    elif checkdir=="East":
        x[i]=x[i-1]+1
        y[i]=y[i-1]
        
pylab.plot(x,y)
pylab.show()
    
        
