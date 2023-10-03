# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 01:15:08 2019

@author: uc
"""

import numpy as np
import math as mt
import random
import matplotlib.pyplot as plt
from os import path

def KE(velocities):
    T=0
    for i in range(N):
        T=T+ 0.5*np.vdot(velocities[i],velocities[i])
    return T

def PE(rel):
    p = 0
    relmag = np.dot(rel,rel)**(0.5)
    p = 4*((1/relmag)**12 - (1/relmag)**6)
    return p

def create_picture(positions,t,L):
    plt.cla()
    plt.axis([0, L, 0, L])
    plt.setp(plt.gca(), xticks=[0, L], yticks=[0, L])
    for x,y in positions:
        atom = plt.Circle((x, y), R, fc='r')
        plt.gca().add_patch(atom)
    #plt.savefig(path.join('H',"image-{0}.png".format(t)))
    
def vir(rel):
    r_val=np.dot(rel,rel)**(0.5)
    vir=(48)*((1/r_val)**(12)-0.5*((1/r_val)**6))
    return vir

def correction(positions,L):
    for i in range(N):
        if positions[i][0]>L:
            positions[i][0]=positions[i][0]-L
        if positions[i][0]<0:
            positions[i][0]=positions[i][0]+L
        if positions[i][1]>L:
            positions[i][1]=positions[i][1]-L
        if positions[i][1]<0:
            positions[i][1]=positions[i][1]+L
    return positions
        
def acce(rel):
    r_val=np.dot(rel,rel)**(0.5)
    acc=(48/(r_val**2))*((1/r_val)**(12)-0.5*((1/r_val)**6))*rel
    return acc

def topology(rel,L):
    if abs(rel[0])>0.5*L:
        rel[0]=rel[0]-L*np.sign(rel[0])
    if abs(rel[1])>0.5*L:
        rel[1]=rel[1]-L*np.sign(rel[1])
    return rel
    
m = 5           
N=m*m
dist = 1.2
L=(m+1)*dist
velocities = np.zeros((N,2))
positions = np.zeros((N,2))
acc=np.zeros((N,2))
R=0.4
Rc=5
i=0
vel = []
pcutoff = PE(Rc)


print(pcutoff)


row=0
col=0
while(True):
    x=dist + dist*col
    y=dist + dist*row
    positions[i][0]=x
    positions[i][1]=y
    col+=1
    i=i+1
    if col == m+1:
        row = row+1
        col= 0
        i = i-1
    if i==N:
        break
    
velocities[:,0] = np.random.normal(0,1,N)
velocities[:,1] = np.random.normal(0,1,N)
cm = (sum(velocities))/N
velocities = velocities-cm

print(sum(velocities))     
create_picture(positions,0,L)
plt.show()

'''
while(True):
    tempx=random.uniform(-1,1)
    x=random.uniform(R,L-R)
    y=random.uniform(R,L-R)
    positions[i][0]=x
    positions[i][1]=y
    for j in range(i):
        dis=mt.sqrt((positions[i][0]-positions[j][0])**2 + (positions[i][1]-positions[j][1])**2)
        if dis<dist:
            i=-1
    i=i+1
    if i==N:
        break

'''
Ptarget = 0.5
Ttarget = 0.16
trelax = 0.3
t=10
deltat=0.01
n=int(t/deltat)
FrameRate=10
t=np.linspace(0,t,n)
T=np.zeros(n)
E=np.zeros(n)
P=np.zeros(n)
temperature = np.zeros(n)
density = np.zeros(n)
PEN = np.zeros(n)
time = 0
temp = []
viri = 0
teq=5
for i in range(n):
    viri = 0
    pe = 0
    print(i)
    #for j in range(N):
    positions += velocities*(deltat/2)
    positions=correction(positions,L)
    for p in range(N-1):
        for q in range(p+1,N):
            rel=positions[p]-positions[q]
            rel=topology(rel,L)
            if mt.sqrt(np.vdot(rel,rel))<Rc:
                acc[p]+=acce(rel)
                acc[q]+=-acce(rel)
                
    #for j in range(N):
    velocities+=acc*deltat
    positions+= velocities*(deltat/2)
        
    
    positions=correction(positions,L)
    for p in range(N-1):
        for q in range(p+1,N):
            rel=positions[p]-positions[q]
            rel=topology(rel,L)
            if mt.sqrt(np.vdot(rel,rel))<Rc:
                pe += PE(rel) - pcutoff
                viri += vir(rel)
    acc=np.zeros((N,2))
    T[i]=KE(velocities)
    en = KE(velocities)
    tmean = T[i]/N
    TEMP = tmean
    Pr = N*Ttarget/(L*L) + viri/(2*L*L)
    lamb = np.sqrt(1 + (deltat/trelax)*((Ttarget/TEMP)-1))
    mu = np.sqrt(1 + (deltat/trelax)*(Pr-Ptarget))
    velocities = lamb*velocities
    
    for j in range(N):
        if(time>teq):
            vel.append(mt.sqrt(np.dot(velocities[j],velocities[j])))
    
    L = mu*L
    positions = mu*positions
    dens = N/(L*L)
    ##print(sum(velocities))
    PEN[i] = pe
    E[i] = en + pe
    temperature[i] = TEMP
    P[i] = Pr
    density[i] = dens

    time += deltat  

    
    #if (i%10==0):
        #create_picture(positions,int(i/10))
    ##print(sum(velocities))

#Teq = np.mean(temp)  
plt.show()
n2 = 1000
v = np.linspace(0,max(vel)+1,n2)
maxwell = v*np.exp(-v*v/(2*Ttarget))/(Ttarget)
plt.plot(t,T)
plt.plot(t,PEN)    
plt.plot(t,E)
plt.show()
create_picture(positions,0,L)
L_arr = np.full((N),L)
data = np.column_stack((positions,velocities,L_arr))
np.savetxt('data.dat',data)
plt.plot(t,P)
plt.show()
plt.plot(t,temperature)
plt.show()
plt.plot(t,density)
plt.show()
plt.hist(np.array(vel),50,normed=1)
plt.plot(v,maxwell)

