#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 20:03:43 2018
@author: Alma Andersson

Created for Exercise 1. This script is not explicitly required to solve any of the questions
but can be used as to study the stability of the system as the b-parameter varies.

The whole script will generate a plot of four values as the b-parameter is varied,
namely:
    1. The real part of eigenvalue 1
    2. The imaginary part of eigenvalue 1
    3. The real part of eigenvalue 2
    4. The imaginary part of eigenvalue 2
    
Together with these the critical point for the bifurcation is marked as well.


Change the epsilon parameter in order to test for different value of epsilon

"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
#%% Creat Symbolic variables
lam = sp.Symbol('L')
x = sp.Symbol('x')
y = sp.Symbol('y')
e = sp.Symbol('e')
#%% Setup system
xc =  -(1./e - 1.)**0.5/((3./e)**0.5)
Re, Im = [[],[]],[[],[]]
stat = np.arange(-1.2,0.1,0.01)
get_real = lambda x: np.complex(sp.N(x).evalf()).real
get_imag = lambda x: np.complex(sp.N(x).evalf()).imag
epsilon = 0.1 #change to test different values of epsilon

#%% Compute eigenvalues for varying critical points -- indirectly varying b
for a in stat:
    J = sp.Matrix([[1./e*(1.-3.*x**2),-1./e],[2,-1]])
    J = J.subs([(x,a),(e,epsilon)])
    D = J.det(); Tr = J.trace()
    Q = Tr**2-4*D
    
    
    eig21 = Tr/2. + (Tr**2-4*D)**0.5/2. 
    eig22 = Tr/2. - (Tr**2-4*D)**0.5/2. 
    eig = J.eigenvals()
    val1,val2 = eig.keys()[0],eig.keys()[1]
    Re[0].append(get_real(val1)); Re[1].append(get_real(val2))
    Im[0].append(get_imag(val1)); Im[1].append(get_imag(val2))
    
Re = np.array(Re)
Im = np.array(Im)
#%% Compute values for critical point
xc = float(sp.N(xc.subs(e,epsilon)))
J_xc = sp.Matrix([[1./e*(1.-3.*x**2),-1/e],[2,-1]])
J_xc = J_xc.subs([(x,xc),(e,epsilon)])
eig_xc = J_xc.eigenvals()
val_xc1, val_xc2 = eig_xc.keys()[0],eig_xc.keys()[1]
Re_xc1 = get_real(val_xc1); Re_xc2 = get_real(val_xc2)
Im_xc1 = get_imag(val_xc1); Im_xc2 = get_imag(val_xc2)
#%% Plot Results
plt.figure(figsize=(10,5))
blist = -stat-stat**3
bc = -xc - xc**3
for i in xrange(2):
    plt.plot(blist,Re[i,:],blist,Im[i,:])
plt.plot(bc,Re_xc1,color='black',marker='o',markersize=10)
plt.axvline(bc,linestyle='--',alpha=0.8)
plt.ylim([-50,50])
plt.xlim([0,2])
plt.legend(['Re1','Im1','Re2','Im2'])
plt.xlabel(r'$b$',fontsize=20)
plt.ylabel(r'eigenvalue part',fontsize=20)
plt.title(r'Eigenvalues for different b')
