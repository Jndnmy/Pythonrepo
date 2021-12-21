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

#start = time.process_time()
sizex= 400
sizey=400
#Array = numpy.array([[0,2,1],[1,1,1],[2,2,1],[1,2,1]])
Array=numpy.zeros((sizex,sizey),dtype= int)#base case, true random
fig = matplotlib.pyplot.figure()  
cmap = matplotlib.colors.ListedColormap(['darkolivegreen','khaki','saddlebrown'])#colours used


for cycle in range (6):
    z =(randrange(50000))
    colour = cycle % 3

    for i in range (sizex):
       
        for j in range (sizey):
            x = float(i) * 0.08
            y = float(j) * 0.08
            a=noise.pnoise3(x + 0,y+0,z, 1)
            if a > 0.08:
                Array[i,j] = colour;

for i in Array:
    for j in i:
        print(j , end=" ")


ax1= fig.add_subplot()
ax1.imshow(Array, interpolation='nearest',cmap=cmap)
#elapsed = time.process_time- start
#print("time tkaen: ",time.elapsed)
#main()