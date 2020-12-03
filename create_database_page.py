from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
from add_database_python import Ui_Form


class DatabaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = DatabaseWindow()
    window.show()
    sys.exit(app.exec())
