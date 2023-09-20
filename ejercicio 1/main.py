import numpy as np
import matplotlib.pyplot as plt


x1= np.array([(0,0), (0,1), (1,0), (1,1)])
x2=np.array([0,0,0,1])
coor=(1.5,0.5)
pendiente=-0.5



plt.plot(0,0, 'x', color='red')
plt.plot(0,1, 'x', color='red')
plt.plot(1,0, 'x', color='red')
plt.plot(1,1, 'o', color='blue')
#plt.plot(x1[0], 'x', color='red')
#plt.plot(x1[1], 'x', color='red')
#plt.plot(x1[2], 'x', color='red')
#plt.plot(x1[3], 'o', color='blue')
plt.axline(coor,slope=pendiente)
plt.grid()
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

#y dibuje una linea (Y = mX + c) con m = -1 y c= 1.5