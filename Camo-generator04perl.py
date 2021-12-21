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
Array=numpy.empty((250,250),dtype= int)#base case, true random
fig = matplotlib.pyplot.figure()  
cmap = matplotlib.colors.ListedColormap(['darkolivegreen','khaki','saddlebrown'])#colours used
Array2= numpy.empty((250,250),dtype= float)
for i in range (250):
    print(i)
    for j in range (250):
        x = float(i) * 0.05 / 3 * 3
        y = float(j) * 0.05 / 3 * 3
        a=noise.pnoise2(x + 0,y+0, 1)
        print(a)
        z =(randrange(3))
        if z == 2:
            z= -1
        print(z)
        a = a#+z
        Array2[i,j] = a;
       # if a > 0.1:
        #    a=2
        if a > 0.01:
            a=1
        #if a < -0.1:
         #   a=1
        if a < 0.01:
            a=2

        
        Array[i,j] = a;

for i in Array2:
    for j in i:
        print(j , end=" ")
ax1= fig.add_subplot()
ax1.imshow(Array, interpolation='nearest',cmap=cmap)
#elapsed = time.process_time- start
#print("time tkaen: ",time.elapsed)
#main()