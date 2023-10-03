# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:49:31 2018

@author: studnet
"""

from pylab import *
import numpy as np
a=-10
b=10
N=2000
delta=0.01
#print (delta)
x=np.linspace(a,b,N)
u=np.zeros(N)   #matrix starts from 0
for j in range (3,N):  #doesnt count 3000
      
          u[j]=x[j]**2

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
print(Evals[0:10])
#%%
plot(x,u)
n1=5
plot(np.zeros(n1),Evals[0:n1],',')

for i in range(n1):
    plot(x,140*Evect[:,i]+Evals[i])