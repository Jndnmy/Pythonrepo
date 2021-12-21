# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:20:00 2021

@author: Jason
"""

import matplotlib
import numpy
import noise
import time
from random import randrange

#def main:

start = time.process_time()
#Array = numpy.array([[0,2,1],[1,1,1],[2,2,1],[1,2,1]])
Array=numpy.random.randint(0,3,(30,200))#base case, true random
fig = matplotlib.pyplot.figure()  
cmap = matplotlib.colors.ListedColormap(['darkolivegreen','khaki','saddlebrown'])#colours used

for i in range (10):
    print(i)
    for j in range (10):
        x = float(i) * 3 / 3 - 0.5 * 3
        y = float(j) * 3/ 3 - 0.5 * 3
        a=noise.pnoise2(x + 0,y+0, 1)
        #print(a)
        z =(randrange(3))
       # if z == 2:
      #      z= -1
        #print(z)
       # a = a+z
       # if a > 0:
        #    a=1
        #if a < 0:
       #     a=2
        
        Array[i,j] = z;
ax1= fig.add_subplot()
ax1.imshow(Array, interpolation='nearest',cmap=cmap)
#elapsed = time.process_time- start
#print("time tkaen: ",time.elapsed)
#main()