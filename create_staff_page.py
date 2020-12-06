from PyQt5.QtWidgets import QApplication, QWidget, QAction, QMessageBox, QInputDialog, QLineEdit
import sys
from add_staff_python import Ui_Form
from db_manager import DbManager


class StaffWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.connection = DbManager()

        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)

        self.cleaner()
        self.staff_loader()

        self.ui.btn_record.clicked.connect(self.recorder)
        self.ui.btn_update.clicked.connect(self.updater)
        self.ui.btn_delete.clicked.connect(self.deleter)

        self.ui.le_id_number.textChanged.connect(lambda: self.is_number(self.ui.le_id_number))

    def error_message_shower(self, p_list):
        control_list = p_list
        for index, error in enumerate(control_list):
            if index == 0 and not error:
                QMessageBox.warning(self, "Dikkat", "TC Kimlik No boş geçilemez.")
                break
            elif index == 1 and not error:
                QMessageBox.warning(self, "Dikkat", "TC Kimlik No 11 rakamdan oluşmalıdır.")
                break
            elif index == 2 and not error:
                QMessageBox.warning(self, "Dikkat", "Girdiğiniz kişi daha önce kaydedilmiş")
                break
            elif index == 3 and not error:
                QMessageBox.warning(self, "Dikkat", "İsim alanı boş geçilemez.")
                break
            elif index == 4 and not error:
                QMessageBox.warning(self, "Dikkat", "İsim alanı içinde en az bir karakter boşluk olmalı.")
                break
            elif index == 5 and not error:
                QMessageBox.warning(self, "Dikkat", "İsim alanı sadece boşluk ve harflerden oluşabilir")
                break
            elif index == 6 and not error:
                QMessageBox.warning(self, "Dikkat", "Güncellerken girilen TC değeri hatalı.")
                break

    @staticmethod
    def only_letter(p_text):
        letters = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p",
                   "r", "s", "ş", "t", "u", "ü", "v", "y", "z", " ", "A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H",
                   "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T", "U, ""Ü", "V", "Y", "Z"]
        for letter in p_text:
            if letter not in letters:
                return False
        return True

    @staticmethod
    def space_control(p_text):
        word_list = p_text.split()
        return " ".join(word_list)

    @staticmethod
    def is_number(obj):
        if not obj.text()[-1:].isnumeric():
            obj.setText(obj.text()[:-1])

    def staff_loader(self):
        self.ui.lw_staff.clear()
        staff_list = ["-".join([str(i[2]), str(i[0])]) for i in self.connection.selector(f"""SELECT * FROM staffs""")]
        self.ui.lw_staff.addItems(staff_list)
        self.ui.lw_staff.sortItems()

    def cleaner(self):
        self.ui.lw_staff.setCurrentItem(None)
        self.ui.le_id_number.clear()
        self.ui.le_name.clear()

    def recorder(self):
        id_number_list = [i[0] for i in self.connection.selector(f"""SELECT id_number FROM staffs""")]
        id_number = self.ui.le_id_number.text()
        name = StaffWindow.space_control(self.ui.le_name.text())
        control_list = [not len(id_number) == 0, len(id_number) == 11, id_number not in id_number_list, not len(name) == 0, name.count(" ") > 0, StaffWindow.only_letter(name)]
        if False not in control_list:
            self.connection.recorder(f"""INSERT INTO staffs (id_number, name) VALUES("{id_number}","{name}") """)
            self.staff_loader()
            self.cleaner()
        else:
            self.error_message_shower(control_list)

    def updater(self):
        obj = self.ui.lw_staff.currentItem()
        if obj is not None:
            id_number_list = [i[0] for i in self.connection.selector(f"""SELECT id_number FROM staffs""")]
            index = (obj.text().split("-"))[1]
            old_id_number, old_name = self.connection.selector(f"""SELECT id_number, name FROM staffs WHERE id={index}""")[0]
            new_id_number, ok_pressed = QInputDialog.getText(self, "Cevap ver", "Yeni Değer:", QLineEdit.Normal, old_id_number)
            new_name, ok_pressed = QInputDialog.getText(self, "Cevap ver", "Yeni Değer:", QLineEdit.Normal, old_name)
            if old_id_number == new_id_number:
                control_list = [True, True, True, not len(new_name) == 0, new_name.count(" ") > 0,
                                StaffWindow.only_letter(new_name)]
            else:
                control_list = [not len(new_id_number) == 0, len(new_id_number) == 11, new_id_number not in id_number_list, not len(new_name) == 0, new_name.count(" ") > 0,
                                StaffWindow.only_letter(new_name), new_id_number.isnumeric()]
            if False not in control_list:
                self.connection.updater(f"""UPDATE staffs SET id_number="{new_id_number}", name="{new_name}" WHERE id_number="{old_id_number}" """)
            else:
                if not new_id_number == "" and not new_name == "":
                    self.error_message_shower(control_list)
            self.staff_loader()
        else:
            QMessageBox.warning(self, "Dikkat", "Önce seçim yapmalısınız.")

    def deleter(self):
        obj = self.ui.lw_staff.currentItem()
        if obj is not None:
            index = (obj.text().split("-"))[1]
            id_number = self.connection.selector(f"""SELECT id_number FROM staffs WHERE id={index}""")[0][0]
            self.connection.deleter(f"""DELETE FROM staffs WHERE id_number="{id_number}" """)
            self.staff_loader()
        else:
            QMessageBox.warning(self, "Dikkat", "Önce seçim yapmalısınız.")

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = StaffWindow()
    window.show()
    sys.exit(app.exec())
