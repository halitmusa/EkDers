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
        MainWindow.resize(637, 641)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/loaded_photo/para.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("/*Copyright (c) DevSec Studio. All rights reserved.\n"
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
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(217, 217, 217, 255),stop:1 rgba(228, 228, 228, 255));\n"
"    color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(54, 197, 177, 255),stop:1 rgba(11, 135, 111, 255));\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(44, 187, 167, 255),stop:1 rgba(1, 125, 101, 255));\n"
"    color: #fff;\n"
"    font-size: 12pt;\n"
"    border-radius: 4px;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(54, 197, 177, 255),stop:1 rgba(11, 135, 111, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabWidget-----*/\n"
"QTabBar::tab \n"
"{\n"
"    font-size: 8pt;\n"
"    font-weight: bold;\n"
"    width: 80px;\n"
"    border: 1px solid #444;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"\n"
"}\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"    border: 1px solid qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(44, 187, 167, 255),stop:1 rgba(1, 125, 101, 255));;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; \n"
"\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"    margin-left: 0px; \n"
"\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #000;\n"
"    margin-top: 3px;\n"
"    background-color: #f6f6f6;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(54, 197, 177, 255),stop:1 rgba(11, 135, 111, 255));\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(44, 187, 167, 255),stop:1 rgba(1, 125, 101, 255));\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_6.addWidget(self.line_10, 1, 0, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_11.addWidget(self.line_11)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.line_6 = QtWidgets.QFrame(self.groupBox_7)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_5.addWidget(self.line_6, 2, 0, 1, 1)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_8 = QtWidgets.QLabel(self.groupBox_7)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_18.addWidget(self.label_8)
        self.cmb_year = QtWidgets.QComboBox(self.groupBox_7)
        self.cmb_year.setMinimumSize(QtCore.QSize(70, 0))
        self.cmb_year.setObjectName("cmb_year")
        self.horizontalLayout_18.addWidget(self.cmb_year)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_18)
        spacerItem = QtWidgets.QSpacerItem(23, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_15 = QtWidgets.QLabel(self.groupBox_7)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        self.cmb_period = QtWidgets.QComboBox(self.groupBox_7)
        self.cmb_period.setMinimumSize(QtCore.QSize(150, 0))
        self.cmb_period.setObjectName("cmb_period")
        self.horizontalLayout_17.addWidget(self.cmb_period)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_17)
        spacerItem1 = QtWidgets.QSpacerItem(20, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem1)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_16 = QtWidgets.QLabel(self.groupBox_7)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_20.addWidget(self.label_16)
        self.cmb_month = QtWidgets.QComboBox(self.groupBox_7)
        self.cmb_month.setMinimumSize(QtCore.QSize(100, 0))
        self.cmb_month.setObjectName("cmb_month")
        self.horizontalLayout_20.addWidget(self.cmb_month)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_20)
        self.gridLayout_5.addLayout(self.horizontalLayout_21, 1, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.groupBox_7)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_5.addWidget(self.line_7, 0, 0, 1, 1)
        self.verticalLayout_11.addWidget(self.groupBox_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem2)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_11.addWidget(self.line_5)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.le_day_normal = QtWidgets.QLineEdit(self.groupBox_3)
        self.le_day_normal.setObjectName("le_day_normal")
        self.horizontalLayout.addWidget(self.le_day_normal)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 10)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.le_day_night = QtWidgets.QLineEdit(self.groupBox_3)
        self.le_day_night.setObjectName("le_day_night")
        self.horizontalLayout_2.addWidget(self.le_day_night)
        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.le_weekend = QtWidgets.QLineEdit(self.groupBox_3)
        self.le_weekend.setObjectName("le_weekend")
        self.horizontalLayout_3.addWidget(self.le_weekend)
        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.le_watch = QtWidgets.QLineEdit(self.groupBox_3)
        self.le_watch.setObjectName("le_watch")
        self.horizontalLayout_4.addWidget(self.le_watch)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.groupBox_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.le_day_course = QtWidgets.QLineEdit(self.groupBox_4)
        self.le_day_course.setObjectName("le_day_course")
        self.horizontalLayout_9.addWidget(self.le_day_course)
        self.horizontalLayout_9.setStretch(0, 10)
        self.horizontalLayout_9.setStretch(1, 10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.le_night_course = QtWidgets.QLineEdit(self.groupBox_4)
        self.le_night_course.setObjectName("le_night_course")
        self.horizontalLayout_10.addWidget(self.le_night_course)
        self.horizontalLayout_10.setStretch(0, 10)
        self.horizontalLayout_10.setStretch(1, 10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.le_weekend_course = QtWidgets.QLineEdit(self.groupBox_4)
        self.le_weekend_course.setObjectName("le_weekend_course")
        self.horizontalLayout_11.addWidget(self.le_weekend_course)
        self.horizontalLayout_11.setStretch(0, 10)
        self.horizontalLayout_11.setStretch(1, 10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.groupBox_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.le_day_special = QtWidgets.QLineEdit(self.groupBox_5)
        self.le_day_special.setObjectName("le_day_special")
        self.horizontalLayout_12.addWidget(self.le_day_special)
        self.horizontalLayout_12.setStretch(0, 10)
        self.horizontalLayout_12.setStretch(1, 10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.le_night_special = QtWidgets.QLineEdit(self.groupBox_5)
        self.le_night_special.setObjectName("le_night_special")
        self.horizontalLayout_13.addWidget(self.le_night_special)
        self.horizontalLayout_13.setStretch(0, 10)
        self.horizontalLayout_13.setStretch(1, 10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_14.addWidget(self.label_14)
        self.le_weekend_special = QtWidgets.QLineEdit(self.groupBox_5)
        self.le_weekend_special.setObjectName("le_weekend_special")
        self.horizontalLayout_14.addWidget(self.le_weekend_special)
        self.horizontalLayout_14.setStretch(0, 10)
        self.horizontalLayout_14.setStretch(1, 10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.gridLayout_3.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.groupBox_5)
        self.horizontalLayout_16.addLayout(self.verticalLayout_8)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_16.addWidget(self.line_3)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_16.addWidget(self.line_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rb_nothing = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_nothing.setChecked(True)
        self.rb_nothing.setObjectName("rb_nothing")
        self.verticalLayout_4.addWidget(self.rb_nothing)
        self.rb_graduate = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_graduate.setObjectName("rb_graduate")
        self.verticalLayout_4.addWidget(self.rb_graduate)
        self.rb_doctorate = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_doctorate.setObjectName("rb_doctorate")
        self.verticalLayout_4.addWidget(self.rb_doctorate)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_15 = QtWidgets.QRadioButton(self.groupBox)
        self.rb_15.setChecked(True)
        self.rb_15.setObjectName("rb_15")
        self.verticalLayout.addWidget(self.rb_15)
        self.rb_20 = QtWidgets.QRadioButton(self.groupBox)
        self.rb_20.setObjectName("rb_20")
        self.verticalLayout.addWidget(self.rb_20)
        self.rb_27 = QtWidgets.QRadioButton(self.groupBox)
        self.rb_27.setObjectName("rb_27")
        self.verticalLayout.addWidget(self.rb_27)
        self.rb_35 = QtWidgets.QRadioButton(self.groupBox)
        self.rb_35.setObjectName("rb_35")
        self.verticalLayout.addWidget(self.rb_35)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.btn_calendar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calendar.setObjectName("btn_calendar")
        self.verticalLayout_10.addWidget(self.btn_calendar)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.le_gross = QtWidgets.QLineEdit(self.groupBox_6)
        self.le_gross.setEnabled(False)
        self.le_gross.setObjectName("le_gross")
        self.horizontalLayout_7.addWidget(self.le_gross)
        self.horizontalLayout_7.setStretch(0, 10)
        self.horizontalLayout_7.setStretch(1, 10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.le_deduction = QtWidgets.QLineEdit(self.groupBox_6)
        self.le_deduction.setEnabled(False)
        self.le_deduction.setObjectName("le_deduction")
        self.horizontalLayout_8.addWidget(self.le_deduction)
        self.horizontalLayout_8.setStretch(0, 10)
        self.horizontalLayout_8.setStretch(1, 10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_15.addWidget(self.label_7)
        self.le_net = QtWidgets.QLineEdit(self.groupBox_6)
        self.le_net.setEnabled(False)
        self.le_net.setObjectName("le_net")
        self.horizontalLayout_15.addWidget(self.le_net)
        self.horizontalLayout_15.setStretch(0, 10)
        self.horizontalLayout_15.setStretch(1, 10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.gridLayout_4.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.verticalLayout_10.addWidget(self.groupBox_6)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.btn_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calculate.setObjectName("btn_calculate")
        self.horizontalLayout_6.addWidget(self.btn_calculate)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_6.addWidget(self.btn_delete)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.btn_record = QtWidgets.QPushButton(self.centralwidget)
        self.btn_record.setObjectName("btn_record")
        self.horizontalLayout_6.addWidget(self.btn_record)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.verticalLayout_10.setStretch(2, 10)
        self.horizontalLayout_16.addLayout(self.verticalLayout_10)
        self.verticalLayout_11.addLayout(self.horizontalLayout_16)
        self.gridLayout_6.addLayout(self.verticalLayout_11, 1, 1, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_6.addWidget(self.line_8, 2, 1, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_6.addWidget(self.line_9, 1, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 21))
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
        self.act_add_staff = QtWidgets.QAction(MainWindow)
        self.act_add_staff.setObjectName("act_add_staff")
        self.act_add_year = QtWidgets.QAction(MainWindow)
        self.act_add_year.setObjectName("act_add_year")
        self.act_exit = QtWidgets.QAction(MainWindow)
        self.act_exit.setObjectName("act_exit")
        self.act_about = QtWidgets.QAction(MainWindow)
        self.act_about.setObjectName("act_about")
        self.actionYard_m = QtWidgets.QAction(MainWindow)
        self.actionYard_m.setObjectName("actionYard_m")
        self.menuDosya.addAction(self.act_add_staff)
        self.menuDosya.addAction(self.act_add_year)
        self.menu_k.addAction(self.act_exit)
        self.menuYard_m.addAction(self.act_about)
        self.menuYard_m.addAction(self.actionYard_m)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menu_k.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anasayfa"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Seçiminiz"))
        self.label_8.setText(_translate("MainWindow", "Yıl : "))
        self.label_15.setText(_translate("MainWindow", "Dönem :"))
        self.label_16.setText(_translate("MainWindow", "Ay :"))
        self.groupBox_3.setTitle(_translate("MainWindow", "-Normal Ücretler-"))
        self.label.setText(_translate("MainWindow", "Gündüz : "))
        self.label_2.setText(_translate("MainWindow", "Gece : "))
        self.label_3.setText(_translate("MainWindow", "Hafta Sonu :"))
        self.label_4.setText(_translate("MainWindow", "Nöbet :"))
        self.groupBox_4.setTitle(_translate("MainWindow", "-Yetiştirme Kursu-"))
        self.label_9.setText(_translate("MainWindow", "Gündüz : "))
        self.label_10.setText(_translate("MainWindow", "Gece : "))
        self.label_11.setText(_translate("MainWindow", "Hafta Sonu :"))
        self.groupBox_5.setTitle(_translate("MainWindow", "-Özel Eğitim-"))
        self.label_12.setText(_translate("MainWindow", "Gündüz : "))
        self.label_13.setText(_translate("MainWindow", "Gece : "))
        self.label_14.setText(_translate("MainWindow", "Hafta Sonu :"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Eğitim Durumu"))
        self.rb_nothing.setText(_translate("MainWindow", "Hiçbiri"))
        self.rb_graduate.setText(_translate("MainWindow", "Yüksek Lisans"))
        self.rb_doctorate.setText(_translate("MainWindow", "Doktora"))
        self.groupBox.setTitle(_translate("MainWindow", "Vergi Dilimi"))
        self.rb_15.setText(_translate("MainWindow", " %15"))
        self.rb_20.setText(_translate("MainWindow", " %20"))
        self.rb_27.setText(_translate("MainWindow", " %27"))
        self.rb_35.setText(_translate("MainWindow", " %35"))
        self.btn_calendar.setText(_translate("MainWindow", "Takvim Göster"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Sonuçlar"))
        self.label_5.setText(_translate("MainWindow", "Brüt Ücret : "))
        self.label_6.setText(_translate("MainWindow", "Kesinti : "))
        self.label_7.setText(_translate("MainWindow", "Net Ücret : "))
        self.btn_calculate.setText(_translate("MainWindow", "Hesapla"))
        self.btn_delete.setText(_translate("MainWindow", "Sil"))
        self.btn_record.setText(_translate("MainWindow", "Kaydet"))
        self.label_17.setText(_translate("MainWindow", "EK DERS HESAPLAMA PROGRAMI"))
        self.menuDosya.setTitle(_translate("MainWindow", "Ekle"))
        self.menu_k.setTitle(_translate("MainWindow", "Çıkış"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.act_add_staff.setText(_translate("MainWindow", "Kişi Ekle"))
        self.act_add_year.setText(_translate("MainWindow", "Yıl Ekle"))
        self.act_exit.setText(_translate("MainWindow", "Çıkış Yap"))
        self.act_about.setText(_translate("MainWindow", "Hakkında.."))
        self.actionYard_m.setText(_translate("MainWindow", "Yardım"))

import photos_rc
