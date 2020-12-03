from PyQt5.QtWidgets import QApplication, QWidget
import sys
from add_calendar_python import Ui_Form


class CalendarWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Takvim")


if __name__ == "__main__":
    app = QApplication([])
    window = CalendarWindow()
    window.show()
    sys.exit(app.exec())
