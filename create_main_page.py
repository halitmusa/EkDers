from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QInputDialog, QMessageBox
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
        self.current_month = datetime.now().month

        self.loader_initialize()

        self.ui.cmb_period.currentIndexChanged.connect(self.loader_month)

        self.ui.btn_calculate.clicked.connect(self.calculator)
        self.ui.btn_delete.clicked.connect(self.cleaner)
        self.ui.btn_record.clicked.connect(self.recorder)

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
        self.ui.cmb_period.setCurrentIndex(0)
        if self.current_month > 6:
            self.ui.cmb_period.setCurrentIndex(1)

    def loader_month(self):
        self.ui.cmb_month.clear()
        month_list = [i[1] for i in self.connection.selector(f"""SELECT * FROM months""")]
        if self.ui.cmb_period.currentText() == "1. Altı Aylık Dönem":
            self.ui.cmb_month.addItems(month_list[:6])
            if self.current_month < 7:
                self.ui.cmb_month.setCurrentIndex(self.current_month-1)
            else:
                self.ui.cmb_month.setCurrentIndex(0)
        else:
            self.ui.cmb_month.addItems(month_list[6:])
            if self.current_month > 6:
                self.ui.cmb_month.setCurrentIndex(self.current_month - 7)
            else:
                self.ui.cmb_month.setCurrentIndex(0)

    @staticmethod
    def obj_control(obj):
        if obj.text() == "":
            return 0
        return int(obj.text())

    def calculator(self):
        year_name = self.ui.cmb_year.currentText()
        period_name = self.ui.cmb_period.currentText()
        year_id = self.connection.find(f"""SELECT id FROM years WHERE name="{year_name}" """)
        period_id = self.connection.find(f"""SELECT id FROM periods WHERE name="{period_name}" """)
        multipliers = list(self.connection.selector(f"""SELECT * FROM data WHERE yearID={year_id} AND periodID={period_id}""")[0])

        price_coefficient = multipliers[2]
        day_coefficient = multipliers[4]
        night_coefficient = multipliers[3]
        tax_rate = multipliers[5]

        # these values can selected from a database
        special_edu_multiplier = 1.25
        course_multiplier = 2
        education_state_multiplier = 1
        if self.ui.rb_graduate.isChecked():
            education_state_multiplier = 1.05
        elif self.ui.rb_doctorate.isChecked():
            education_state_multiplier = 1.15
        income_tax = 0.15
        if self.ui.rb_20.isChecked():
            income_tax = 0.2
        elif self.ui.rb_27.isChecked():
            income_tax = 0.27
        elif self.ui.rb_35.isChecked():
            income_tax = 0.35
        obj_list = [self.obj_control(self.ui.le_normal_day) * price_coefficient * education_state_multiplier * day_coefficient,
                    self.obj_control(self.ui.le_normal_night) * price_coefficient * education_state_multiplier * night_coefficient,
                    self.obj_control(self.ui.le_normal_weekend) * price_coefficient * education_state_multiplier * night_coefficient,
                    self.obj_control(self.ui.le_watch) * price_coefficient * education_state_multiplier * day_coefficient,
                    self.obj_control(self.ui.le_course_day) * price_coefficient * education_state_multiplier * day_coefficient * course_multiplier,
                    self.obj_control(self.ui.le_course_night) * price_coefficient * education_state_multiplier * night_coefficient * course_multiplier,
                    self.obj_control(self.ui.le_course_weekend) * price_coefficient * education_state_multiplier * night_coefficient * course_multiplier,
                    self.obj_control(self.ui.le_special_day) * price_coefficient * education_state_multiplier * day_coefficient * special_edu_multiplier,
                    self.obj_control(self.ui.le_special_night) * price_coefficient * education_state_multiplier * night_coefficient * special_edu_multiplier,
                    self.obj_control(self.ui.le_special_weekend) * price_coefficient * education_state_multiplier * night_coefficient * special_edu_multiplier
                    ]
        gross_total = sum(obj_list)
        income_deduction = gross_total * income_tax
        tax_deduction = gross_total * tax_rate
        total_deduction = income_deduction + tax_deduction
        net_price = gross_total - total_deduction
        self.ui.le_gross.setText(str(round(gross_total, 2)) + " TL")
        self.ui.le_deduction.setText(str(round(total_deduction, 2)) + " TL")
        self.ui.le_net.setText(str(round(net_price, 2)) + " TL")

    def cleaner(self):
        self.ui.rb_15.setChecked(True)
        self.ui.rb_nothing.setChecked(True)
        obj_list = [self.ui.le_normal_day, self.ui.le_normal_night, self.ui.le_normal_weekend, self.ui.le_watch, self.ui.le_course_day, self.ui.le_course_night, self.ui.le_course_weekend,
                    self.ui.le_special_day, self.ui.le_special_night, self.ui.le_special_weekend, self.ui.le_gross, self.ui.le_deduction, self.ui.le_net]
        for obj in obj_list:
            obj.clear()

    def recorder(self):
        month = self.ui.cmb_month.currentText()
        year = self.ui.cmb_year.currentText()
        year_id = self.connection.find(f"""SELECT id FROM years WHERE name = "{year}" """)
        month_id = self.connection.find(f"""SELECT id FROM months WHERE name = "{month}" """)

        gross = self.ui.le_gross.text()[:-3]
        deduction = self.ui.le_deduction.text()[:-3]
        net = self.ui.le_net.text()[:-3]
        if gross != "" and deduction != "" and net != "":
            staff_list = ["-".join([str(i[2]), str(i[0])]) for i in self.connection.selector(f"""SELECT * FROM staffs""")]
            name, ok_pressed = QInputDialog.getItem(self, "Seçim Ekranı", "Kayıt yapmak istediğiniz personeli seçiniz.", staff_list, 0, False)
            if ok_pressed:
                staff_id = name.split("-")[1]
                counter = self.connection.find(f"""SELECT COUNT(id) FROM staffs_prices WHERE yearID={year_id} AND monthID={month_id} AND staffID={staff_id}""")
                if counter == 0:
                    self.connection.recorder(
                        f"""INSERT INTO staffs_prices(staffID, yearID, monthID, gross, deduction, net) VALUES({staff_id}, {year_id}, {month_id}, {float(gross)}, {float(deduction)}, {float(net)})""")
                    QMessageBox.warning(self, "Dikkat", "Kayıt yapıldı.")
                else:
                    result = QMessageBox.question(self, "Dikkat", "Bu kayıt var.\nÜzerine yazmak iste misiniz?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if result == QMessageBox.Yes:
                        self.connection.updater(
                            f"""UPDATE staffs_prices SET gross={float(gross)}, deduction={float(deduction)}, net={float(net)}
                             WHERE staffID={staff_id} AND yearID={year_id} AND monthID={month_id} """)
                        QMessageBox.warning(self, "Dikkat", "Üzerine yazıldı")
        else:
            QMessageBox.warning(self, "Dikkat", "Ortada hesaplanan bir şey yok.")

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
