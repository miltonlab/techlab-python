# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 22:46:06 2017

@author: miltonlab
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidgets.QMainWindow()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())