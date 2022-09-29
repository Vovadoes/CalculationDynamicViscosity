import json
import math

from PyQt5 import QtWidgets, QtGui
from typing import List

from files.CalculationDynamicViscosity import Ui_MainWindow
from files.Window import Ui_Dialog
import sys


class Window(QtWidgets.QDialog):
    def __init__(self, parent, nl: float, dnl: float, Ee: float):
        super(Window, self).__init__()
        self.ui = Ui_Dialog()
        self.parent = parent
        self.ui.setupUi(self)
        self.ui.label_2.setText('{:.3f}'.format(Ee))
        self.ui.label_7.setText('{:.3f}'.format(nl))
        self.ui.label_9.setText('{:.3f}'.format(dnl))


# System consts

path_to_A = "files/student_coefficient.json"

# Consts
G = 9.81
A = None
dG = 0.006
Nmax = 5


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.click_plus)
        self.ui.pushButton_3.clicked.connect(self.click_minus)
        self.ui.pushButton.clicked.connect(self.calculate)
        # self.ui.tableWidget.itemSelectionChanged.connect(self.on_selection)

        # self.p = 0.0
        # self.dp = 0.0
        # self.p0 = 0.0
        # self.dp0 = 0.0
        # self.l = 0.0
        # self.dl = 0.0
        # self.t = 0.0
        # self.dt = 0.0
        # self.ddnp = 0.0
        # self.run()

    def click_plus(self):
        row = self.ui.tableWidget.rowCount() + 1
        # self.ui.tableWidget.setRowCount(row)
        if row <= 10:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem("0.0"))
            # self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem("0.0"))
            self.ui.tableWidget.setVerticalHeaderLabels([f"d{i + 1}" for i in range(row)])
            # print(self.ui.tableWidget.item(0, 0).text())

    def click_minus(self):
        indexes = []
        for selectionRange in self.ui.tableWidget.selectedRanges():
            indexes.append(selectionRange.topRow())
        indexes.sort()
        j = 0
        for i in indexes:
            # print(f"{i=}", f"{j=}", f"{i-j=}")
            if self.ui.tableWidget.rowCount() > 2:
                self.ui.tableWidget.removeRow(i - j)
                j += 1
            else:
                break

        self.ui.tableWidget.setVerticalHeaderLabels(
            [f"d{i + 1}" for i in range(self.ui.tableWidget.rowCount())])
        # print("click -")

    def calculate(self):
        p = self.is_float(self.ui.doubleSpinBox)
        dp = self.is_float(self.ui.doubleSpinBox_2)
        p0 = self.is_float(self.ui.doubleSpinBox_11)
        dp0 = self.is_float(self.ui.doubleSpinBox_12)
        l = self.is_float(self.ui.doubleSpinBox_13)
        dl = self.is_float(self.ui.doubleSpinBox_14)
        t = self.is_float(self.ui.doubleSpinBox_15)
        dt = self.is_float(self.ui.doubleSpinBox_16)
        ddnp = self.is_float(self.ui.doubleSpinBox_17)
        n = self.ui.tableWidget.rowCount()
        # print(n)

        measurements = []
        flag = False
        for i in range(n):
            lst = []
            try:
                lst.append(float(self.ui.tableWidget.item(i, 0).text()))
                self.ui.tableWidget.item(i, 0).setBackground(QtGui.QColor(255, 255, 255))
            except:
                self.ui.tableWidget.item(i, 0).setBackground(QtGui.QColor(255, 0, 0))
                flag = True
                lst.append(0.0)
            measurements.append({"d": lst[0], "dd": 0.0})
        del lst
        if flag:
            print("error")
            return None

        measurements: List[dict[str:float]]
        su: float = sum([i["d"] for i in measurements]) / len(measurements)
        for i in measurements:
            i["dd"] = su - i["d"]

        # Change A to n
        with open(path_to_A, "r", encoding="UTF-8") as f:
            A = round(json.loads(f.read())[str(n)]["0.95"], 2)

        ddcn = A * math.sqrt(sum([i["dd"] ** 2 for i in measurements]) / (n * (n - 1)))

        dcp = sum([i["d"] for i in measurements]) / n

        dd = ddcn + ddnp

        E = (dG / G) + ((dp + dp0) / (p - p0)) + 2 * (dd / dcp) + (dl / l) + (dt / t)

        nl = (G / 18) * ((p - p0) / (l / 100)) * ((dcp / 1000) ** 2) * t

        dnl = nl * E

        # print(f"nl = {round(nl, 10)} +- {round(dnl, 10)} Па*с")
        # print(f"Ee = {round(E * 100, 2)} %")

        window = Window(
            self,
            nl=round(nl, 3),
            dnl=round(dnl, 3),
            Ee=round(E * 100, 3)
        )
        window.exec_()

    def is_float(self, value: QtWidgets.QDoubleSpinBox):
        try:
            a = float(value.value())
            value.setStyleSheet("QDoubleSpinBox {}")
            return a
        except:
            value.setStyleSheet("QDoubleSpinBox { background-color: red; }")
            raise ValueError()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
