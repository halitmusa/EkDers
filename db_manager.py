from datetime import datetime

from PyQt5.QtWidgets import QMessageBox
import sqlite3
import os


class DbManager:
    def __init__(self):

        if os.path.isfile("./database.db"):
            self.db = sqlite3.connect("database.db")
            self.cur = self.db.cursor()
            self.cur.execute("PRAGMA foreign_keys = ON")
        else:
            self.create_database()


    @staticmethod
    def message_box(p_text):
        QMessageBox.warning(None, "Uyarı", "Bir hataya raslanıldı.\nProgram kapanacak.\n" + p_text)

    def create_database(self):
        self.db = sqlite3.connect("database.db")
        self.cur = self.db.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS "months" ("id" INTEGER NOT NULL, "name" TEXT NOT NULL UNIQUE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "periods" ("id" INTEGER NOT NULL, "name" TEXT NOT NULL UNIQUE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "years" ("id" INTEGER NOT NULL, "name" TEXT NOT NULL,PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "data" ("yearID" INTEGER NOT NULL,"periodID" INTEGER NOT NULL,"price_coefficient"	REAL NOT NULL,"night_coefficient" INTEGER NOT NULL,
        "day_coefficient" INTEGER NOT NULL,"tax_rate" REAL NOT NULL, PRIMARY KEY("yearID","periodID"),FOREIGN KEY("yearID") REFERENCES "years"("id") ON DELETE RESTRICT ON UPDATE CASCADE,
        FOREIGN KEY("periodID") REFERENCES "periods"("id") ON DELETE RESTRICT ON UPDATE CASCADE)""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "staffs" ("id" INTEGER NOT NULL,"id_number" TEXT NOT NULL UNIQUE,"name" TEXT NOT NULL, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "staffs_prices" ("id" INTEGER NOT NULL, "staffID" INTEGER NOT NULL,"yearID" INTEGER NOT NULL,"monthID" INTEGER NOT NULL,
        "gross"	REAL NOT NULL, "deduction" REAL NOT NULL, "net"	REAL NOT NULL, PRIMARY KEY("id" AUTOINCREMENT), FOREIGN KEY("staffID") REFERENCES "staffs"("id") ON DELETE RESTRICT ON UPDATE CASCADE,
        FOREIGN KEY("yearID") REFERENCES "years"("id") ON DELETE RESTRICT ON UPDATE CASCADE, FOREIGN KEY("monthID") REFERENCES "months"("id") ON DELETE RESTRICT ON UPDATE CASCADE)""")

        self.cur.execute("""INSERT INTO "months" VALUES (1,'Ocak')""")
        self.cur.execute("""INSERT INTO "months" VALUES (2,'Şubat')""")
        self.cur.execute("""INSERT INTO "months" VALUES (3,'Mart')""")
        self.cur.execute("""INSERT INTO "months" VALUES (4,'Nisan')""")
        self.cur.execute("""INSERT INTO "months" VALUES (5,'Mayıs')""")
        self.cur.execute("""INSERT INTO "months" VALUES (6,'Haziran')""")
        self.cur.execute("""INSERT INTO "months" VALUES (7,'Temmuz')""")
        self.cur.execute("""INSERT INTO "months" VALUES (8,'Ağustos')""")
        self.cur.execute("""INSERT INTO "months" VALUES (9,'Eylül')""")
        self.cur.execute("""INSERT INTO "months" VALUES (10,'Ekim')""")
        self.cur.execute("""INSERT INTO "months" VALUES (11,'Kasım')""")
        self.cur.execute("""INSERT INTO "months" VALUES (12,'Aralık')""")
        self.cur.execute("""INSERT INTO "periods" VALUES (1,'1. Altı Aylık Dönem')""")
        self.cur.execute("""INSERT INTO "periods" VALUES (2,'2. Altı Aylık Dönem')""")

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
            if "constraint failed" in str(err):
                QMessageBox.warning(None, "UYARI !!!", "Bu kayıtla ilişkili kayıtlar var.\nKaydı silemezsiniz.\nSadece güncelleme yapabilirsiniz.")
            else:
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
        self.cur.execute("PRAGMA foreign_keys = OFF")
        self.db.close()


if __name__ == "__main__":
    db_manager = DbManager()
