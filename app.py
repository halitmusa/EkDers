import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from create_main_page import MainWindow
from create_staff_page import StaffWindow
from create_database_page import DatabaseWindow
from create_about_page import AboutWindow
from create_help_page import HelpWindow
from create_calendar_page import CalendarWindow


class App(MainWindow):
    def __init__(self):
        super().__init__()
        # Triggered signals
        self.ui.act_add_staff.triggered.connect(lambda: self.open(StaffWindow))
        self.ui.act_add_database.triggered.connect(lambda: self.open(DatabaseWindow))
        self.ui.act_about.triggered.connect(lambda: self.open(AboutWindow))
        self.ui.act_help.triggered.connect(lambda: self.open(HelpWindow))
        self.ui.act_exit.triggered.connect(lambda: self.close())
        self.ui.btn_calendar.clicked.connect(lambda: self.open(CalendarWindow))

    def open(self, param_class):
        self.inst = param_class()
        self.inst.setWindowModality(Qt.ApplicationModal)
        self.inst.show()


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    sys.exit(app.exec())
