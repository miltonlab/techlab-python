from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtWidgets import QLabel, QComboBox, QDoubleSpinBox
from PyQt5.QtWidgets import QGridLayout
import sys
import urllib3
import json
        
class Frame(QDialog):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.get_data() # get date and rates
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(self.date)
        self.cmbFrom = QComboBox()
        self.cmbTo = QComboBox()
        self.cmbFrom.addItems(self.rates)
        self.cmbTo.addItems(self.rates)

        self.spnFrom = QDoubleSpinBox()
        self.spnFrom.setRange(0.01, 1000)
        self.spnFrom.setValue(1.00)

        self.lblTo = QLabel('1.00')

        layout = QGridLayout()
        layout.addWidget(dateLabel, 0, 0)
        layout.addWidget(self.cmbFrom, 1, 0)
        layout.addWidget(self.cmbTo, 2, 0)
        layout.addWidget(self.spnFrom, 1, 1)
        layout.addWidget(self.lblTo, 2, 1)
        self.setLayout(layout)

        self.cmbFrom.currentIndexChanged.connect(self.update_ui)
        self.cmbTo.currentIndexChanged.connect(self.update_ui)
        self.spnFrom.valueChanged.connect(self.update_ui)

        
    def get_data(self):
        self.rates = {}
        http = urllib3.PoolManager()
        #from_ = self.cmbFrom.currentText()
        #to_ = self.cmbTo.currentText()
        r = http.request('GET', 'http://api.fixer.io/latest')
        data = json.loads(r.data.decode('utf-8'))
        self.rates = data['rates']
        self.date = data['date']

    def update_ui(self):
        from_ = self.cmbFrom.currentText()
        to_ = self.cmbTo.currentText()
        results = (self.rates[from_] /self.rates[to_]) * self.spnFrom.value()
        self.lblTo.setText("%0.2f" % results)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Frame()
    win.show()
    app.exec_()
    
