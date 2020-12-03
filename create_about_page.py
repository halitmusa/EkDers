from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
from add_about_python import Ui_Dialog


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Hakkında")
        self.ui.btn_ok.clicked.connect(lambda: self.close())


if __name__ == "__main__":
    app = QApplication([])
    window = AboutWindow()
    window.show()
    sys.exit(app.exec())
