# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Erhan/Desktop/githubProject/EkDers/add_staff.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(545, 435)
        Form.setStyleSheet("/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0.00480769 rgba(3, 50, 76, 255),stop:0.293269 rgba(6, 82, 125, 255),stop:0.514423 rgba(8, 117, 178, 255),stop:0.745192 rgba(7, 108, 164, 255),stop:1 rgba(3, 51, 77, 255));\n"
"    color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(42, 95, 113, 255),stop:1 rgba(12, 53, 97, 255));\n"
"    color: #fff;\n"
"    border: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(167, 214, 50, 255),stop:1 rgba(98, 169, 67, 255));\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(147, 194, 30, 255),stop:1 rgba(78, 149, 47, 255));\n"
"    color: #fff;\n"
"    border: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #bfbfbf;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-color: #141414;\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView{\n"
"    background-color: transparent;\n"
"    font-size: 12pt;\n"
"    border: none;\n"
"    color: #fff;\n"
"    show-decoration-selected: 0;\n"
"    padding-left: px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected{\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(147, 194, 30, 255),stop:1 rgba(78, 149, 47, 255));\n"
"       border: none;\n"
"       border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected{\n"
"    color: #fff;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected:hover{\n"
"    color: #fff;\n"
"    background-color: #0c3561;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    \n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:vertical \n"
"{\n"
"    border: none;\n"
"    width: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"    border-radius : 0px;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(167, 214, 50, 255),stop:1 rgba(98, 169, 67, 255));\n"
"    min-height: 50px;\n"
"    width : 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(147, 194, 30, 255),stop:1 rgba(78, 149, 47, 255)); \n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover \n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:pressed \n"
"{\n"
"    background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:hover \n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:pressed \n"
"{\n"
"    background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical \n"
"{\n"
"       width: 0px;\n"
"       height: 0px;\n"
"       background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"       background-color: #0c2669;\n"
"    width: 11px;;\n"
"    \n"
"}\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.le_id_number = QtWidgets.QLineEdit(self.groupBox)
        self.le_id_number.setMinimumSize(QtCore.QSize(150, 0))
        self.le_id_number.setObjectName("le_id_number")
        self.horizontalLayout.addWidget(self.le_id_number)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.le_name = QtWidgets.QLineEdit(self.groupBox)
        self.le_name.setMinimumSize(QtCore.QSize(150, 0))
        self.le_name.setObjectName("le_name")
        self.horizontalLayout_2.addWidget(self.le_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btn_record = QtWidgets.QPushButton(self.groupBox)
        self.btn_record.setObjectName("btn_record")
        self.horizontalLayout_3.addWidget(self.btn_record)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btn_update = QtWidgets.QPushButton(self.groupBox)
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout_3.addWidget(self.btn_update)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_delete = QtWidgets.QPushButton(self.groupBox)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_3.addWidget(self.btn_delete)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lw_staff = QtWidgets.QListWidget(self.groupBox_2)
        self.lw_staff.setObjectName("lw_staff")
        self.gridLayout_2.addWidget(self.lw_staff, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Personel bilgileri"))
        self.label.setText(_translate("Form", "Personel TC : "))
        self.label_2.setText(_translate("Form", "Personel Ad soyad : "))
        self.btn_record.setText(_translate("Form", "Kaydet"))
        self.btn_update.setText(_translate("Form", "Güncelle"))
        self.btn_delete.setText(_translate("Form", "Sil"))
        self.groupBox_2.setTitle(_translate("Form", "Kayıtlı Personel"))

