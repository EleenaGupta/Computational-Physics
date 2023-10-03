# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 10:26:53 2018

@author: studnet
"""
#square potential well and time evolution
from pylab import *
import numpy as np
import cmath
a=-50
b=50
N=1000
delta=0.1
print (delta)
x=np.linspace(a,b,N)
u=np.zeros(N)   #matrix starts from 0
for j in range (N):  
      if(abs(x[j])<1):
          u[j]=-10

H=np.zeros([N,N])
D=np.zeros([N,N])
for i in range(N):
    for j in range(N):
        if(i==j):
           D[i][j]=-2
        if(np.abs(i-j)==1):
            D[i][j]=1
print(D)
for i in range(N):
    for j in range(N):
        if(i==j):
            H[i][j]=-1*D[i][j]/(delta*delta) +u[i]
        else:
            H[i][j]=-1*D[i][j]/(delta*delta)
print(H)
Evals,Evect=np.linalg.eigh(H)   #eigen vectors
print(Evals[0:10])
#plot(x,u)
#n1=10
#plot(np.zeros(n1),Evals[0:n1],',')

#for i in range(n1):
    #plot(x,140*Evect[:,i]+Evals[i])

#%%
b1=-10
w=2
p0=2
psi0=np.zeros(N,dtype=complex)
psit=np.zeros(N,dtype=complex)

iota=np.complex(0,1)
pie=cmath.pi
#print(pie)
for i in range(N):
    psi= cmath.exp(-(x[i]-b1)**2/(4*w*w)+(1j*p0*x[i]))/(2*pie*w*w)**0.25
    psi0[i]=psi
#plot(x,psi0**2)
psiabs=abs(10*psi0)       
EvectT=np.conjugate(np.transpose(Evect)) 
Cn=np.zeros(N,dtype=complex)
for i in range (N):
    Cn[i]=psi0.dot(Evect[:,i])
#print(Cn)
#%%
def psitime(t):
       s=0.0
       for i in range(N):
           s=s+Cn[i]*cmath.exp(-iota*Evals[i]*t)*Evect[:,i]
       
       return abs(s)
       
t=6
#for t in range (0,20,1):
plot(x,u)       
plot(x,psiabs**2)   
psit=psitime(t)    
plot(x,abs(psit)**2*100)

#%%
##calculation of R,T coefficients
c=0
c=np.vdot(psit,psit)*delta
print(c)
R=0
for i in range (0,500)  :
    R=R+abs(psit[i])**2*delta
print(R)

T=0
for i in range (500,1000)  :
    T=T+abs(psit[i])**2*delta
print(T)
print(T+R)
#%%           
        
