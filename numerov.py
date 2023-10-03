import numpy as np
import matplotlib.pyplot as plt

def V(x_l,x_r,n):
    x = np.linspace(x_l,x_r,n)
    V = np.zeros(n)
    for i in range(n):
            V[i] = x[i]**2
    return V

x_l = -5
x_r = 5
n = 1000           
##def numerov(x_l,x_r,E,n):
delta = (x_r -x_l)/n
x = np.linspace(x_l,x_r,num=n)
V1 = V(x_l,x_r,n)
E = 6.4
DeltaE = 0.01
fe = 5
tol = 0.05
while(abs(fe)>tol):
    E = E + DeltaE
    K = E-V1
    
    n1 = np.where(abs(V1-E)<0.05)
    n1= n1[0][0]
    ##print(n1)
    ##print(x[n1])
    n2 = n-n1+1
    psil = np.zeros(n1)
    psir = np.zeros(n2)
    psi_derl = 0.01
    psi_derr = -0.01
    psil[1] = delta*psi_derl
    psir[1] = -delta*psi_derr
    for i in range(n1-2):
        psil[i+2] = (2*(1-(5/12.)*delta*delta*K[i+1])*psil[i+1]-(1+delta*delta*K[i]/12.)*psil[i])/(1+delta*delta*K[i+2]/12.)
    for i in range(n2-2):
        psir[i+2] = (2*(1-(5/12.)*delta*delta*K[n-(i+1)-1])*psir[i+1]-(1+delta*delta*K[n-i-1]/12.)*psir[i])/(1+delta*delta*K[n-(i+2)-1]/12)
    ##plt.plot(x[0:n1],psil)
    psir2 = np.zeros(n2)
    for i in range(n2):
        psir2[i] = psir[n2-1-i]
    k1 = psil[n1-1]
    k2 = psir2[0]
    psir2 = (k1/k2)*psir2
    #plt.plot(x[n1-1:n],psir2)
    derright = psir2[1]-psir2[0]
    derleft = psil[n1-1]-psil[n1-2]
    fe = (derleft - derright)/(delta*psil[n1-1])
    print(fe)

print(E)   ##estimated ground state energy
psi = np.concatenate((psil,psir2[1:n2]))
norm = np.vdot(psi,psi)*delta
finalpsi = psi/norm
plt.plot(x,finalpsi)
