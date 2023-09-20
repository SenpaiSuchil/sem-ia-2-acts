import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from perceptron_1 import *
import numpy as np


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    dim=50
    X=-1 + 2 * np.random.rand(dim)
    X2=-1 + 2 * np.random.rand(dim)
    inputs=np.vstack([X,X2])#las apila para que quede una matriz a partir de dos arreglos apilados
    _,p=inputs.shape
    Y=np.zeros(p)
    for i in range(p):#ciclo para determinar si una persona tiene sobrepeso
        #si si tiene sobrepeso Y=1, sino Y=1
        #imc= peso / (altura ** 2)
        #print((X[1,i]/(X[0,i])**2))
        1 * inputs[1,i] + -1 * inputs[0,i] + 0
        # print()
        # input()
        if 1 * inputs[1,i] + -1 * inputs[0,i] + 0 >=0:
            Y[i]=1 
            
        else:
            Y[i]=0
            #plt.plot(X[0,i],X[1,i], 'ob')
    
    neuron=Perceptron(2, 0.5)
    neuron.fit(inputs,Y)
    widget.plotData(neuron,Y,X,inputs)

    widget.show()
    sys.exit(app.exec())
