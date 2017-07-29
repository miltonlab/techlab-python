from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.Qt import QTime, QTimer
from PyQt5.Qt import Qt
import sys
import time

msg = "Welcome to PyQt World"
if len(sys.argv) < 2:
	raise ValueError("Missing command line arguments")

hours, minutes = sys.argv[1].split(":")
end = QTime(int(hours), int(minutes))

if not end.isValid():
	raise ValueError("Error in arguments")

if len(sys.argv) > 2:
	msg = " ".join(sys.argv[2:])

app = QApplication(sys.argv)
while QTime.currentTime() < end:
	time.sleep(5)
label = QLabel("<h1>" + msg + " " + hours + ":" + minutes + "</h1>")
label.setWindowFlag(Qt.SplashScreen)
label.show()
QTimer.singleShot(2000, app.quit)

app.exec()
