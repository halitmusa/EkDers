import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from create_main_page import MainWindow
from create_staff_page import StaffWindow


class App(MainWindow):
    def __init__(self):
        super().__init__()
        print("")
        # Triggered signals
        self.ui.act_add_staff.triggered.connect(lambda: self.open(StaffWindow))

    def open(self, param_class):
        self.inst = param_class()
        self.inst.setWindowModality(Qt.ApplicationModal)
        self.inst.show()


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    sys.exit(app.exec())
