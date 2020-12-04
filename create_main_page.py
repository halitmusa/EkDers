from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
import sys
from add_main_python import Ui_MainWindow
from db_manager import DbManager
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection = DbManager()

        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)

        self.current_year = str(datetime.now().year)

        self.loader_initialize()

        self.ui.cmb_period.currentIndexChanged.connect(self.loader_month)

        self.ui.btn_calculate.clicked.connect(self.calculator)

        self.ui.le_normal_day.textChanged.connect(lambda: self.is_number(self.ui.le_normal_day))
        self.ui.le_normal_night.textChanged.connect(lambda: self.is_number(self.ui.le_normal_night))
        self.ui.le_normal_weekend.textChanged.connect(lambda: self.is_number(self.ui.le_normal_weekend))
        self.ui.le_watch.textChanged.connect(lambda: self.is_number(self.ui.le_watch))

        self.ui.le_course_day.textChanged.connect(lambda: self.is_number(self.ui.le_course_day))
        self.ui.le_course_night.textChanged.connect(lambda: self.is_number(self.ui.le_course_night))
        self.ui.le_course_weekend.textChanged.connect(lambda: self.is_number(self.ui.le_course_weekend))

        self.ui.le_special_day.textChanged.connect(lambda: self.is_number(self.ui.le_special_day))
        self.ui.le_special_night.textChanged.connect(lambda: self.is_number(self.ui.le_special_night))
        self.ui.le_special_weekend.textChanged.connect(lambda: self.is_number(self.ui.le_special_weekend))

    @staticmethod
    def is_number(obj):
        if not obj.text()[-1:].isnumeric():
            obj.setText(obj.text()[:-1])

    def loader_initialize(self):
        self.loader_current_year()
        self.loader_year()
        self.loader_period()
        self.loader_month()

    def loader_current_year(self):
        current_year_counter = self.connection.selector(f"""SELECT COUNT(name) FROM years WHERE name="{self.current_year}" """)[0][0]
        if current_year_counter == 0:
            self.connection.recorder(f"""INSERT INTO years(name) VALUES("{self.current_year}")""")

    def loader_year(self):
        self.ui.cmb_year.clear()
        year_list = [year[1] for year in self.connection.selector(f"""SELECT * FROM years""")]
        year_list.sort()
        self.ui.cmb_year.addItems(year_list)
        self.ui.cmb_year.setCurrentText(self.current_year)

    def loader_period(self):
        self.ui.cmb_period.clear()
        period_list = [i[1] for i in self.connection.selector(f"""SELECT * FROM periods""")]
        period_list.sort()
        self.ui.cmb_period.addItems(period_list)

    def loader_month(self):
        self.ui.cmb_month.clear()
        month_list = [i[1] for i in self.connection.selector(f"""SELECT * FROM months""")]
        if self.ui.cmb_period.currentText() == "1. Altı Aylık Dönem":
            self.ui.cmb_month.addItems(month_list[:6])
        else:
            self.ui.cmb_month.addItems(month_list[6:])

    def calculator(self):
        hour_dict = {"normally_day": int(self.ui.le_normal_day.text()), "normally_night": int(self.ui.le_normal_night.text()), "normally_weekend": int(self.ui.le_normal_weekend.text()),
                     "watch_hour": int(self.ui.le_watch.text()), "course_day": int(self.ui.le_course_day.text()), "course_night": int(self.ui.le_course_night.text()),
                     "course_weekend": int(self.ui.le_course_weekend.text()), "special_day": int(self.ui.le_special_day.text()), "special_night": int(self.ui.le_special_night.text()),
                     "special_weekend": int(self.ui.le_special_weekend.text())}




    def cleaner(self):
        pass

    def recorder(self):
        pass

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
