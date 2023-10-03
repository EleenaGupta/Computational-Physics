# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:17:17 2019

@author: uc
"""

import pylab
import numpy as np
import matplotlib.pyplot as plt
import random
import math
L = 8
N = L**2 # Number of spins
J = 1.0 # Coupling strength
def create_picture(positions,colors): ## Graphical visualisation of spins
    pylab.cla()
    pylab.axis([0, L, 0, L])
    pylab.setp(pylab.gca())
    for pos, col in zip(positions,colors):
        square = pylab.Rectangle((pos[0], pos[1]), 0.8, 0.8, fc = col)
        pylab.gca().add_patch(square)
def color(i):
    if i == 1: return 'r'# Red: `up'
    else: return 'b' # Blue: `down'
##### ######################### Computes neighbors for ith spin #########
############## Identification of opposite edges is taken into account #####
def right(i): # Neighbor to the right
    if (i+1)%L == 0: return i+1-L
    else: return i+1
def left(i): # Neighbor to the left
    if i%L == 0: return i-1+L
    else: return i-1
def up(i): # Neighbor up
    return (i+L)%N
def down(i): # Neighbor down
    return (i-L+N)%N
neighbors = [[right(i),left(i),up(i),down(i)] for i in range(N)] # Neighbor table
##########################################################################
coordinates = [[i%L,i//L] for i in range(N)] ## Coordinates of spins (squares) for
## graphical output
orientations = [1,-1]
spins = []
colors = []
##### initial random spin assignment ##################
for i in range(N):
    spin = random.choice(orientations)
    spins.append(spin)
##################################################
mean_mag = []
T = np.linspace(1.5,3.5,30)
nsteps = 10000*N # Number of steps in the Metropolis algorithm
for i in T:
    beta = 1/i
    mag,counter = 0,0
    ### Metropolis algorithm ###
    for step in range(nsteps):
        k = random.randint(0, N - 1) ### Random spin choice
        delta_E = 2.0 * spins[k] * sum(spins[j] for j in neighbors[k]) ## Change in energy
        if random.uniform(0.0, 1.0) < math.exp(-beta * delta_E): # Metropolis acceptance probability
            spins[k] *= -1 ## Spin flipped after accepting the proposed flip
        if(step > nsteps/2 and (nsteps % N == 0 )):
            mag = mag + abs(sum(spins))
            counter += 1
    mean_mag.append(mag/(counter*N))
    

for i in range(N):
    colors.append(color(spins[i]))
create_picture(coordinates,colors)
pylab.show()
mean_mag = np.array(mean_mag)
plt.plot(T,abs(mean_mag),'.')
plt.show()
print(1)