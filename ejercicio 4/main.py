import numpy as np
import matplotlib.pyplot as plt

x1=np.array([[0,0,1,1],
             [0,1,0,1]])

y=np.array([0,1,1,1])

_,p=x1.shape
for i in range (p):
    if y[i]==0:
        plt.plot(x1[0,i],x1[1,i], 'or')
    else:
        plt.plot(x1[0,i],x1[1,i], 'ob')

m=-1
#intenté desde 1.5 que era el default para la and, bajé a 1 y quedo cortando dos resultados que si pertenecian a la or
#ahi bajé a 0.5 y cortó bien el unico resultado que debia de quedar fuera
c=0.5
x=[-2,2]
linea=[m* xi + c for xi in x]
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.plot(x, linea, '--k')
plt.grid()
plt.show()