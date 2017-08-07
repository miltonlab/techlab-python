import gui.dialog
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
#import PyQt5.QtCore import

class TestQtDesigner(QMainWindow, gui.dialog.Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    form = TestQtDesigner()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()