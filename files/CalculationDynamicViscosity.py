# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalculationDynamicViscosity.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(500)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setAutoRepeatInterval(100)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_9.addWidget(self.label_33)
        self.doubleSpinBox_17 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_17.setMinimumSize(QtCore.QSize(0, 24))
        self.doubleSpinBox_17.setDecimals(5)
        self.doubleSpinBox_17.setMaximum(1000000.0)
        self.doubleSpinBox_17.setProperty("value", 0.01)
        self.doubleSpinBox_17.setObjectName("doubleSpinBox_17")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_17)
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_9.addWidget(self.label_34)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(0, 24))
        self.doubleSpinBox.setDecimals(5)
        self.doubleSpinBox.setMaximum(1000000.0)
        self.doubleSpinBox.setProperty("value", 11300.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setMinimumSize(QtCore.QSize(0, 24))
        self.doubleSpinBox_2.setDecimals(5)
        self.doubleSpinBox_2.setMaximum(1000000.0)
        self.doubleSpinBox_2.setProperty("value", 10.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout.addWidget(self.doubleSpinBox_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_6.addWidget(self.label_21)
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_11.setMinimumSize(QtCore.QSize(0, 24))
        self.doubleSpinBox_11.setDecimals(5)
        self.doubleSpinBox_11.setMaximum(1000000.0)
        self.doubleSpinBox_11.setProperty("value", 950.0)
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_11)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_6.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_6.addWidget(self.label_23)
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_12.setMinimumSize(QtCore.QSize(0, 24))
        self.doubleSpinBox_12.setDecimals(5)
        self.doubleSpinBox_12.setMaximum(1000000.0)
        self.doubleSpinBox_12.setProperty("value", 1.0)
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_12)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_6.addWidget(self.label_24)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_7.addWidget(self.label_25)
        self.doubleSpinBox_13 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_13.setMinimumSize(QtCore.QSize(0, 24))
        self.doubleSpinBox_13.setDecimals(5)
        self.doubleSpinBox_13.setMaximum(1000000.0)
        self.doubleSpinBox_13.setProperty("value", 30.0)
        self.doubleSpinBox_13.setObjectName("doubleSpinBox_13")
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_13)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_7.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_7.addWidget(self.label_27)
        self.doubleSpinBox_14 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_14.setMinimumSize(QtCore.QSize(0, 24))
        self.doubleSpinBox_14.setDecimals(5)
        self.doubleSpinBox_14.setMaximum(1000000.0)
        self.doubleSpinBox_14.setProperty("value", 0.5)
        self.doubleSpinBox_14.setObjectName("doubleSpinBox_14")
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_14)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_7.addWidget(self.label_28)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_8.addWidget(self.label_29)
        self.doubleSpinBox_15 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_15.setMinimumSize(QtCore.QSize(0, 24))
        self.doubleSpinBox_15.setDecimals(5)
        self.doubleSpinBox_15.setMaximum(1000000.0)
        self.doubleSpinBox_15.setProperty("value", 1.05)
        self.doubleSpinBox_15.setObjectName("doubleSpinBox_15")
        self.horizontalLayout_8.addWidget(self.doubleSpinBox_15)
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_8.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_8.addWidget(self.label_31)
        self.doubleSpinBox_16 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_16.setMinimumSize(QtCore.QSize(0, 24))
        self.doubleSpinBox_16.setDecimals(5)
        self.doubleSpinBox_16.setMaximum(1000000.0)
        self.doubleSpinBox_16.setProperty("value", 0.01)
        self.doubleSpinBox_16.setObjectName("doubleSpinBox_16")
        self.horizontalLayout_8.addWidget(self.doubleSpinBox_16)
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_8.addWidget(self.label_32)
        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 0, 1, 1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "d1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "d2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "d3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "d4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "d5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "d"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1.56"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "1.58"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "1.63"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "1.52"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "1.7"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "-"))
        self.label_33.setText(_translate("MainWindow", "??d(????????????.)"))
        self.label.setText(_translate("MainWindow", "??"))
        self.label_3.setText(_translate("MainWindow", "????/(??^3)"))
        self.label_9.setText(_translate("MainWindow", "+-"))
        self.label_2.setText(_translate("MainWindow", "????/(??^3)"))
        self.label_21.setText(_translate("MainWindow", "??0"))
        self.label_22.setText(_translate("MainWindow", "????/(??^3)"))
        self.label_23.setText(_translate("MainWindow", "+-"))
        self.label_24.setText(_translate("MainWindow", "????/(??^3)"))
        self.label_25.setText(_translate("MainWindow", "L"))
        self.label_26.setText(_translate("MainWindow", "????"))
        self.label_27.setText(_translate("MainWindow", "+-"))
        self.label_28.setText(_translate("MainWindow", "????"))
        self.label_29.setText(_translate("MainWindow", "t"))
        self.label_30.setText(_translate("MainWindow", "??"))
        self.label_31.setText(_translate("MainWindow", "+-"))
        self.label_32.setText(_translate("MainWindow", "??"))
        self.pushButton.setText(_translate("MainWindow", "??????????????????"))
