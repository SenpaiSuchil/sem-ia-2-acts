from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from canvas import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(r'tarea 1\form.ui', self)

        self.chart = Canvas(self)
        self.test.addWidget(self.chart)
        

    def plotData(self, X, gate):
        peso=float(self.peso.text())
        pend=float(self.pend.text())
        self.chart.plotPerceptron(peso,pend,X,gate)
        self.chart.draw()
