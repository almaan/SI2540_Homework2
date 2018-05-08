#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 12:48:36 2018

@author: almz
"""
import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt

class Orbit_Maker:
    def __init__(self,f,**kwargs):
        self.f = f
        self.h = kwargs.pop('h', 0.01)
        self.r = ode(f).set_integrator('dopri5')
        self.fig, self.ax = plt.subplots(1,1)
    def generate_trajectory(self,tt,y0,plot=True):
       self.time = []
       self.r.set_initial_value(y0,tt[0])
       self.traj = []
       while self.r.successful() and self.r.t < tt[1]:
          self.r.integrate(self.r.t + self.h)
          self.traj.append(self.r.y)
          self.time.append(self.r.t+self.h)
       self.traj = np.array(self.traj)
       if plot:
           self.ax.plot(self.traj[:,0],self.traj[:,1])
    def plot_trajs(self,):
         self.ax.set_title('Phase Portrait')
         self.ax.set_xlabel(r'$x$',fontsize=25)
         self.ax.set_ylabel(r'$y$',fontsize=25)
         plt.show()