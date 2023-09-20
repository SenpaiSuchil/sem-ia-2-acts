from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from canvas import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r'tarea 2\form.ui', self)

        self.chart = Canvas(self)
        self.test.addWidget(self.chart)
        

    def plotData(self, neuron, Y,X,inputs):
        self.chart.plotPerceptron(neuron,Y,X,inputs)
        self.chart.draw()
