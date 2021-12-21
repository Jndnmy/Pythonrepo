# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:20:00 2021

@author: Jason
"""

import matplotlib
import numpy as np
import noise
import time
from random import randrange
import pandas as pd

def segments():

    sizex= 400
    sizey = 400
    Array=np.zeros((sizex,sizey),dtype= int)
    segments= np.array([np.array([[4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], 
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                                  [4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]), 
                       
                        np.array([[4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
                                  [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4]]),
                        
                        np.array([[4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                            ])
    
  #  print(segments[2].shape)
    for cycle in range (9000):
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
    for resolution in range (60):    
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
    sizex=400
    sizey=400
    for i in range(sizex):
        for j in range(sizey):
            colours[Array[i,j]] +=1
    
    
   # print("Olive: ",colours[0])
   # print("Khaki: ",colours[1])
   # print("brown: ",colours[2])
   # print("total:",colours[0] + colours[1] + colours[2])
    return colours

def main():
  Test = []
  Test.append(["Errors","Ratio Green","Ratio Brown","Ratio Khaki","Time"])
  repeats = 1
  print("Enter no. repeats")
  repeats = int(input())
  print()
  print("Enter desired algorthim")
  print("1 - Perlin noise")
  print("2 - Cellular automata")
  print("3 - Prefabs")
  procgen = int(input())
  for i in range(repeats):
    error = 0
    start = time.time()
   
    #base case, true random
    fig = matplotlib.pyplot.figure()  
    cmap = matplotlib.colors.ListedColormap(['darkolivegreen','khaki','saddlebrown'])#colours used
    if procgen == 1:
        Array = perlinCamo()
    if procgen == 4:
        Array = smoothing()
    if procgen == 2:
        Array = smoothing2()
    if procgen== 3:
        Array = segments()
    colour = comparecolours(Array)
    end = time.time()
    elapsed = end- start
    for k in range(400):
       for j in range(400):
        adjArray = adjacencies(Array, k, j, 400, 400)
        if adjArray[Array[k,j]] < 1:
            error +=1
    Test.append([error,colour[0]/160000,colour[1]/160000,colour[2]/160000,elapsed])
    print(i)

    
    ax1= fig.add_subplot()
    ax1.imshow(Array, interpolation='nearest',cmap=cmap)
  testarray = np.array(Test)

  print(pd.DataFrame(testarray))
   
  timeT = 0
  timeAv = 0
  timeM = 0
  timem=99999
  
  greenT=0
  greenM=0
  greenm=99999
  greenAv=0
  
  khakiT=0
  khakiM=0
  khakim=99999
  khakiAv=0
  
  brownT=0
  brownM=0
  brownm=9999
  brownAv=0
  
  errorT=0
  errorM=0
  errorm=99999
  errorAv=0
  
  m = 1
  for l in range(i + 1):
     m = l + 1
 #    print(m)
     errors = Test[m][0]
     errorT += errors
  #   print(errors)
     if errors > errorM:
          errorM = errors
     if errors < errorm:
          errorm = errors
      
     green = Test[m][1]
     greenT += green
     if green > greenM:
          greenM = green
     if green < greenm:
          greenm = green
    
     khaki = Test[m][2]
     khakiT += khaki
     if khaki > khakiM:
          khakiM = khaki
     if khaki < khakim:
          khakim = khaki
     
     brown = Test[m][3]
     brownT += brown
     if brown > brownM:
         brownM = brown
     if brown < brownm:
          brownm = brown
     
     timer = Test[m][4]
     timeT += timer
     if timer > timeM:
          timeM = timer
     if timer < timem:
          timem = timer
          
  errorAv = errorT/m
  khakiAv = khakiT/m
  greenAv = greenT/m
  brownAv = brownT/m
  timeAv = timeT/m
  print("Errors: total =",errorT,"Average =",errorAv," Maximum =",errorM," Minimum =",errorm) 
  print("Time: total =",timeT,"Average =",timeAv," Maximum =",timeM," Minimum =",timem) 
  print("Khaki: Average =", khakiAv," Maximum =",khakiM," Minimum =",khakim)
  print("green: Average =",greenAv," Maximum =", greenM," Minimum =",greenm)
  print("brown: Average =",brownAv," Maximum =", brownM," Minimum =",brownm)

main()
