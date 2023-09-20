import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(1,figsize=(2, 2), dpi=100,sharey=True)
        super().__init__(self.fig)
        self.setParent(parent)
    

    def plotPerceptron(self,neuron,Y,X,inputs):
        #x1=np.array([[0,0,1,1],[0,1,0,1]])
        self.ax.clear()
        w1,w2,b=neuron.w[0], neuron.w[1],neuron.b
        
        #x1=X
        _,p=inputs.shape
        for i in range (p):
            if Y[i]==0:
                self.ax.plot(inputs[0,i],inputs[1,i], 'or')
            else:
                self.ax.plot(inputs[0,i],inputs[1,i], 'ob')
        #intenté desde 1.5 que era el default para la and, bajé a 1 y quedo cortando dos resultados que si pertenecian a la or
        #ahi bajé a 0.5 y cortó bien el unico resultado que debia de quedar fuera
        li,ls=-1,1
        plt.plot([li,ls],
             [(1/w2)*(-w1*(li)-b),(1/w2)*(-w1*(ls)-b)], '--k')
        self.ax.set(xlabel='X', ylabel='Y', title='Perceptrón')
        #self.ax.set_xlabel('X', fontsize=20)
        self.ax.grid()