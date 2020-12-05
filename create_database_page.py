from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, QMessageBox
import sys
from add_database_python import Ui_Form
from db_manager import DbManager


class DatabaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.connection = DbManager()

        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)

        self.loader_year()
        self.loader_period()
        self.loader_recorded_years()
        self.import_data()

        self.ui.btn_record.clicked.connect(self.data_processor)
        self.ui.btn_update.clicked.connect(self.data_processor)
        self.ui.btn_delete.clicked.connect(self.data_processor)

        self.ui.le_night_price_coefficient.textChanged.connect(lambda: self.is_number(self.ui.le_night_price_coefficient))
        self.ui.le_day_price_coefficient.textChanged.connect(lambda: self.is_number(self.ui.le_day_price_coefficient))

        self.ui.cmb_year.currentTextChanged.connect(self.import_data)
        self.ui.cmb_period.currentTextChanged.connect(self.import_data)

    def error_message_shower(self, p_list, sender):
        control_list = p_list
        for index, state in enumerate(control_list):
            if index == 0 and not state and sender.text() == "Kaydet":
                QMessageBox.warning(self, "Dikkat", "Kayıtlı veri kaydedilemez. Ancak güncelleyebilirsiniz.")
                break
            elif index == 0 and not state and sender.text() == "Güncelle":
                QMessageBox.warning(self, "Dikkat", "Güncellemek istediğiniz kayıt mevcut değil.")
                break
            elif index == 0 and not state and sender.text() == "Sil":
                QMessageBox.warning(self, "Dikkat", "Silmek istediğiniz kayıt mevcut değil")
                break
            elif index == 1 and not state:
                QMessageBox.warning(self, "Dikkat", "Memur maaş katsayısı alanı boş geçilemez.")
                break
            elif index == 2 and not state:
                QMessageBox.warning(self, "Dikkat", "Memur maaş katsayısı alanı ondalıklı bir değer içermelidir.")
                break
            elif index == 3 and not state:
                QMessageBox.warning(self, "Dikkat", "Gündüz ücret katsayısı boş geçilemez")
                break
            elif index == 4 and not state:
                QMessageBox.warning(self, "Dikkat", "Gece ücret katsayısı boş geçilemez.")
                break
            elif index == 5 and not state:
                QMessageBox.warning(self, "Dikkat", "Damga vergisi oranı boş geçilemez.")
                break
            elif index == 6 and not state:
                QMessageBox.warning(self, "Dikkat", "Damga vergisi oranı ondalıklı bir değer olmalıdır.")
                break

    def cleaner(self):
        self.ui.lw_recorded_years.setCurrentItem(None)
        self.ui.le_staff_coefficient.clear()
        self.ui.le_day_price_coefficient.clear()
        self.ui.le_night_price_coefficient.clear()
        self.ui.le_tax_rate.clear()

    @staticmethod
    def is_number(obj):
        if not obj.text()[-1:].isnumeric():
            obj.setText(obj.text()[:-1])

    def import_data(self):
        year_name = self.ui.cmb_year.currentText()
        period_name = self.ui.cmb_period.currentText()
        year_id = self.connection.find(f"""SELECT id FROM years WHERE name="{year_name}" """)
        period_id = self.connection.find(f"""SELECT id FROM periods WHERE name="{period_name}" """)
        data_list = self.connection.selector(f"""SELECT * FROM data WHERE yearID={year_id} AND periodID={period_id}""")

        if len(data_list) > 0:
            self.ui.le_staff_coefficient.setText(str(data_list[0][2]))
            self.ui.le_day_price_coefficient.setText(str(data_list[0][4]))
            self.ui.le_night_price_coefficient.setText(str(data_list[0][3]))
            self.ui.le_tax_rate.setText(str(data_list[0][5]))
        else:
            self.cleaner()

    def loader_year(self):
        self.ui.cmb_year.clear()
        year_list = [year[1] for year in self.connection.selector(f"""SELECT * FROM years""")]
        year_list.sort()
        self.ui.cmb_year.addItems(year_list)

    def loader_period(self):
        self.ui.cmb_period.clear()
        period_list = [i[1] for i in self.connection.selector(f"""SELECT * FROM periods""")]
        period_list.sort()
        self.ui.cmb_period.addItems(period_list)

    def loader_recorded_years(self):
        self.ui.lw_recorded_years.clear()
        year_list = self.connection.selector(f"""SELECT yearID, periodID FROM data""")
        for year, period in year_list:
            year_name = self.connection.find(f"""SELECT name FROM years WHERE id={year}""")
            period_name = self.connection.find(f"""SELECT name FROM periods WHERE id={period}""")
            combined_name = "-".join([year_name, period_name])
            self.ui.lw_recorded_years.addItem(combined_name)
        self.ui.lw_recorded_years.sortItems()

    @staticmethod
    def float_controller(p_number):
        authorized_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        for character in p_number:
            if character not in authorized_list:
                return False
        return True

    def data_processor(self):
        sender = self.sender()
        year_list = self.connection.selector(f"""SELECT yearID, periodID FROM data""")
        year_name = self.ui.cmb_year.currentText()
        year_id = self.connection.find(f"""SELECT id FROM years WHERE name="{year_name}" """)
        period_name = self.ui.cmb_period.currentText()
        period_id = self.connection.find(f"""SELECT id FROM periods WHERE name="{period_name}" """)
        price_coefficient = self.ui.le_staff_coefficient.text()
        day_coefficient = self.ui.le_day_price_coefficient.text()
        night_coefficient = self.ui.le_night_price_coefficient.text()
        tax_rate = self.ui.le_tax_rate.text()
        if sender.text() == "Kaydet":
            control_list = [(year_id, period_id) not in year_list, price_coefficient != "", self.float_controller(price_coefficient), day_coefficient != "", night_coefficient != "",
                            tax_rate != "", self.float_controller(tax_rate)]
            if False not in control_list:
                self.connection.recorder(f"""INSERT INTO data VALUES ({year_id}, {period_id}, {float(price_coefficient)}, {int(day_coefficient)}, {int(night_coefficient)}, {float(tax_rate)})""")
                self.loader_recorded_years()
            else:
                self.error_message_shower(control_list, sender)
        elif sender.text() == "Güncelle":
            control_list = [(year_id, period_id) in year_list, price_coefficient != "", self.float_controller(price_coefficient), day_coefficient != "", night_coefficient != "",
                            tax_rate != "", self.float_controller(tax_rate)]
            if False not in control_list:
                self.connection.updater(f"""UPDATE data SET price_coefficient={float(price_coefficient)}, day_coefficient={int(day_coefficient)}, night_coefficient={int(night_coefficient)}, 
                tax_rate={float(tax_rate)} WHERE yearID={year_id} AND periodID={period_id} """)
                self.loader_recorded_years()
            else:
                self.error_message_shower(control_list, sender)
        elif sender.text() == "Sil":
            control_list = [(year_id, period_id) in year_list]
            if False not in control_list:
                self.connection.deleter(f"""DELETE FROM data WHERE yearID={year_id} AND periodID={period_id} """)
                self.loader_recorded_years()
                self.cleaner()
            else:
                self.error_message_shower(control_list, sender)
        else:
            pass

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = DatabaseWindow()
    window.show()
    sys.exit(app.exec())
