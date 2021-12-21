# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:20:00 2021

@author: Jason
"""
#try cellular automata which generates a new map each time
import matplotlib
import numpy as np
import noise
import time
from random import randrange
procgen = 1

def segments():
    'Now increase the size by an oom lol. Liberal amounts of copy-pasting suggested'
    'larger shapes allows for more variation anyway'
    'displays horizontally, fixing causes crashes'
    
    sizex= 20
    sizey = 20
    Array=np.zeros((sizex,sizey),dtype= int)
    segments= np.array([np.array([[4,2,2,2,4], 
                                  [4,4,2,2,2],
                                  [4,4,2,2,2],
                                  [4,2,2,2,4],
                                  [2,2,2,2,4]]), 
                        np.array([[4,1,1,1,4], 
                                  [4,4,1,1,4]]),
                        np.array([[4,0,0,0,4], 
                                  [4,4,0,0,0],
                                  [4,4,0,0,0],
                                  [4,0,0,0,4],
                                  [0,0,0,0,4]]),
                            ])
    #print(segments[0].shape)
    for cycle in range (900):
        z = randrange (3)
        x = randrange (sizex)
        y = randrange(sizey)
        line = x
        length = segments[z].shape[0]
        width = segments[z].shape[1] 
     #   print(width)
      #  print(length)
        for i in range(length):
          for j in range(width):
              if segments[z][i,j] != 4:
                  Array[x,y] = segments[z][i,j]
             #     print("check")
              if x < sizex-1:
                  x +=1
          x = line  
          if y < sizey-1:
             y +=1
    return Array
        
        
def perlinCamo():
    sizex= 400
    sizey=400
    Array=np.zeros((sizex,sizey),dtype= int)
    for cycle in range (3):
            z =(randrange(50000))
            colour = cycle % 3
        
            for i in range (sizex):
               
                for j in range (sizey):
                    x = float(i) * 0.04
                    y = float(j) * 0.04
                    a=noise.pnoise3(x + 0,y+0,z, 1)
                    if a > 0.08:
                        Array[i,j] = colour;
    return Array

def adjacencies(Array,x,y,sizex,sizey):#Write adjacency 2 where Replace if with if elseif for speed'
    adjacent = np.array([0,0,0])
    if x+1 < sizex:
        adjacent[Array[x+1,y]] +=1
    if x > 0:
        adjacent[Array[x-1,y]] +=1
    if y+1 < sizey:
        adjacent[Array[x,y+1]] +=1
    if y > 0:
        adjacent[Array[x,y-1]] +=1
    if x+1 < sizex and y+1 < sizey:
        adjacent[Array[x+1,y+1]] +=1
    if x > 0 and y > 0:
        adjacent[Array[x-1,y-1]] +=1
    if x+1 < sizex and y > 0:
        adjacent[Array[x+1,y-1]] +=1
    if x > 0 and y+1 < sizey:
        adjacent[Array[x-1,y+1]] +=1
   # adjacent[Array[x,y]] +=1
    if adjacent[0] == adjacent[1] and adjacent[1] == adjacent[2]:
        l = (randrange(3))
        adjacent[l] -=1
    if adjacent[0] == adjacent [1]:
        l = (randrange(2))
        adjacent[l] -=1
    if adjacent[1] == adjacent [2]:
        l = (randrange(2))
        adjacent[l+1] -=1
    if adjacent[0] == adjacent[2]:
        l = (randrange(2))
        if l == 0:
            adjacent[0] -=1
        else:
            adjacent[2] -=1
  #  print(adjacent[0],adjacent[1],adjacent[2])
    return adjacent
        
    

       


      
def smoothing2():
    sizex= 400
    sizey= 400
    Array = np.random.randint(3, size=(sizex,sizey))
    Array2 = np.zeros((sizex,sizey), dtype=int)
    for resolution in range (90):    
        for i in range (sizex):
            for j in range(sizey):
               adjArray = adjacencies(Array, i, j, sizex, sizey)
               #If Mode = max then do random
               #not guarunteed to swap
               Array2[i,j] = np.argmax(adjArray)
        Array = Array2       
               
    return Array
def smoothing():
    sizex= 400
    sizey= 400
    Array = np.random.randint(3, size=(sizex,sizey))
    for resolution in range (60):    
        for i in range (sizex):
            for j in range(sizey):
               adjArray = adjacencies(Array, i, j, sizex, sizey)
               #If Mode = max then do random
               #not guarunteed to swap
               Array[i,j] = np.argmax(adjArray)
    return Array

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
    cmap = matplotlib.colors.ListedColormap(['darkolivegreen','khaki','saddlebrown'])#colours used
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
