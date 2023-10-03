# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:28:11 2019

@author: uc
"""
import pylab
import numpy as np
import matplotlib.pyplot as plt 
import random
import math

L = 8
N = L**2


def create_picture(positions,colors):
    pylab.cla()
    pylab.axis([0, L, 0, L])
    pylab.setp(pylab.gca())
    for pos, col in zip(positions,colors):
        square = pylab.Rectangle((pos[0], pos[1]), 0.8, 0.8, fc = col)
        pylab.gca().add_patch(square)
 
def color(i):
    if i == 1: return 'r'
    else: return 'b'
      
##### #########################  Neighbors  ################################    
def right(i):
	if (i+1)%L == 0: return i+1-L 
	else: return i+1
	
def left(i):
	if i%L == 0: return i-1+L
	else: return i-1
	
def up(i):
	return (i+L)%N
	
def down(i):
	return (i-L+N)%N
	
neighbors = [[right(i),left(i),up(i),down(i)] for i in range(N)]

##########################################################################

coordinates = [[i%L,i//L] for i in range(N)]

orientations = [1,-1]
spins = []
colors = []

##### initial spin assignment ##################

for i in range(N):
    spin = random.choice(orientations)
    spins.append(spin)
  

##################################################


nsteps = 10000
T = 4.
delta_T = 0.1
n = 30
mean_mag = np.zeros(n)
suscep = np.zeros(n)
Temp = np.zeros(n)
for a in range(n):
    ############# Wolff Cluster Algorithm
    beta = 1/T
    p = 1-math.exp(-2.*beta)
    mag = sum(spins)
    M = []
    M.append(np.abs(mag))
    for step in range(nsteps):
        i = random.randint(0, N - 1) # Random spin selected. This will be the start of the cluster.
        cluster = [i]  # Initially the cluster consists of only this spin.
        frontier = [i] # The old frontier.
        while frontier != []:   # This checks if the frontier is empty.
            j = random.choice(frontier)
            for k in neighbors[j]:
                if spins[k] == spins[j] and k not in cluster and random.uniform(0.0, 1.0) < p:
                    frontier.append(k)
                    cluster.append(k)
            frontier.remove(j)
        for l in cluster:
            spins[l] *= -1
        M.append(np.abs(sum(spins)))
    mean_mag[a] = np.mean(M)
    Temp[a] = T
    suscep[a] = ((np.std(M))**2)/(N*T)
    
    T = T - delta_T

        
for i in range(N):
    colors.append(color(spins[i]))

create_picture(coordinates,colors)
pylab.show()
plt.plot(Temp,mean_mag)
pylab.show()
plt.plot(Temp,suscep)
pylab.show()

    