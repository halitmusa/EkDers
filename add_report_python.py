# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Erhan/Desktop/githubProject/EkDers/add_report.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(665, 769)
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lw_staff = QtWidgets.QListWidget(self.groupBox)
        self.lw_staff.setObjectName("lw_staff")
        self.gridLayout.addWidget(self.lw_staff, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lw_year = QtWidgets.QListWidget(self.groupBox_2)
        self.lw_year.setObjectName("lw_year")
        self.gridLayout_2.addWidget(self.lw_year, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.tbl_data = QtWidgets.QTableWidget(Form)
        self.tbl_data.setRowCount(14)
        self.tbl_data.setColumnCount(6)
        self.tbl_data.setObjectName("tbl_data")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_data.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_data.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tbl_data)
        self.verticalLayout.setStretch(2, 10)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Kişi"))
        self.groupBox_2.setTitle(_translate("Form", "Yıl"))
        item = self.tbl_data.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Kisi"))
        item = self.tbl_data.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Yil"))
        item = self.tbl_data.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ay"))
        item = self.tbl_data.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Brut"))
        item = self.tbl_data.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Kesinti"))
        item = self.tbl_data.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Net"))
