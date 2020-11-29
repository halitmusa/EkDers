# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Erhan/Desktop/githubProject/EkDers/main_page.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/loaded_photo/para.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menu_k = QtWidgets.QMenu(self.menubar)
        self.menu_k.setObjectName("menu_k")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPersonel_Ekle = QtWidgets.QAction(MainWindow)
        self.actionPersonel_Ekle.setObjectName("actionPersonel_Ekle")
        self.actionY_l_Ekle = QtWidgets.QAction(MainWindow)
        self.actionY_l_Ekle.setObjectName("actionY_l_Ekle")
        self.action_k_Yap = QtWidgets.QAction(MainWindow)
        self.action_k_Yap.setObjectName("action_k_Yap")
        self.actionHakk_nda = QtWidgets.QAction(MainWindow)
        self.actionHakk_nda.setObjectName("actionHakk_nda")
        self.actionYard_m = QtWidgets.QAction(MainWindow)
        self.actionYard_m.setObjectName("actionYard_m")
        self.menuDosya.addAction(self.actionPersonel_Ekle)
        self.menuDosya.addAction(self.actionY_l_Ekle)
        self.menu_k.addAction(self.action_k_Yap)
        self.menuYard_m.addAction(self.actionHakk_nda)
        self.menuYard_m.addAction(self.actionYard_m)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menu_k.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anasayfa"))
        self.menuDosya.setTitle(_translate("MainWindow", "Ekle"))
        self.menu_k.setTitle(_translate("MainWindow", "Çıkış"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.actionPersonel_Ekle.setText(_translate("MainWindow", "Personel Ekle"))
        self.actionY_l_Ekle.setText(_translate("MainWindow", "Yıl Ekle"))
        self.action_k_Yap.setText(_translate("MainWindow", "Çıkış Yap"))
        self.actionHakk_nda.setText(_translate("MainWindow", "Hakkında.."))
        self.actionYard_m.setText(_translate("MainWindow", "Yardım"))

import photos_rc
