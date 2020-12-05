from PyQt5.QtWidgets import QApplication, QWidget, QAction, QMessageBox, QInputDialog, QLineEdit, QTableWidgetItem
import sys
from add_report_python import Ui_Form
from db_manager import DbManager

from create_staff_page import StaffWindow


class ReportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.connection = DbManager()

        self.loader_staff()
        self.loader_year()

        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)

        self.ui.lw_staff.currentItemChanged.connect(self.loader_data)
        self.ui.lw_year.currentItemChanged.connect(self.loader_data)

    def loader_staff(self):
        self.ui.lw_staff.clear()
        staff_list = ["-".join([str(i[2]), str(i[0])]) for i in self.connection.selector(f"""SELECT * FROM staffs""")]
        staff_list.sort()
        self.ui.lw_staff.addItems(staff_list)

    def loader_year(self):
        self.ui.lw_year.clear()
        year_list = [year[1] for year in self.connection.selector(f"""SELECT * FROM years""")]
        year_list.sort()
        self.ui.lw_year.addItems(year_list)

    def loader_data(self):
        obj_staff = self.ui.lw_staff.currentItem()
        obj_year = self.ui.lw_year.currentItem()
        if obj_staff is not None and obj_year is not None:
            self.ui.tbl_data.clearContents()
            staff_id = obj_staff.text().split("-")[1]
            year_id = self.connection.find(f"""SELECT id FROM years WHERE name = "{obj_year.text()}" """)
            month_list = [month[1] for month in self.connection.selector(f"""SELECT * FROM months""")]
            all_data_for_year = []
            for index, month in enumerate(month_list):
                month_id = self.connection.find(f"""SELECT id FROM months WHERE name = "{month}" """)
                data_list = [data for data in self.connection.selector(f"""SELECT gross, deduction, net FROM staffs_prices WHERE staffID={staff_id} AND yearID={year_id} AND monthID={month_id}""")]
                if len(data_list) > 0:
                    all_data_for_year.append([obj_staff.text(), obj_year.text(), month] + list(data_list[0]))
            for index, row in enumerate(all_data_for_year):
                for i in range(6):
                    self.ui.tbl_data.setItem(index+1, i, QTableWidgetItem(str(row[i])))

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = ReportWindow()
    window.show()
    sys.exit(app.exec())