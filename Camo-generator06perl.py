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
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
start = time.process_time()
sizex= 100
sizey=100
#Array = numpy.array([[0,2,1],[1,1,1],[2,2,1],[1,2,1]])
Array=numpy.empty((sizex,sizey),dtype= int)#base case, true random
fig = matplotlib.pyplot.figure()  
cmap = matplotlib.colors.ListedColormap(['darkolivegreen','khaki','saddlebrown'])#colours used
Array2= numpy.empty((sizex,sizey),dtype= float)
'Rewrite to loop multiple times and overlap the khaki range in a random colour each time'
z =(randrange(9000))
for i in range (sizex):
    print(i)
    for j in range (sizey):
        x = float(i) * 0.02
        y = float(j) * 0.02
        a=noise.pnoise3(x + 0,y+0,z, 4)
        print(a)
       
        if a > 0.3:
            count1 +=1
        elif a > 0.2:
            count2 +=1
        elif a < 0:
            count3 +=1
        elif a < 0.1:
            count4 +=1
        else:
            count5 +=1
        if z == 2:
            z= -0.2
        if z == 1:
            z= 0.2
        print(z)
       # a = a+z
        Array2[i,j] = a;
       # if a > 0.1:
        #    a=2
        if a > 0:
            a=1
        #if a < -0.1:
         #   a=1
        elif a < 0.0:
            a=2

        
        Array[i,j] = a;


for i in Array2:
    for j in i:
        print(j , end=" ")

print("> .2 ",count1)
print("> .1 ",count2)
print("< .2 ",count3)
print("> .1 ",count4)
print("else" ,count5)
ax1= fig.add_subplot()
ax1.imshow(Array, interpolation='nearest',cmap=cmap)
#elapsed = time.process_time- start
#print("time tkaen: ",time.elapsed)
#main()