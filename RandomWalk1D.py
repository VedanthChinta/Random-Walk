# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import matplotlib.pyplot as plt
import numpy as np
import random
n=1000
x=np.zeros(n)
y=np.zeros(n)
Directions=["North","South"]
for i in range(1,n):
    CheckDir=random.choice(Directions)
    if CheckDir=="North":
        x[i]=x[i-1]+1
        y[i]=y[i-1]+1
            
    if CheckDir=="South":
        x[i]=x[i-1]+1
        y[i]=y[i-1]-1
    
plt.plot(x,y)
plt.show()

