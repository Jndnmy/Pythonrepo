# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:20:00 2021

@author: Jason
"""
import sys
import matplotlib
import numpy
import noise
#def main:

if len(sys.argv) > 1:
	octaves = int(sys.argv[1])
else:
	octaves = 1

base = 0
min = max = 0

#Array = numpy.array([[0,2,1],[1,1,1],[2,2,1],[1,2,1]])
Array=numpy.random.randint(0,3,(1000,1000))#base case, true random
fig = matplotlib.pyplot.figure()  
cmap = matplotlib.colors.ListedColormap(['darkolivegreen','khaki','saddlebrown'])#colours used

for i in range (1000):
    for j in range (1000):
        x = float(i) * 3 / 3 - 0.5 * 3
        y=noise.pnoise1(x + 0,z, 100)
        print(y)
        if y > 0:
            y=1
        if y < 0:
            y=2
        
        Array[i,j] = y;
ax1= fig.add_subplot()
ax1.imshow(Array, interpolation='nearest',cmap=cmap)
 
#main()