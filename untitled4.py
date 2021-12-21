# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 09:14:08 2021

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
procgen = 3
def placefountain(Array, x, y):

    return Array
def adjacencies2(Array,x,y,sizex,sizey):#Write adjacency 2 where Replace if with if elseif for speed'
    #if x,y = 2 right and up, and x,y = 1 left down

      if Array[x,y] == 1:
        #print('start')
        if x+1 >= sizex:
             Array=Array
             'print x+1 addednothing'
        elif Array[x+1,y] == 1 or Array[x+1,y] == 2:
            Array[x+1,y] = 3
            Array[x,y] = 3
         #   print('x+1 set to 3')
            if x-1>=0:
             if Array[x-1,y] != 3:
                 Array[x-1,y] = 1
          #       print('x-1 set')
                 if x-2>=0:
                     if Array[x-2,y] !=3:
                         Array[x-2,y] = 1
           #              print('x-2set')

        elif y+1 >= sizey:
             Array=Array
        elif Array[x,y+1] == 1 or Array[x,y+1] == 2:
            Array[x,y+1] = 3
            Array[x,y] = 3
            if y-1>=0:
             if Array[x,y-1] != 3:
                 Array[x,y-1] = 1
                 if y-2>=0:
                     if Array[x,y-2] !=3:
                         Array[x,y-2] = 1
      if Array[x,y] == 2:
        if x-1 < 0:
              Array=Array
        elif Array[x-1,y] == 2 or  Array[x-1,y] == 1:
            Array[x-1,y] = 3
            Array[x,y] = 3
            if x+1<sizex:
              if Array[x+1,y] != 3:
                  Array[x+1,y] = 2
                  if x+2<sizex:
                      if Array[x+2,y] !=3:
                          Array[x+2,y] = 2
        elif y-1 < 0:
              Array=Array
        elif Array[x,y-1] == 2 or Array[x,y-1] == 1:
            Array[x,y-1] =3
            Array[x,y] =3
            if y+1<sizey:
              if Array[x,y+1] != 3:
                  Array[x,y+1] = 2
                  if y+2<sizey:
                      if Array[x,y+2] !=3:
                          Array[x,y+2] = 2
      #elif Array[x,y] != 3:
      #     Array[x,y] =0
      return Array
def seed(Array,sizex,sizey):
    Array2 = Array
    print('seeding')
    for i in range(sizex):
            for j in range(sizey):
                if Array[i,j] != 0:
                    n = Array[i,j]
                    if adjacencies(Array, i, j, sizex, sizey) == 0:
                        z = randrange(4)
                        if z == 0 :
                            if i+1 <sizex:
                                Array2[i+1,j] = n
                        elif z == 1:
                            if i-1 >= 0:
                                Array2[i-1,j] = n
                        elif z == 2:
                            if j+1 < sizey:
                                Array2[i,j+1] = n
                        elif z == 3:
                            if j-1 >= 0:
                                Array2[i,j-1]=n
    Array = Array2
    return Array

def evaluate(Array,sizex,sizey):
    print ('evaluating')
    root = getRoot(Array,sizex,sizey)
    total = 0
    navigated = []
    previous = (0,0)
    count = 0
    if root[0] == 0 and root[1] == 0:
        return False
    print('evaluating2')
    for i in range(sizex):
        for j in range (sizey):
            if Array[i,j] != 0:
                total += 1
                if i + 1 < sizex:
                    if Array[i+1,j] !=0:
                        if j + 1 < sizey:
                          if Array[i,j+1] !=0 and Array[i,j] !=0:
                                #return False
                                a=1
    print('evaluating3')
    print(Array)
    navigated.append(countTree(Array,sizex,sizey, root[0], root[1], navigated,total,count,previous))
    print(len(set(navigated)))
    print(total)
    if len(set(navigated)) >= total:
        return True
    else:
        return False
   #list which contains unique tiles
   #int which keeps count of unique tiles  using touples
   #int which keeps count of total tiles touched

def countTree (Array,sizex,sizey, x,y,navigated,total,count,previous):
    current = (x,y)
    #automatically discard trees with [1,1
                                      #1,1]
    #print(current,' ',count)
    count +=1
    if count > total:
        return current
    if (x+1,y) != previous:
        if x+1 < sizex:
            if Array[x+1,y] != 0:
                navigated.append(countTree(Array,sizex,sizey,x+1,y,navigated,total,count,current))
    if (x-1,y) != previous:
        if x-1 >= 0:
            if Array[x-1,y] != 0:
                navigated.append(countTree(Array,sizex,sizey,x-1,y,navigated,total,count,current))
    if (x,y+1) != previous:
        if y+1 < sizey:
            if Array[x,y+1] != 0:
                if count > total:
                    navigated.append(countTree(Array,sizex,sizey,x,y+1,navigated,total,count,current))
    if (x,y-1) != previous:
        if y-1 >= 0:
            if Array[x,y-1] != 0:
                if count > total:
                    navigated.append(countTree(Array,sizex,sizey,x,y-1,navigated,total,count,current))
    return current
def getRoot(Array,sizex,sizey):
    for x in range (sizex):
        if Array[x,sizey-1] != 0:
            return [x,sizey-1]
        if Array[x,0] != 0:
            return [x,0]
    for y in range (sizey):
        if Array[sizex-1,y] !=0 :
            return[sizex-1,y]
        if Array[0,y] !=0:
            return[0,y]
    return [0,0]
def smoothing2():
    sizex= 20
    sizey= 20
    acceptable = False
    count =0
    while acceptable == False:
        Array = np.random.randint(120, size=(sizex,sizey))

        for i in range(sizex):
                for j in range(sizey):
                    if Array[i,j] >2:

                        Array[i,j] = 0
        Array = seed(Array, sizex,sizey)
        Array2 = np.zeros((sizex,sizey), dtype=int)
        #try creating cells, if cell has no neighbor create one neighbor randomly
        #rule =, if cell has a neighbor, delete neighbor, create 2 cells opposite direction of neighbor and delete self
        #create trail where cells were, if cell touches trail delete
        #seeding phase = random, after that deteministic
        for resolution in range (10):
            for i in range (sizex):
                for j in range(sizey):
                   Array2 = adjacencies2(Array, i, j, sizex, sizey)
                   #If Mode = max then do random
                   #not guarunteed to swap


            Array = Array2

        for i in range(sizex):
                for j in range(sizey):
                    if Array[i,j] != 0:

                        Array[i,j] = 1
        acceptable = evaluate(Array,sizex,sizey)
        count +=1
        print(count)
    print(Array2)
    print(Array)
    return Array

def pathadj (Array,x,y,sizex,sizey):
    path = 0
    if x+1 <= sizex:
         path = path+1
    elif Array(x+1,y) == 1:
        path = path+1
    if x-1 >= sizex:
         path = path+1
    elif Array(x-1,y) == 1:
        path = path+1
    if y+1 <= sizey:
         path = path+1
    elif Array(x,y+1) == 1:
        path = path+1
    if y-1 >= sizey:
         path = path+1
    elif Array(x,y-1) == 1:
        path = path+1

    return path
def adjacencies(Array,x,y,sizex,sizey):#Write adjacency 2 where Replace if with if elseif for speed'
   path = 0
    #if bordering paths = 2, become path
    #if greater become grass
    #if smaller become grass
    #border counts as path
  # print(x)
  # print(y)
   if x == 0 and y == 0 or x == sizex-1 and y == sizey -1 or x == 0 and y == sizey -1 or y == 0 and x == sizex -1:
     path = 0
   else:
    if x+1 >= sizex:
         path = path
    elif Array[x+1,y] == 1:
   #     print('x<size')
        path = path+1
    if x-1 <= 0:
         path = path
    elif Array[x-1,y] == 1:
     #   print('x<size')
        path = path+1
    if y+1 >= sizey:
         path = path
    elif Array[x,y+1] == 1:
        path = path+1
    if y-1 <= 0:
         path = path
    elif Array[x,y-1] == 1:
        path = path+1
   return path
def smoothing():
    sizex= 40
    sizey= 40
    fountainx = 32
    fountainy = 32
    Array = np.random.randint(2, size=(sizex,sizey))
#    Array = np.ones((sizex,sizey))
 #   Array = placefountain(Array, fountainx, fountainy)
    for resolution in range (5):
        for i in range (sizex):
            for j in range(sizey):
               paths = adjacencies(Array, i, j, sizex, sizey)
               #If Mode = max then do random
               #not guarunteed to swap
               #need precurser if for fountain
               #try with diagonal counting as path unless border
               #with above try allowing 2 3 or 4
               #try to implememt
               if paths == 2 or paths ==3:
                   Array[i,j] = 1
               else:
                   Array[i,j]= 0
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