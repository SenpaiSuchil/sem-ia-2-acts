import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from perceptron_1 import *
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score

def metricas(neurona, X,Y):
    y_pred=neurona.predict(X)
    mean_accuracy = accuracy_score(Y,y_pred)
    conf_matrix = confusion_matrix(Y, y_pred)
    f1 = f1_score(Y, y_pred)
    widget.accuracy.setText(f"{mean_accuracy}")
    widget.matrix.setText(f"{conf_matrix}")
    widget.f1.setText(f"{f1}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    dim=100
    X=-1 + 2 * np.random.rand(dim)
    X2=-1 + 2 * np.random.rand(dim)
    inputs=np.vstack([X,X2])#las apila para que quede una matriz a partir de dos arreglos apilados
    _,p=inputs.shape
    Y=np.zeros(p)
    for i in range(p):

        1 * inputs[1,i] + -1 * inputs[0,i] + 0
        if 1 * inputs[1,i] + -1 * inputs[0,i] + 0 >=0:
            Y[i]=1 
            
        else:
            Y[i]=0
    
    neuron=Perceptron(2, 0.5)
    neuron.fit(inputs,Y)
    metricas(neuron,inputs,Y)
    widget.plotData(neuron,Y,X,inputs)
    
    widget.show()
    sys.exit(app.exec())
