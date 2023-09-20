import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(1,figsize=(2, 2), dpi=100,sharey=True)
        super().__init__(self.fig)
        self.setParent(parent)
    

    def plotPerceptron(self,neuron,Y,X,inputs):

        self.ax.clear()
        w1,w2,b=neuron.w[0], neuron.w[1],neuron.b
        _,p=inputs.shape
        for i in range (p):
            if Y[i]==0:
                self.ax.plot(inputs[0,i],inputs[1,i], 'or')
            else:
                self.ax.plot(inputs[0,i],inputs[1,i], 'ob')
        li,ls=-1,1
        plt.plot([li,ls],
             [(1/w2)*(-w1*(li)-b),(1/w2)*(-w1*(ls)-b)], '--k')
        self.ax.set(xlabel='X', ylabel='Y', title='Perceptrón')
        self.ax.grid()