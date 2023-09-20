import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
import numpy as np

def plotTrigger():
    try:
        peso = float(widget.peso.text())
        pend = float(widget.pend.text())
        widget.warning.setText("")
        index=int(gateButtons.index(widget.sender()))
        archivo=open(r'tarea 1\data.txt', 'r')
        # Itera sobre las líneas del archivo
        x1=np.array(archivo.readline().split())
        x2=np.array(archivo.readline().split())
        # for linea in archivo:
        #     # Divide la línea en números utilizando el espacio como separador
        #     valores = linea.split()
        X = np.vstack((x1.astype(int), x2.astype(int)))
        widget.plotData(X,index)
    
    except ValueError:
        widget.warning.setText("Los valores no son validos!!!")
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    gateButtons=[widget.cAND, widget.cOR, widget.cXOR]
    widget.cAND.clicked.connect(plotTrigger)
    widget.cOR.clicked.connect(plotTrigger)
    widget.cXOR.clicked.connect(plotTrigger)
    widget.show()
    sys.exit(app.exec())
