# all application code goes here (pyqt6) 

from PyQt6.QtWidgets import Qwidget, QLabel

class AlarmClockApp(Qwidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("clock")
        self.setGeometry(100, 100, 600, 400)
        
        label = QLabel("Hello, PyQt6!", self)
        label.setGeometry(200, 150, 200, 50)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        