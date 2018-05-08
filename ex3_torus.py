#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:16:49 2018

@author: Alma Andersson

Code to generate the torus picture used in the assignment. This script is almost
an exact copy of the one found at 

https://scipython.com/book/chapter-7-matplotlib/examples/a-torus/

and thus all credit shall be given to these authors.


"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = 100

theta = np.linspace(0, 2.*np.pi, n)
phi = np.linspace(0, 2.*np.pi, n)
theta, phi = np.meshgrid(theta, phi)
c, a = 2, 1
x = (c + a*np.cos(theta)) * np.cos(phi)
y = (c + a*np.cos(theta)) * np.sin(phi)
z = a * np.sin(theta)

fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_zlim(-3,3)
ax1.plot_surface(x, y, z, rstride=5, cstride=5, color='b', edgecolors='r')
ax1.view_init(50, 90)
ax2 = fig.add_subplot(122, projection='3d')
ax2.set_zlim(-3,3)
ax2.plot_surface(x, y, z, rstride=5, cstride=5, color='b', edgecolors='r')
ax2.view_init(0, 0)
ax2.set_xticks([])
plt.show()