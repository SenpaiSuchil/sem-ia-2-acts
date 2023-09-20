import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(1,figsize=(2, 2), dpi=100,sharey=True)
        super().__init__(self.fig)
        self.setParent(parent)
    

    def plotPerceptron(self,peso,pend,X,gate):
        #x1=np.array([[0,0,1,1],[0,1,0,1]])
        self.ax.clear()
        x1=X
        c=peso
        m=pend
        if gate==0:
            y=np.array([0,0,0,1])
        elif gate==1:
            y=np.array([0,1,1,1])
        elif gate==2:
            y=np.array([0,1,1,0])
        _,p=x1.shape
        for i in range (p):
            if y[i]==0:
                self.ax.plot(x1[0,i],x1[1,i], 'or')
            else:
                self.ax.plot(x1[0,i],x1[1,i], 'ob')
        #intenté desde 1.5 que era el default para la and, bajé a 1 y quedo cortando dos resultados que si pertenecian a la or
        #ahi bajé a 0.5 y cortó bien el unico resultado que debia de quedar fuera
        x=[-2,2]
        linea=[m* xi + c for xi in x]
        self.ax.plot(x, linea, '--k')
        self.ax.set(xlabel='X', ylabel='Y', title='Perceptrón')
        #self.ax.set_xlabel('X', fontsize=20)
        self.ax.grid()