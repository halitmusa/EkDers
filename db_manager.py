from PyQt5.QtWidgets import QMessageBox
import sqlite3
import os


class DbManager:
    def __init__(self):
        if os.path.isfile("./database.db"):
            self.db = sqlite3.connect("database.db")
            self.cur = self.db.cursor()
        else:
            self.create_database()

    @staticmethod
    def message_box(p_text):
        QMessageBox.warning(None, "Uyarı", "Bir hataya raslanıldı.\nProgram kapanacak.\n" + p_text)

    def create_database(self):
        pass

    def recorder(self, p_text):
        try:
            self.cur.execute(p_text)
            self.db.commit()
        except sqlite3.Error as err:
            self.message_box(str(err))

    def updater(self, p_text):
        try:
            self.cur.execute(p_text)
            self.db.commit()
        except sqlite3.Error as err:
            self.message_box(str(err))

    def deleter(self, p_text):
        try:
            self.cur.execute(p_text)
            self.db.commit()
        except sqlite3.Error as err:
            self.message_box(str(err))

    def selector(self, p_text):
        try:
            self.cur.execute(p_text)
            return self.cur.fetchall()
        except sqlite3.Error as err:
            self.message_box(str(err))

    def find(self, p_text):
        try:
            self.cur.execute(p_text)
            return self.cur.fetchone()[0]
        except sqlite3.Error as err:
            self.message_box(str(err))

    def db_closer(self):
        self.db.close()


if __name__ == "__main__":
    db_manager = DbManager()
