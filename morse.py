# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 09:51:24 2018

@author: studnet
"""
#morse potential
from pylab import *
import numpy as np
import math
a=-0.5
b=0.5
N=100
delta=0.01
alpha=0.01
print (delta)
x=np.linspace(a,b,N)
u=np.zeros(N)   #matrix starts from 0
for i in range (N):  
      #if(abs(x[j])<1):
          u[i]=(math.exp(-2*x[i])-2*math.exp(-x[i]))/(alpha*alpha)

H=np.zeros([N,N])
D=np.zeros([N,N])
for i in range(N):
    for j in range(N):
        if(i==j):
           D[i][j]=-2
        if(np.abs(i-j)==1):
            D[i][j]=1
#print(D)
for i in range(N):
    for j in range(N):
        if(i==j):
            H[i][j]=-1*D[i][j]/(delta*delta) +u[i]
        else:
            H[i][j]=-1*D[i][j]/(delta*delta)
#print(H)
Evals,Evect=np.linalg.eigh(H)   #eigen vectors
#%%
print(Evals[0:10]*alpha/2)

plot(x,u)
n1=5
plot(np.zeros(n1),Evals[0:n1],'.')

for i in range(n1):
    plot(x,1500*Evect[:,i]+Evals[i])
    
#%%
umin=u.min()
print(umin)  
for i in range(10):
    difference=-umin+Evals[i] 
    #print(difference)
    factor=difference*alpha/2
    print(factor)
    
    
    
    
    
    
    
    
    
    
    
    
