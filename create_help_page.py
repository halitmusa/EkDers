from PyQt5.QtWidgets import QApplication, QWidget
import sys
from add_help_python import Ui_Dialog


class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Yardım Sayfası")
        self.ui.btn_ok.clicked.connect(lambda: self.close())


if __name__ == "__main__":
    app = QApplication([])
    window = HelpWindow()
    window.show()
    sys.exit(app.exec())
