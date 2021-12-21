# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:05:52 2021

@author: Jason
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 13:05:04 2021

@author: Jason
"""

import matplotlib
import numpy as np
import noise
import time
from random import randrange
##generting hills and steps?
##or just pathways +fountain?

#diagonals dont count
procgen = 2
def placefountain(Array, x, y):
    
    return Array

def smoothing():
    sizex= 40
    sizey= 40
    fountainx = 32
    fountainy = 32
    Array = np.random.randint(2, size=(sizex,sizey))
    Array2 = np.zeros((sizex,sizey), dtype=int)
   # for i in range (sizex):
     #       for j in range(sizey):
    #            if Array[i,j] >1:
    #                Array[i,j]=0
#    Array = np.ones((sizex,sizey))
 #   Array = placefountain(Array, fountainx, fountainy)
    for resolution in range (98):    
        for i in range (sizex):
            for j in range(sizey):
               paths = adjacencies(Array, i, j, sizex, sizey)
               #If Mode = max then do random
               #not guarunteed to swap
               #need precurser if for fountain
               #try with diagonal counting as path unless border
               #with above try allowing 2 3 or 4
               #try to implement multithreading
               #try with ruleset if a cell has 1 neighbor it comes alive
               #if a cell has more than one neighbors it dies
               #leave a shadow where  cells have been
               
               if paths == 3:
                    Array[i,j] = 1
               else:
                    Array[i,j]= 0
      
    return Array
#def cellular automata 2
def adjacencies(Array,x,y,sizex,sizey):#Write adjacency 2 where Replace if with if elseif for speed'
   path = 0
    #if bordering paths = 2, become path
    #if greater become grass
    #if smaller become grass
    #border counts as path
   if x == 0 and y == 0 or x == sizex-1 and y == sizey -1 or x == 0 and y == sizey -1 or y == 0 and x == sizex -1:
     path = 0
   else:
    if x+1 >= sizex:  
         path = path+1  
    elif Array[x+1,y] == 1:
        path = path+1
    if x-1 <= sizex:  
         path = path+1 
    elif Array[x-1,y] == 1:
        path = path+1
    if y+1 >= sizey:  
         path = path+1    
    elif Array[x,y+1] == 1:
        path = path+1
    if y-1 <= sizey:  
         path = path+1          
    elif Array[x,y-1] == 1:
        path = path+1
   return path

def comparecolours(Array):
    colours = np.array([0,0,0])
    #make it so size x and size y are setin main
    sizex=20
    sizey=20
    for i in range(sizex):
        for j in range(sizey):
            colours[Array[i,j]] +=1
    
    print("Olive: ",colours[0])
    print("Khaki: ",colours[1])
    print("brown: ",colours[2])
    print("total:",colours[0] + colours[1] + colours[2])
    
def main():

    start = time.time()
   
    #base case, true random
    fig = matplotlib.pyplot.figure()  
    cmap = matplotlib.colors.ListedColormap(['lightgreen','darkgray','grey'])#colours used
    if procgen == 1:
        Array = perlinCamo()
    if procgen == 2:
        Array = smoothing()
    if procgen == 3:
        Array = smoothing2()
    if procgen== 4:
        Array = segments()
   # comparecolours(Array)
    
    #for i in Array:
      # for j in i:
       #     print(j , end=" ")
    
    
    ax1= fig.add_subplot()
    ax1.imshow(Array, interpolation='nearest',cmap=cmap)
    end = time.time()
    elapsed = end- start
    print("time taken: ", elapsed)
    
main()