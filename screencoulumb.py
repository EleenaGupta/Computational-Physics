# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:36:25 2018

@author: studnet
"""

#screen coulumb
from pylab import *
import numpy as np
a=0
b=10
N=1000
delta=0.01
#print (delta)
x=np.linspace(a,b,N)
u=np.zeros(N)   #matrix starts from 0
for j in range (3,N):  #doesnt count 3000
      
          u[j]=-2/x[j]*math.exp(-x[j])

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