#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:24:20 2018
@author: Alma Andersson

Created for Exercise 1. A small script just to better visualize the typical
solutions to the Fitzhugh-Nagumo model as constructed in the exercise.

"""

import numpy as np
import matplotlib.pyplot as plt
from homework2 import *
    
class Function:
    """
    Fitzhugh Nagumo dynamical system. 
    Function to be used for the numerical integration.
    """
    def __init__(self,b):
        self.b = b
    def function(self,t,y):
        return [100*(y[0]-y[0]**3-y[1]), 2*y[0]-y[1]+self.b]
    
if __name__ == '__main__':
#%% Setup and perform integration
    b1 = 0. #Specify this parameter to test for different systems
    T = [0,100]
    y0 = [1,0]
    fun = Function(b1)
    system = Orbit_Maker(fun.function,h=0.01)
    system.generate_trajectory(T,y0)
#%% Plot result
    xt = system.traj[:,0]
    yt = system.traj[:,1]
    time = np.arange(T[0],T[1],0.01)
    plt.plot(time,xt,'b')
    plt.plot(time,yt,'r')
    plt.xlim([0,10])
    plt.legend(['x','y'])