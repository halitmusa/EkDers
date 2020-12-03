from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
from add_staff_python import Ui_Form


class StaffWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = StaffWindow()
    window.show()
    sys.exit(app.exec())
