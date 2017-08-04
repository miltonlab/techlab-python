from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys


class ZeroSpinBox(QSpinBox):

    zeros = 0    
    #atZero = pyqtSignal()
    atZero = pyqtSignal(int)

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)

        self.valueChanged.connect(self.check_zero)


    def check_zero(self, value):
        if value == 0:
            ZeroSpinBox.zeros += 1
            #self.zeros += 1
            self.constant = 5
            self.atZero.emit(ZeroSpinBox.zeros)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)


        self.dial = QDial()
        self.dial.setNotchesVisible(True)

        self.spinbox = ZeroSpinBox()

        layout = QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)

        self.spinbox.atZero.connect(self.printvalue)


    def printvalue(self):
        #print ("Caught the signal!")
        print("Ha llegado a cero {0} veces ".format(ZeroSpinBox.zeros))
        








app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
