import sys
from PyQt5.QtWidgets import QApplication
from create_main_page import MainWindow


class App(MainWindow):
    def __init__(self):
        super().__init__()
        print("")
        # Triggered signals


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    sys.exit(app.exec())
