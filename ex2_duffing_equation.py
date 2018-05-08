#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:24:20 2018
@author: Alma Andersson

Created for Exercise 2 with focus on the Duffing Equation.
This script will allow one to plot all the orbits of with different initial conditions
or values of epsilon. Comparission with the solution obtained when using Poincaré-Lindstedts
method.

Two different cases of analysis are provided  and may be run by changing the settings of
different variables:

    1. Dependency of omega on epsilon. Fixed initial value, varying epsilon : by_epsilon = True
    2. Dependency of omega on initial value. Fixed epsilon, varying initial values. : by_initial = True 


"""

import numpy as np
import matplotlib.pyplot as plt
from homework2 import *


def approximated_period(x0,epsilon):
    """
    Approximated solution using Poincaré-Lindstedts method.
    """
    omega = 1.0 + 3.0*x0**2/8.0*epsilon
    return omega
    

def autocorrelate(series,h=0):
    """
    Function to estimate the period of the numerical solutions
    """
    T = series.shape[0]
    tlist = np.arange(T)
    corr = np.zeros(T)
    for t in tlist:
        k = 0
        for j in xrange(T-t):
            k += 1.
            corr[t] += np.abs(series[j]-series[j+t])
        corr[t] = corr[t]/k
    if h:
        period = np.argmin(corr[1::])*h
        return corr, period
    else:
        return corr
    
class Function:
    """
    Function used in numerical integration. Here the rewritten form of the
    Duffing Equation.
    """
    def __init__(self,E):
        self.epsilon = E
    def function(self,t,y):
        return [y[1], -y[0]-self.epsilon*y[0]**3]

if __name__ == '__main__':
#%% Compare different values of epsilon, fixed initial condition
    by_epsilon = True
    if by_epsilon:
        H = 0.01
        initial_value = [1,0]
        epsilon_list = np.array([0.001,0.01,0.1,0.2,0.3,0.5])
        period,aprx_eps = [],[]
        for (neps,epsilon) in enumerate(epsilon_list):
            f1 = Function(epsilon)
            mk = Orbit_Maker(f1.function,h=H)
            t = [0,10]
            mk.generate_trajectory(t,initial_value)
            mk.plot_trajs()
            acorr, period_temp = autocorrelate(mk.traj[:,0],h=H)
            period.append(period_temp)
            aprx_eps.append(approximated_period(initial_value[0],epsilon))
        period = np.array(period)
        aprx_eps = np.array(aprx_eps)
        plt.show()
        
        plt.figure()
        plt.plot(epsilon_list,np.pi*2./period,'bo--')
        plt.plot(epsilon_list,aprx_eps,'ro--')
        plt.xlabel(r'$\epsilon$',fontsize=25)
        plt.ylabel(r'$\omega$',fontsize=25)
#%% Compare different initial value, fixed epsilon
    by_initial = False
    if by_initial:
        H = 0.01
        epsilon = 0.01
        f1 = Function(epsilon)
        mk = Orbit_Maker(f1.function,h=H)
        t = [0,10]
        timeseries,valseries = [], []
        initial_values = np.array([[0.5,0],[1,0],[2,0],[3,0],[4,0]])
        for pt in initial_values:
            mk.generate_trajectory(t,pt)
            timeseries.append(mk.time)
            valseries.append(mk.traj)
        mk.plot_trajs()
        
        period = []
        for ii in xrange(len(initial_values)):
            vals = valseries[ii][:,0]
            acorr, period_ini = autocorrelate(vals,h=H)
            period.append(period_ini)
        period = np.array(period)
            
        plt.figure()
        plt.plot(initial_values[:,0],np.pi*2.0/period,'bo--')
        plt.plot(initial_values[:,0],approximated_period(initial_values[:,0],epsilon),'ro--')
        plt.xlabel(r'$a$',fontsize=25)
        plt.ylabel(r'$\omega$',fontsize=25)