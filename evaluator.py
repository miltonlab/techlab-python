from PyQt5.QtWidgets import QApplication, QDialog, QTextBrowser, QLineEdit, QVBoxLayout
#from PyQt5.Qt import 
import sys


class Frame(QDialog):
        def __init__(self):
               super(Frame, self).__init__()
               self.init_ui()

        def init_ui(self):
                self.txtaResult = QTextBrowser()
                self.txtInput = QLineEdit("Ingrese una expresión y presione ENTER")
                self.txtInput.selectAll()
                self.txtInput.setFocus()
                layout = QVBoxLayout()
                layout.addWidget(self.txtaResult)
                layout.addWidget(self.txtInput)
                self.txtInput.returnPressed.connect(self.compute)
                self.setLayout(layout)
                self.show()

        def compute(self):
                try:
                        text = self.txtInput.text()
                        self.txtaResult.append("{0} = <b>{1}</b>".format(
                                text, eval(text)))
                except:
                        self.txtaResult.append("<font color='red'> Expression Invalid </font>")

if __name__ == "__main__":
        app = QApplication(sys.argv)
        frame = Frame()
        #frame.show()
        app.exec()
