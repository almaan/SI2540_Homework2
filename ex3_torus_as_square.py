#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 11:38:05 2018
@author: Alma Andersson

This script was used for Exercise 3 part b) as to perform of numerical integration
of the uncoupled system. 

Two test cases are available for display and may be choosen by changing the variable 'rational'
to either 'True' or 'False'

1. Rational quotient : rational = True
2. Irrational quotient : rational = False

"""

import numpy as np
import matplotlib.pyplot as plt

class Torus:
    """
    Creates the square representation of the torus with periodic boundary conditions
    with limits given as input when creating the class. Default are 2pi. Once the object
    is created use 'generate_traectory' with a set of omega_1 and omega_2 parameters and
    an optional initial condition, default is origin.
    """
    def __init__(self,lim=np.pi*2):
        self.pxlim = lim; self.nxlim = -lim
        self.pylim = lim; self.nylim = -lim 
    def periodic_boundary_conditions(self,val,lower,upper):
        if val > upper or val < lower :
            diff = upper-lower
            if val < lower:
                val = val + diff
            else:
                val = val - diff
        return val
        
    def generate_trajectory(self,o1,o2,ini=np.array([0, 0])):
        k = float(o2)/float(o1)
        dt1 = 0.05
        N = 10000
        theta1 = np.zeros(N)
        theta2 = np.zeros(theta1.shape)
        theta1[0],theta2[0] = ini
        for t in xrange(1,N):
            theta1[t] = self.periodic_boundary_conditions(theta1[t-1] + dt1,self.nxlim,self.pxlim)
            theta2[t] = self.periodic_boundary_conditions(theta2[t-1] + dt1*k,self.nylim,self.pylim)
        return theta1,theta2

def make_legend_element(o1,o2):
    string = r'$\frac{' + str(o1) + r'}{' + str(o2) + r'}$'
    return string
#%%%
if __name__ == '__main__':
    
    rational = True
    
    if rational:
        omega1 = np.array([1, 2, 7, 9])
        omega2 = np.array([7, 4, 1, 6])
        cmap = ['r','g','b','y']
    else:
        omega1 = np.array([np.pi, 1.])
        omega2 = np.array([7, 2**0.5])
        cmap = ['r','g']
    
    T = Torus()
    for w1,w2,cm in zip(omega1,omega2,cmap):
        t1,t2 = T.generate_trajectory(w1,w2,ini=np.array([2, 3]))
        plt.plot(t1,t2,color=cm,marker='.',linewidth=0,label=make_legend_element(w1,w2))
    plt.legend()
    plt.show()
