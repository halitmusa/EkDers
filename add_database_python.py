# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Erhan/Desktop/githubProject/EkDers/add_database.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(487, 315)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
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
"QWidget{\n"
"    background-color: #e6e7eb;\n"
"}\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #000000;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar\n"
"{\n"
"    background-color: #d6e1f0;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background-color: #a7dfff;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background-color: #98daff;\n"
"    border: 1px solid #000;\n"
"    margin-bottom: -1px;\n"
"    padding-bottom: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #beccde;\n"
"    border: 1px solid;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu QWidget{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #6d8eff;\n"
"    color: #ffffff;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    min-width : 150px;\n"
"    padding: 3px 20px 3px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #d6e1f0;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #262626;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBar-----*/\n"
"QToolBar\n"
"{\n"
"    background-color: #d6e1f0;\n"
"    color: #ffffff;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"    background-color: #d6e1f0;\n"
"    color: #ffffff;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    background-color: #f0f5f3;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::checked:hover\n"
"{\n"
"    background-color: #5cc4ff;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"    background-color: #5cc4ff;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::checked\n"
"{\n"
"    background-color: #5cc4ff;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    show-decoration-selected: 0;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolTip-----*/\n"
"QToolTip\n"
"{\n"
"    border: 1px solid black;\n"
"    background-color: #b2c1d5;\n"
"    border-radius: 0px;\n"
"    color: #000;\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit{\n"
"    background-color: #fefffc;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTextEdit-----*/\n"
"QTableWidget{\n"
"    background-color: #fff;\n"
"    padding: 10px;\n"
"    \n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: #fefefe;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 0px;\n"
"    padding-left: 6px;\n"
"    color: #000;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #fefefe;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #dcdcdf;\n"
"    color: #000;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #217346;\n"
"    selection-color: #dcdcdf;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; \n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(\"./ressources/down_arrow.png\");\n"
"    width:8px;\n"
"    height:8px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox-----*/\n"
"QSpinBox\n"
"{\n"
"    background-color: #fefefe;\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    color: #000;\n"
"    padding: 2px;\n"
"    selection-background-color: #4e4e8f;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, \n"
"QSpinBox::down-button\n"
"{\n"
"    background-color: #fefefe;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, \n"
"QSpinBox::down-button:hover\n"
"{\n"
"    background-color: #fefefe;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, \n"
"QSpinBox::down-button:pressed\n"
"{\n"
"    background-color: #ebebeb;\n"
"    border: 1px solid #ebebeb;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow\n"
"{\n"
"    image: url(\"./ressources/down_arrow.png\");\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow\n"
"{\n"
"    image: url(\"./ressources/up_arrow.png\");\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSlider \n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"\n"
"}\n"
"\n"
"QSlider::groove:horizontal \n"
"{\n"
"    subcontrol-origin: content;\n"
"    background-color: transparent;\n"
"    height: 15px;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"    background-color: #4ebfff;\n"
"    width: 15px;\n"
"    border-radius: 7px;\n"
"\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal \n"
"{\n"
"    background-color: #999;\n"
"    margin: 5px;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"    background-color: #666;\n"
"    margin: 5px;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: #beccde;\n"
"    border: 1px solid darkgray;\n"
"    height: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: 1px solid gray;\n"
"    min-width: 100px;\n"
"    background-color: #e6edf6;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: #beccde;\n"
"    border: 1px solid darkgray;\n"
"    width: 14px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: 1px solid gray;\n"
"    min-height: 100px;\n"
"    background-color: #e6edf6;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QStatusBar-----*/\n"
"QStatusBar\n"
"{\n"
"    background-color: #d6e1f0;\n"
"    color: #000000;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMinimumSize(QtCore.QSize(120, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cmb_year = QtWidgets.QComboBox(self.groupBox_2)
        self.cmb_year.setObjectName("cmb_year")
        self.horizontalLayout.addWidget(self.cmb_year)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setMinimumSize(QtCore.QSize(120, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.cmb_period = QtWidgets.QComboBox(self.groupBox_2)
        self.cmb_period.setObjectName("cmb_period")
        self.horizontalLayout_2.addWidget(self.cmb_period)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setMinimumSize(QtCore.QSize(120, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.le_staff_coefficient = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_staff_coefficient.setObjectName("le_staff_coefficient")
        self.horizontalLayout_3.addWidget(self.le_staff_coefficient)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setMinimumSize(QtCore.QSize(120, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.le_day_price_coefficient = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_day_price_coefficient.setObjectName("le_day_price_coefficient")
        self.horizontalLayout_4.addWidget(self.le_day_price_coefficient)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setMinimumSize(QtCore.QSize(120, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.le_night_price_coefficient = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_night_price_coefficient.setObjectName("le_night_price_coefficient")
        self.horizontalLayout_5.addWidget(self.le_night_price_coefficient)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMinimumSize(QtCore.QSize(120, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.le_tax_rate = QtWidgets.QLineEdit(self.groupBox_2)
        self.le_tax_rate.setObjectName("le_tax_rate")
        self.horizontalLayout_6.addWidget(self.le_tax_rate)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.btn_record = QtWidgets.QPushButton(Form)
        self.btn_record.setObjectName("btn_record")
        self.horizontalLayout_7.addWidget(self.btn_record)
        self.btn_update = QtWidgets.QPushButton(Form)
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout_7.addWidget(self.btn_update)
        self.btn_delete = QtWidgets.QPushButton(Form)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_7.addWidget(self.btn_delete)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_8.addWidget(self.line)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_8.addWidget(self.line_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lw_recorded_years = QtWidgets.QListWidget(self.groupBox)
        self.lw_recorded_years.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lw_recorded_years.setObjectName("lw_recorded_years")
        self.gridLayout.addWidget(self.lw_recorded_years, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "Veri Girişi"))
        self.label.setText(_translate("Form", "Yıl : "))
        self.label_6.setText(_translate("Form", "Dönem : "))
        self.label_2.setText(_translate("Form", "Memur Maaş Katsayısı : "))
        self.label_4.setText(_translate("Form", "Gündüz Ücret Katsayısı : "))
        self.label_5.setText(_translate("Form", "Gece Ücret Katsayısı : "))
        self.label_3.setText(_translate("Form", "Damga Vergisi Oranı : "))
        self.btn_record.setText(_translate("Form", "Kaydet"))
        self.btn_update.setText(_translate("Form", "Güncelle"))
        self.btn_delete.setText(_translate("Form", "Sil"))
        self.groupBox.setTitle(_translate("Form", "Kayıtlı Yıllar"))

