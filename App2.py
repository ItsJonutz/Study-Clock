from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QTimeEdit
from PyQt6.QtCore import QTimer, QTime
from PyQt6.QtGui import QFont
import CurrentTime
class AlarmClockApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alarm Clock")

        # Current Time Display
        self.clock_label = QLabel()
        self.clock_label.setFont(QFont('Arial', 36))
        self.clock_label.setStyleSheet("color: white;")
        self.clock_label.setText("00:00:00")

        # Alarm Time Input
        self.alarm_time_edit = QTimeEdit()
        self.alarm_time_edit.setDisplayFormat("HH:mm")

        # Set Alarm Button
        self.set_alarm_btn = QPushButton("Set Alarm")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.clock_label)
        layout.addWidget(self.alarm_time_edit)
        layout.addWidget(self.set_alarm_btn)
        self.setLayout(layout)
        self.setStyleSheet("background-color: black;")

        # Timer to update clock every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)


    def update_clock(self):
        current_time = CurrentTime.get_current_time()
        self.clock_label.setText(current_time)

    def get_alarm_time(self):
        return self.alarm_time_edit.time().toString("HH:mm")
