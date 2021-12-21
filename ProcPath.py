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
import math
import pandas as pd
##generting hills and steps?
##or just pathways +fountain?

#diagonals dont count

def placefountain(Array, x, y):

    return Array

def segments():
    sizex = 20
    sizey = 20
    segments= np.array([np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                        
                        np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                        
                        np.array([[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                        
                        np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                        
                        np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                        
                        np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                        
                        np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                        
                        np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                        
                        np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                        
                        np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                        
                        np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                        
                        np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
                                                
                        np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]]),
                                                                        
                        
                        np.array([[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])])
    
    acceptable = False
    fail = 0
    while acceptable == False:
      Array = np.zeros((20,20),dtype=int)
      for cycle in range (4):
        z = randrange(len(segments))
        for i in range (sizex):
            for j in range (sizey):
                if segments[z][i,j] == 1:
                    Array[i,j] =1
      acceptable = evaluate(Array, sizex, sizey)
      if acceptable == False:
          fail +=1
   # print("fails =",fail)
    return Array ,fail
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
    root = getRoot(Array,sizex,sizey)
    total = 0
    navigated = []
    previous = (0,0)
    count = 0
    if root[0] == 0 and root[1] == 0:
      #  print('no root')
        return False
    for i in range(sizex):
        for j in range (sizey):
            if Array[i,j] != 0:
                total += 1
                if i + 1 < sizex:
                    if Array[i+1,j] !=0:
                        if j + 1 < sizey:
                          if Array[i,j+1] !=0 and Array[i+1,j+1] !=0:
          #                     print('Invalid block') 
                               return False

    navigated.append(countTree(Array,sizex,sizey, root[0], root[1], navigated,total,count,previous))
 #   print("Navigated = ",len(set(navigated)))
 #   print("Path tiles = ", total)
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
    if (x+1,y) != previous:
        if x+1 < sizex:
            if Array[x+1,y] != 0:
                if count > total:
                    return current
                else:
                    navigated.append(countTree(Array,sizex,sizey,x+1,y,navigated,total,count,current))
    if (x-1,y) != previous:
        if x-1 >= 0:
            if Array[x-1,y] != 0:
                if count > total:
                    return current
                else:
                    navigated.append(countTree(Array,sizex,sizey,x-1,y,navigated,total,count,current))
    if (x,y+1) != previous:
        if y+1 < sizey:
            if Array[x,y+1] != 0:
                if count > total:
                    return current
                else:
                    navigated.append(countTree(Array,sizex,sizey,x,y+1,navigated,total,count,current))
    if (x,y-1) != previous:
        if y-1 >= 0:
            if Array[x,y-1] != 0:
                if count > total:
                    return current
                else:
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
    fail = 0
    while acceptable == False:
        Array = np.random.randint(60, size=(sizex,sizey))

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
        if acceptable == 0:
            fail +=1
        
 #   print("failures =", fail)
    return Array , fail

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


def generate(Array):
    z =(randrange(900000))
    for i in range (80):
         # print(i)
        for j in range (80):
            x = float(i) * 0.1 / 3 * 3
            y = float(j) * 0.1 / 3 * 3
            a=noise.pnoise3(x + 0,y+0,z,1)

            # Array2[i,j] = a;
            if a > 0.6:
                a=1

    
            
            Array[i,j] = a;
    return Array

def minimize(Array,Array2,sizex,sizey):
    for x in range (sizex):

        for y in range(sizey):
           # print(Array2[x,y])
           count = 0
           for i in range(4):
                for j in range(4):
                    px = x * 3 + i
                    py = y*3 +j
                    
                    if Array[px,py] == 1:
                        count +=1
                       # print('w')
                    if count == 3:
                        Array2[x,y] = 1
                       # print(Array2[x,y])
    return Array2
def link(Array,sizex,sizey):
    position = [] #(x,y)
    nearest = [] #[(x,y),(x,y)]
    nearest1 = (0,0)
    nearest2= (0,0)
    temp = (0,0)
    for i in range(sizex):
        for j in range(sizey):
            if Array[i,j]  == 1:
                position.append((i,j))
                if i >= (sizex/2) :
                    nearest1 = (sizex-1,j)
                if i < (sizex/2):
                    nearest1 = (0,j)
                if j >= (sizey/2):
                    nearest2= (i,sizey-1)
                if j < (sizey/2):
                    nearest2 = (i,0)
                #nearest 2 larger
                if (math.sqrt((i-nearest1[0])**2) + math.sqrt((j-nearest1[1])**2)) < (math.sqrt((i-nearest2[0])**2) + math.sqrt((j-nearest2[1])**2)):
                    nearest2 = nearest1
                    nearest1 = temp
                nearest1= (randrange(sizex),randrange(sizey))
                    #print(i,j)
                  #  print(nearest2)
                   # print(nearest1)
                for k in range(sizex):
                    for l in range(sizey):
                        if Array[k,l] == 1:
                            if math.sqrt((i-k)**2) > 1 or math.sqrt((j-l)**2) > 1:
                                if(math.sqrt((i-k)**2) +math.sqrt((j-l)**2)) < (math.sqrt((i-nearest1[0])**2) + math.sqrt((j-nearest1[1])**2)):
                                    if (k-nearest2[0])**2 > 1 or (l-nearest2[1])**2 > 1:
                                        if (math.sqrt((i-k)**2 +(j-l)**2)) < (math.sqrt((i-nearest2[0])**2) + math.sqrt((j-nearest2[1])**2)): # check if larger than nearest 2
                                            # print(i,' ',j)
                                            # print((i-k)**2 + (j-l)**2)
                                            # print((i-nearest2[0])**2 + (j-nearest2[1])**2)
                                            nearest1 = nearest2
                                            nearest2 = (k,l)
                                            
                                        else:         #replace nearest 1
                                            nearest1 = (k,l)  
                nearest.append([nearest1,nearest2])    
                                
    # set closest to nearest y wall and nearest x wall
    # if another path seed is closer make a line to it
    # if a nearest path is adjacent to another discard it
    # after all nearest parths are found go through and connect them
   # print(len(nearest))
    for i in range(len(position)):
                x = position[i][0]
                y = position[i][1]
                finished = False
                
                while finished == False:
                    Array[x,y] = 1
                    if x < nearest[i][0][0]:
                        x +=1
                    elif x > nearest[i][0][0]:
                        x-=1
                    elif y < nearest[i][0][1]:
                        y +=1
                    elif y > nearest[i][0][1]:
                        y-=1
                    if x == nearest[i][0][0] and y == nearest[i][0][1]:
                        finished = True
                    Array[x,y] = 1
                finished = False
                x = position[i][0]
                y = position[i][1]
                while finished == False:
                    if x < nearest[i][1][0]:
                        x +=1
                    elif x > nearest[i][1][0]:
                        x-=1
                    elif y < nearest[i][1][1]:
                        y +=1
                    elif y > nearest[i][1][1]:
                        y-=1
                    if x == nearest[i][1][0] and y == nearest[i][1][1]:
                        finished =True   
                    Array[x,y] = 1
                

    return Array
def perlin():
    sizex = 20
    sizey = 20
    acceptable = False
    fail =0
    while acceptable == False:
        Array=np.zeros((80,80),dtype= int)#base case, true random
        Array2 = np.zeros((sizex,sizey),dtype=int)
        Array = generate(Array)
        Array2 = minimize(Array,Array2,sizex,sizey)
        Array2 = link (Array2,sizex,sizey)
        acceptable = evaluate(Array2,sizex,sizey)
        if acceptable == False:
            fail +=1
 #   print("failures",fail)
    return Array2 , fail

def main():
 Test = []
 Test.append (["Failures","Elapsed time","Tiles"])
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

    start = time.time()

    # base case, true random
    fig = matplotlib.pyplot.figure()
    cmap = matplotlib.colors.ListedColormap(['lightgreen','darkgray','grey'])#colours used
    if procgen == 1:
        output = perlin()
    if procgen == 2:
        output = smoothing2()
    if procgen == 3:
        output = segments()
    if procgen== 4:
        output = smoothing()


    count = 0
    for j in range(20):
        for k in range (20):
            if output[0][j,k] == 1:
                count += 1
    end = time.time()
    elapsed = end- start
    Test.append([output[1],elapsed,count])
    ax1= fig.add_subplot()
    ax1.imshow(output[0], interpolation='nearest',cmap=cmap)
 testarray = np.array(Test)

 print(pd.DataFrame(testarray))

 failT=0
 failM=0
 failm=99999
 failAv=0
 
 timeT=0
 timeM=0
 timem=99999
 timeAv=0

 tilesT=0
 tilesM=0
 tilesm=99999
 tilesAv=0
 m = 1
 for l in range(i):
    m= l +1
    fail = Test[m][0]
    failT += fail
    if fail > failM :
         failM = fail
    if fail < failm:
        failm = fail
     
    timer = Test[m][1]
    timeT += timer
    if timer > timeM :
         timeM = timer
    if timer < timem:
        timem = timer
    
    tiles = Test[m][2]
    tilesT += tiles
    if tiles > tilesM :
         tilesM = tiles
    if tiles < tilesm:
        tilesm = tiles
 
 failAv = failT/m
 timeAv = timeT/m
 tilesAv = tilesT/m
 print("Time: total =",timeT,"Average =",timeAv," Maximum =",timeM," Minimum =",timem)
 print("Tiles: total =",tilesT,"Average =",tilesAv," Maximum =",tilesM," Minimum =",tilesm)
 print("failures: total =",failT,"Average =",failAv," Maximum =",failM," Minimum =",failm)
main()